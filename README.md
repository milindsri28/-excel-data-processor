# Excel Data Processor

A simple web application to upload Excel files and view data in a browser. Built with Python (FastAPI) and React.

## What it does

1. **Upload Excel files** (.xlsx, .xls)
2. **Store data** in Firebase Realtime Database
3. **View data** in a nice table format
4. **Get basic statistics** about your data

## Live Demo

- **App**: https://creative-puffpuff-5a6348.netlify.app
- **API**: https://excel-data-processor-production.up.railway.app

## Tech Stack

- **Backend**: Python, FastAPI, Firebase
- **Frontend**: React, Bootstrap
- **Database**: Firebase Realtime Database
- **Hosting**: Railway (backend), Netlify (frontend)

## Quick Start

### Backend Setup
```bash
cd backend
pip install -r requirements.txt
# Add your Firebase credentials to .env file
uvicorn main:app --reload
```

### Frontend Setup
```bash
cd frontend
npm install
npm start
```

## API Endpoints

- `GET /` - Health check
- `POST /upload-excel` - Upload Excel file
- `GET /data` - Get all data
- `DELETE /data` - Clear data

## Features

- Upload Excel files
- View data in table
- Search and sort data
- Basic statistics
- Responsive design
- Auto-clear data on page close

## Sample Files

The app includes sample Excel files for testing:
- Employee data
- Sales data
- Inventory data
- Student data

Generate them with: `python create_sample_data.py`

## Deployment

### Backend (Railway)
1. Connect GitHub repo to Railway
2. Set environment variables:
   - `FIREBASE_DATABASE_URL`
   - `FIREBASE_SERVICE_ACCOUNT`
3. Deploy

### Frontend (Netlify)
1. Connect GitHub repo to Netlify
2. Set build settings:
   - Base directory: `frontend`
   - Build command: `npm run build`
   - Publish directory: `build`
3. Set environment variable: `REACT_APP_API_URL`
4. Deploy

## Project Structure

```
├── backend/          # FastAPI application
├── frontend/         # React application
├── create_sample_data.py  # Generate test files
└── README.md
```

---

Built with Python, React, and Firebase 