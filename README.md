# 📊 Excel Data Processor - Full Stack Application

A complete full-stack web application for uploading Excel files, processing data, and viewing it in a beautiful interface with Firebase Realtime Database integration.

## 🎯 Project Overview

This application addresses the following requirements:

### ✅ Data Ingestion
- Extract data from Excel sheets (.xlsx, .xls)
- Store extracted data in Firebase Realtime Database
- Handle various data types and formats

### ✅ API Development
- FastAPI backend with multiple endpoints
- RESTful API for data operations
- CORS configuration for frontend integration

### ✅ Frontend Application
- React-based web interface
- Beautiful Bootstrap UI design
- Real-time data viewing and interaction

### ✅ Documentation
- Comprehensive setup and deployment guides
- API documentation
- Screenshots and usage examples

## 🚀 Live Demo

- **Frontend**: [https://creative-puffpuff-5a6348.netlify.app](https://creative-puffpuff-5a6348.netlify.app)
- **Backend API**: [https://excel-data-processor-production.up.railway.app](https://excel-data-processor-production.up.railway.app)

## 🛠️ Tech Stack

### Backend
- **Python 3.11** - Core programming language
- **FastAPI** - Modern, fast web framework
- **Firebase Admin SDK** - Database integration
- **Pandas** - Excel file processing
- **Uvicorn** - ASGI server

### Frontend
- **React 18** - User interface framework
- **Bootstrap 5** - CSS framework for styling
- **Axios** - HTTP client for API calls
- **React Table** - Data table with sorting and pagination

### Database & Deployment
- **Firebase Realtime Database** - NoSQL database
- **Railway** - Backend hosting platform
- **Netlify** - Frontend hosting platform
- **GitHub** - Version control

## 📁 Project Structure

```
kustodian/
├── backend/
│   ├── main.py                 # FastAPI application
│   ├── requirements.txt        # Python dependencies
│   ├── firebase-service-account.json  # Firebase credentials
│   ├── railway.toml           # Railway deployment config
│   ├── runtime.txt            # Python version
│   └── DEPLOYMENT_GUIDE.md    # Backend deployment guide
├── frontend/
│   ├── src/
│   │   ├── App.js             # Main React component
│   │   ├── components/
│   │   │   ├── DataTable.js   # Data display component
│   │   │   ├── FileUpload.js  # File upload component
│   │   │   └── Statistics.js  # Statistics component
│   │   └── index.js           # React entry point
│   ├── package.json           # Node.js dependencies
│   ├── netlify.toml          # Netlify deployment config
│   └── NETLIFY_DEPLOYMENT.md # Frontend deployment guide
├── create_sample_data.py      # Sample Excel file generator
├── requirements.txt           # Root dependencies
└── README.md                 # This file
```

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- Node.js 16+
- Firebase project
- Railway account
- Netlify account

### Local Development

#### Backend Setup
```bash
# Clone the repository
git clone https://github.com/your-username/excel-data-processor.git
cd excel-data-processor

# Setup backend
cd backend
pip install -r requirements.txt

# Set environment variables
cp env.example .env
# Edit .env with your Firebase credentials

# Run backend
uvicorn main:app --reload
```

#### Frontend Setup
```bash
# Setup frontend
cd frontend
npm install

# Set environment variable
echo "REACT_APP_API_URL=http://localhost:8000" > .env

# Run frontend
npm start
```

## 📊 API Endpoints

### Base URL
```
https://excel-data-processor-production.up.railway.app
```

### Available Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | API health check |
| `GET` | `/debug` | Debug information |
| `POST` | `/upload-excel` | Upload Excel file |
| `GET` | `/data` | Retrieve all data |
| `GET` | `/data/{row_id}` | Get specific row |
| `DELETE` | `/data` | Clear all data |
| `POST` | `/session/clear` | Clear session data |
| `GET` | `/sessions/active` | Get active sessions |

### Example API Usage

#### Upload Excel File
```bash
curl -X POST "https://excel-data-processor-production.up.railway.app/upload-excel" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@sample_data.xlsx"
```

#### Get Data
```bash
curl "https://excel-data-processor-production.up.railway.app/data"
```

## 🎨 Features

### Data Processing
- ✅ **Excel File Support**: .xlsx and .xls formats
- ✅ **Automatic Column Sanitization**: Firebase-compatible column names
- ✅ **Data Type Handling**: Numbers, dates, text, booleans
- ✅ **Error Handling**: Robust error management

### User Interface
- ✅ **File Upload**: Drag & drop or click to upload
- ✅ **Data Table**: Sortable, searchable, paginated
- ✅ **Statistics**: Data insights and summaries
- ✅ **Responsive Design**: Works on all devices
- ✅ **Real-time Updates**: Instant data refresh

### Data Management
- ✅ **Session Management**: Automatic data clearing
- ✅ **Data Persistence**: Firebase Realtime Database
- ✅ **Column Mapping**: Preserve original column names
- ✅ **Data Export**: View and interact with data

## 📸 Screenshots

### Main Interface
![Main Interface](https://via.placeholder.com/800x400/007bff/ffffff?text=Excel+Data+Processor+Interface)

### File Upload
![File Upload](https://via.placeholder.com/800x400/28a745/ffffff?text=File+Upload+Section)

### Data Table
![Data Table](https://via.placeholder.com/800x400/ffc107/000000?text=Data+Table+View)

### Statistics
![Statistics](https://via.placeholder.com/800x400/dc3545/ffffff?text=Statistics+Dashboard)

## 🔧 Configuration

### Environment Variables

#### Backend (Railway)
```env
FIREBASE_DATABASE_URL=https://your-project.firebaseio.com
FIREBASE_SERVICE_ACCOUNT={"type":"service_account",...}
```

#### Frontend (Netlify)
```env
REACT_APP_API_URL=https://your-backend-url.railway.app
```

### Firebase Setup
1. Create Firebase project
2. Enable Realtime Database
3. Generate service account key
4. Set database rules for read/write access

## 🚀 Deployment

### Backend Deployment (Railway)
1. Connect GitHub repository to Railway
2. Set environment variables
3. Deploy automatically on push

### Frontend Deployment (Netlify)
1. Connect GitHub repository to Netlify
2. Set build settings:
   - Base directory: `frontend`
   - Build command: `npm run build`
   - Publish directory: `build`
3. Set environment variables
4. Deploy automatically on push

## 📋 Sample Data

The application includes sample Excel files for testing:
- Employee data
- Sales data
- Inventory data
- Student data
- Customer data
- Weather data
- Simple test data

Generate sample files:
```bash
python create_sample_data.py
```

## 🔒 Security Features

- **CORS Configuration**: Secure cross-origin requests
- **Input Validation**: File type and size validation
- **Error Handling**: Graceful error management
- **Session Management**: Automatic data cleanup
- **Environment Variables**: Secure credential management

## 🧪 Testing

### Backend Testing
```bash
cd backend
python -m pytest
```

### Frontend Testing
```bash
cd frontend
npm test
```

### API Testing
```bash
# Test all endpoints
curl https://excel-data-processor-production.up.railway.app/
curl https://excel-data-processor-production.up.railway.app/data
curl https://excel-data-processor-production.up.railway.app/debug
```

## 📈 Performance

- **FastAPI**: High-performance async framework
- **Firebase**: Real-time database with low latency
- **React**: Optimized rendering and state management
- **CDN**: Global content delivery via Netlify

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- FastAPI for the excellent web framework
- Firebase for the real-time database
- React and Bootstrap for the UI components
- Railway and Netlify for hosting services

## 📞 Support

For support and questions:
- Create an issue on GitHub
- Check the deployment guides in the respective folders
- Review the API documentation above

---

**Built with ❤️ using Python, React, and Firebase** 