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
from datetime import datetime
import re

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI(title="Excel Data Processor", version="1.0.0")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",  # Local development
        "https://*.railway.app",  # Railway frontend
        "https://*.netlify.app",  # Netlify frontend
        "https://*.vercel.app",   # Vercel frontend
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
    if firebase_service_account:
        # For Railway deployment - service account from environment variable
        import json
        service_account_info = json.loads(firebase_service_account)
        cred = credentials.Certificate(service_account_info)
    else:
        # For local development - service account from file
        cred = credentials.Certificate("firebase-service-account.json")
    
    firebase_admin.initialize_app(cred, {
        'databaseURL': os.getenv('FIREBASE_DATABASE_URL', 'https://your-project-id.firebaseio.com')
    })

# Get database reference
db_ref = db.reference()

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

@app.get("/")
async def root():
    """Root endpoint"""
    return {"message": "Excel Data Processor API", "version": "1.0.0"}

@app.post("/upload-excel")
async def upload_excel(file: UploadFile = File(...)):
    """
    Upload and process Excel file
    """
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
        
        # Store in Firebase
        db_ref.child('excel_data').set(serialized_data)
        db_ref.child('column_mapping').set(column_mapping)
        
        return {
            "message": "Data uploaded successfully",
            "rows_processed": len(serialized_data) if serialized_data else 0,
            "columns": original_columns,
            "sanitized_columns": sanitized_columns
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing file: {str(e)}")

@app.get("/data")
async def get_data():
    """
    Retrieve all data from Firebase
    """
    try:
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
    try:
        db_ref.child('excel_data').delete()
        db_ref.child('column_mapping').delete()
        return {"message": "All data cleared successfully"}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error clearing data: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 