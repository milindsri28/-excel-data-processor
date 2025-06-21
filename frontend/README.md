# Frontend - Excel Data Viewer

A modern React application for viewing and analyzing Excel data with a beautiful, responsive interface.

## Features

- 📁 Drag & drop Excel file upload
- 📊 Interactive data table with sorting and pagination
- 🔍 Real-time search functionality
- 📈 Data statistics and insights
- 🎨 Modern, responsive design
- 📱 Mobile-friendly interface

## Setup Instructions

### 1. Install Dependencies
```bash
cd frontend
npm install
```

### 2. Start Development Server
```bash
npm start
```

The application will be available at `http://localhost:3000`

### 3. Build for Production
```bash
npm run build
```

## Usage

1. **Upload Excel File**: Drag and drop an Excel file (.xlsx or .xls) onto the upload area
2. **View Data**: The uploaded data will be displayed in an interactive table
3. **Search & Filter**: Use the search bar to filter data
4. **Sort Data**: Click on column headers to sort data
5. **View Statistics**: See data insights and statistics
6. **Clear Data**: Use the "Clear All Data" button to remove all data

## Technologies Used

- React 18
- Bootstrap 5
- React Table
- React Dropzone
- Axios
- Chart.js (for future enhancements)

## API Integration

The frontend connects to the FastAPI backend running on `http://localhost:8000`. Make sure the backend is running before using the frontend. 