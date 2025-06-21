import firebase_admin
from firebase_admin import credentials, db
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def test_firebase():
    try:
        print("Testing Firebase connection...")
        
        # Check if service account file exists
        if not os.path.exists("firebase-service-account.json"):
            print("❌ firebase-service-account.json not found!")
            return False
        
        # Check if .env file exists
        if not os.path.exists(".env"):
            print("❌ .env file not found!")
            return False
        
        # Get database URL
        database_url = os.getenv('FIREBASE_DATABASE_URL')
        if not database_url:
            print("❌ FIREBASE_DATABASE_URL not set in .env file!")
            return False
        
        print(f"✅ Database URL: {database_url}")
        
        # Initialize Firebase
        try:
            firebase_admin.get_app()
            print("✅ Firebase already initialized")
        except ValueError:
            cred = credentials.Certificate("firebase-service-account.json")
            firebase_admin.initialize_app(cred, {
                'databaseURL': database_url
            })
            print("✅ Firebase initialized successfully")
        
        # Test database connection
        db_ref = db.reference()
        test_data = {"test": "Hello Firebase!"}
        db_ref.child('test').set(test_data)
        print("✅ Successfully wrote to Firebase")
        
        # Read back the data
        result = db_ref.child('test').get()
        print(f"✅ Successfully read from Firebase: {result}")
        
        # Clean up test data
        db_ref.child('test').delete()
        print("✅ Successfully deleted test data")
        
        print("🎉 Firebase connection test passed!")
        return True
        
    except Exception as e:
        print(f"❌ Firebase test failed: {str(e)}")
        return False

if __name__ == "__main__":
    test_firebase() 