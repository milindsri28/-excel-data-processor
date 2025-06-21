# Backend - Excel Data Processor

This is a FastAPI backend application that processes Excel files and stores data in Firebase Realtime Database.

## Setup Instructions

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Firebase Setup
1. Go to [Firebase Console](https://console.firebase.google.com/)
2. Create a new project or select existing one
3. Go to Project Settings > Service Accounts
4. Generate a new private key (JSON file)
5. Download the JSON file and rename it to `firebase-service-account.json`
6. Place it in the `backend/` directory

### 3. Environment Configuration
1. Copy `env.example` to `.env`
2. Update the Firebase database URL in `.env`

### 4. Run the Application
```bash
cd backend
python main.py
```

The API will be available at `http://localhost:8000`

## API Endpoints

- `GET /` - Root endpoint
- `POST /upload-excel` - Upload and process Excel file
- `GET /data` - Retrieve all data
- `GET /data/{row_id}` - Retrieve specific row
- `DELETE /data` - Clear all data

## API Documentation

Once the server is running, visit:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc` 