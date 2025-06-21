from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import pandas as pd
import firebase_admin
from firebase_admin import credentials, db
import os
from dotenv import load_dotenv
import json
from typing import List, Dict, Any
import tempfile
from datetime import datetime, timedelta
import re
import uuid

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI(title="Excel Data Processor", version="1.0.0")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",  # Local development
        "https://*.onrender.com", # Render frontend
        "https://*.netlify.app",  # Netlify frontend (all subdomains)
        "https://creative-puffpuff-5a6348.netlify.app",  # Specific Netlify URL
        "https://*.vercel.app",   # Vercel frontend
        "https://*.railway.app",  # Railway frontend
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize Firebase
try:
    # Check if Firebase is already initialized
    firebase_admin.get_app()
except ValueError:
    # Initialize Firebase with service account
    firebase_service_account = os.getenv('FIREBASE_SERVICE_ACCOUNT')
    firebase_database_url = os.getenv('FIREBASE_DATABASE_URL')
    
    if firebase_service_account:
        # For deployment - service account from environment variable
        try:
            service_account_info = json.loads(firebase_service_account)
            cred = credentials.Certificate(service_account_info)
        except json.JSONDecodeError:
            raise ValueError("FIREBASE_SERVICE_ACCOUNT environment variable contains invalid JSON")
    else:
        # For local development - service account from file
        service_account_path = "firebase-service-account.json"
        if not os.path.exists(service_account_path):
            raise FileNotFoundError(
                f"Firebase service account file '{service_account_path}' not found. "
                "For deployment, set FIREBASE_SERVICE_ACCOUNT environment variable with the JSON content. "
                "For local development, ensure the service account file exists."
            )
        cred = credentials.Certificate(service_account_path)
    
    if not firebase_database_url:
        raise ValueError(
            "FIREBASE_DATABASE_URL environment variable is required. "
            "Set it to your Firebase Realtime Database URL (e.g., https://your-project-id.firebaseio.com)"
        )
    
    try:
        firebase_admin.initialize_app(cred, {
            'databaseURL': firebase_database_url
        })
        print(f"Firebase initialized successfully with database URL: {firebase_database_url}")
    except Exception as e:
        print(f"Error initializing Firebase: {str(e)}")
        raise e

# Get database reference
try:
    db_ref = db.reference()
    # Test the connection
    test_result = db_ref.child('test_connection').get()
    print("Firebase database connection successful")
except Exception as e:
    print(f"Error connecting to Firebase database: {str(e)}")
    # Create a mock database reference for development
    db_ref = None

# Session management
active_sessions = {}

def sanitize_column_name(column_name):
    """Sanitize column names for Firebase compatibility"""
    if not column_name:
        return "unnamed_column"
    
    # Convert to string and remove/replace invalid characters
    sanitized = str(column_name)
    
    # Remove or replace invalid characters: $ # [ ] / . and spaces
    sanitized = re.sub(r'[\$#\[\]/\.\s]', '_', sanitized)
    
    # Remove leading/trailing underscores
    sanitized = sanitized.strip('_')
    
    # Ensure it's not empty
    if not sanitized:
        return "unnamed_column"
    
    # Ensure it doesn't start with a number
    if sanitized[0].isdigit():
        sanitized = "col_" + sanitized
    
    return sanitized

def serialize_data(data):
    """Convert data to JSON serializable format"""
    if isinstance(data, list):
        return [serialize_data(item) for item in data]
    elif isinstance(data, dict):
        return {key: serialize_data(value) for key, value in data.items()}
    elif isinstance(data, (datetime, pd.Timestamp)):
        return data.isoformat()
    elif hasattr(data, 'timestamp'):  # Handle datetime objects
        return data.isoformat() if hasattr(data, 'isoformat') else str(data)
    elif pd.isna(data):  # Handle NaN values
        return None
    else:
        return data

def cleanup_expired_sessions():
    """Clean up expired sessions"""
    if not db_ref:
        return
        
    current_time = datetime.now()
    expired_sessions = []
    
    for session_id, session_data in active_sessions.items():
        if current_time - session_data['created_at'] > timedelta(hours=24):  # 24 hour expiry
            expired_sessions.append(session_id)
    
    for session_id in expired_sessions:
        # Clear data for expired session
        db_ref.child(f'sessions/{session_id}').delete()
        del active_sessions[session_id]

@app.get("/")
async def root():
    """Root endpoint"""
    return {"message": "Excel Data Processor API", "version": "1.0.0"}

@app.get("/debug")
async def debug_info():
    """Debug endpoint to check environment variables and Firebase status"""
    try:
        firebase_service_account = os.getenv('FIREBASE_SERVICE_ACCOUNT')
        firebase_database_url = os.getenv('FIREBASE_DATABASE_URL')
        
        # Test Firebase connection
        test_data = db_ref.child('test').get()
        
        return {
            "firebase_service_account_set": bool(firebase_service_account),
            "firebase_database_url_set": bool(firebase_database_url),
            "firebase_database_url": firebase_database_url,
            "firebase_connection_test": "success" if test_data is not None else "failed",
            "environment_variables": {
                "FIREBASE_SERVICE_ACCOUNT_length": len(firebase_service_account) if firebase_service_account else 0,
                "FIREBASE_DATABASE_URL": firebase_database_url
            }
        }
    except Exception as e:
        return {
            "error": str(e),
            "firebase_service_account_set": bool(os.getenv('FIREBASE_SERVICE_ACCOUNT')),
            "firebase_database_url_set": bool(os.getenv('FIREBASE_DATABASE_URL')),
            "firebase_database_url": os.getenv('FIREBASE_DATABASE_URL')
        }

@app.post("/upload-excel")
async def upload_excel(file: UploadFile = File(...)):
    """
    Upload and process Excel file
    """
    if not db_ref:
        raise HTTPException(status_code=500, detail="Firebase database not available")
        
    if not file or not file.filename or not file.filename.endswith(('.xlsx', '.xls')):
        raise HTTPException(status_code=400, detail="Only Excel files are allowed")
    
    try:
        # Save uploaded file temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix='.xlsx') as tmp_file:
            content = await file.read()
            tmp_file.write(content)
            tmp_file_path = tmp_file.name
        
        # Read Excel file
        df = pd.read_excel(tmp_file_path)
        
        # Clean up temporary file
        os.unlink(tmp_file_path)
        
        # Sanitize column names
        original_columns = list(df.columns)
        sanitized_columns = [sanitize_column_name(col) for col in original_columns]
        
        # Create mapping for frontend
        column_mapping = dict(zip(sanitized_columns, original_columns))
        
        # Rename columns in DataFrame
        df.columns = sanitized_columns
        
        # Convert DataFrame to list of dictionaries and serialize datetime objects
        data = df.to_dict('records')
        serialized_data = serialize_data(data)
        
        # Generate session ID for this upload
        session_id = str(uuid.uuid4())
        active_sessions[session_id] = {
            'created_at': datetime.now(),
            'rows_count': len(serialized_data) if serialized_data else 0
        }
        
        # Store in Firebase with session tracking
        db_ref.child('excel_data').set(serialized_data)
        db_ref.child('column_mapping').set(column_mapping)
        db_ref.child('current_session').set({
            'session_id': session_id,
            'created_at': datetime.now().isoformat(),
            'rows_count': len(serialized_data) if serialized_data else 0
        })
        
        return {
            "message": "Data uploaded successfully",
            "rows_processed": len(serialized_data) if serialized_data else 0,
            "columns": original_columns,
            "sanitized_columns": sanitized_columns,
            "session_id": session_id
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing file: {str(e)}")

@app.get("/data")
async def get_data():
    """
    Retrieve all data from Firebase
    """
    if not db_ref:
        raise HTTPException(status_code=500, detail="Firebase database not available")
        
    try:
        # Clean up expired sessions first
        cleanup_expired_sessions()
        
        data = db_ref.child('excel_data').get()
        column_mapping = db_ref.child('column_mapping').get()
        
        if data is None:
            return {"data": [], "message": "No data found"}
        
        # Convert sanitized column names back to original names
        if column_mapping and isinstance(column_mapping, dict):
            # Create reverse mapping
            reverse_mapping = {v: k for k, v in column_mapping.items()}
            
            # Convert data back to original column names
            converted_data = []
            for row in data:
                converted_row = {}
                for sanitized_key, value in row.items():
                    original_key = reverse_mapping.get(sanitized_key, sanitized_key)
                    converted_row[original_key] = value
                converted_data.append(converted_row)
            
            return {"data": converted_data, "count": len(converted_data)}
        else:
            return {"data": data, "count": len(data)}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving data: {str(e)}")

@app.get("/data/{row_id}")
async def get_row(row_id: int):
    """
    Retrieve specific row by index
    """
    try:
        data = db_ref.child('excel_data').get()
        column_mapping = db_ref.child('column_mapping').get()
        
        if data is None or row_id >= len(data):
            raise HTTPException(status_code=404, detail="Row not found")
        
        row_data = data[row_id]
        
        # Convert sanitized column names back to original names
        if column_mapping and isinstance(column_mapping, dict):
            reverse_mapping = {v: k for k, v in column_mapping.items()}
            converted_row = {}
            for sanitized_key, value in row_data.items():
                original_key = reverse_mapping.get(sanitized_key, sanitized_key)
                converted_row[original_key] = value
            return {"data": converted_row}
        else:
            return {"data": row_data}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving row: {str(e)}")

@app.delete("/data")
async def clear_data():
    """
    Clear all data from Firebase
    """
    if not db_ref:
        raise HTTPException(status_code=500, detail="Firebase database not available")
        
    try:
        db_ref.child('excel_data').delete()
        db_ref.child('column_mapping').delete()
        db_ref.child('current_session').delete()
        
        # Clear active sessions
        active_sessions.clear()
        
        return {"message": "All data cleared successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error clearing data: {str(e)}")

@app.post("/session/clear")
async def clear_session_data():
    """
    Clear session data from Firebase
    """
    if not db_ref:
        raise HTTPException(status_code=500, detail="Firebase database not available")
        
    try:
        db_ref.child('excel_data').delete()
        db_ref.child('column_mapping').delete()
        db_ref.child('current_session').delete()
        
        # Clear active sessions
        active_sessions.clear()
        
        return {"message": "Session data cleared successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error clearing session data: {str(e)}")

@app.get("/sessions/active")
async def get_active_sessions():
    """
    Get active sessions
    """
    if not db_ref:
        raise HTTPException(status_code=500, detail="Firebase database not available")
        
    try:
        # Clean up expired sessions first
        cleanup_expired_sessions()
        
        return {
            "active_sessions": len(active_sessions),
            "sessions": [
                {
                    "session_id": session_id,
                    "created_at": session_data['created_at'].isoformat(),
                    "rows_count": session_data['rows_count']
                }
                for session_id, session_data in active_sessions.items()
            ]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving sessions: {str(e)}")

# For Vercel serverless deployment
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 