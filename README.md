# 📊 Excel Data Processor

A full-stack web application for uploading Excel files, storing data in Firebase Realtime Database, and viewing it through a beautiful React interface with automatic data clearing when the website is closed.

## 🚀 Features

### Core Functionality
- **Excel File Upload**: Drag & drop or click to upload Excel files (.xlsx, .xls)
- **Firebase Storage**: Secure data storage in Firebase Realtime Database
- **Real-time Data Viewing**: Beautiful table interface with sorting, pagination, and search
- **Statistics Dashboard**: Data insights and analytics
- **Automatic Data Clearing**: Data is automatically cleared when the website is closed or refreshed
- **Session Management**: Track and manage user sessions

### Multiple Sample Data Files
The application comes with 7 different sample Excel files for comprehensive testing:

1. **Employee Data** (`sample_employee_data.xlsx`) - 50 records
   - Employee management with departments, salaries, performance scores
   - Fields: Employee_ID, Name, Department, Position, Salary, Age, Experience_Years, Location, Hire_Date, Performance_Score, Projects_Completed, Is_Active

2. **Sales Data** (`sample_sales_data.xlsx`) - 100 records
   - Sales and financial data with order tracking
   - Fields: Order_ID, Customer_Name, Product, Quantity, Unit_Price, Total_Amount, Order_Date, Payment_Method, Region, Sales_Rep, Status

3. **Inventory Data** (`sample_inventory_data.xlsx`) - 100 records
   - Inventory management with stock levels and pricing
   - Fields: Product_ID, Product_Name, Category, Brand, Stock_Quantity, Reorder_Level, Unit_Cost, Selling_Price, Supplier, Last_Updated, Location, Status

4. **Student Data** (`sample_student_data.xlsx`) - 100 records
   - Academic data with grades and performance metrics
   - Fields: Student_ID, Name, Age, Grade, Subject, Test_Score, Assignment_Score, Participation, Attendance, Final_Grade, Teacher, Parent_Contact, Enrollment_Date

5. **Customer Data** (`sample_customer_data.xlsx`) - 100 records
   - Customer relationship management data
   - Fields: Customer_ID, First_Name, Last_Name, Email, Phone, Age, Gender, City, State, Zip_Code, Membership_Level, Total_Purchases, Last_Purchase_Date, Is_Active

6. **Weather Data** (`sample_weather_data.xlsx`) - 100 records
   - Time series weather data with multiple metrics
   - Fields: Date, Temperature_C, Temperature_F, Humidity, Pressure, Wind_Speed, Wind_Direction, Precipitation, UV_Index, Visibility, Weather_Condition, Location

7. **Simple Data** (`sample_simple_data.xlsx`) - 20 records
   - Basic test data for simple scenarios
   - Fields: ID, Name, Value, Category, Active

## 🏗️ Architecture

### Backend (FastAPI)
- **Framework**: FastAPI with Python
- **Database**: Firebase Realtime Database
- **File Processing**: Pandas for Excel file handling
- **Session Management**: UUID-based session tracking
- **Automatic Cleanup**: 24-hour session expiry

### Frontend (React)
- **Framework**: React with hooks
- **UI Library**: Bootstrap for responsive design
- **File Upload**: React Dropzone for drag & drop
- **Data Table**: Custom component with sorting, pagination, search
- **Statistics**: Real-time data analytics
- **Auto-clear**: Automatic data clearing on page close/refresh

## 📋 Prerequisites

- Python 3.8+
- Node.js 14+
- Firebase project with Realtime Database
- Firebase service account key

## 🛠️ Installation

### 1. Clone the Repository
```bash
git clone <repository-url>
cd kustodian
```

### 2. Backend Setup
```bash
cd backend

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp env.example .env
# Edit .env with your Firebase credentials

# Place Firebase service account JSON in backend folder
# Name it: firebase-service-account.json
```

### 3. Frontend Setup
```bash
cd frontend

# Install dependencies
npm install

# Set up environment variables (optional for local development)
# Create .env file with REACT_APP_API_URL=http://localhost:8000
```

### 4. Generate Sample Data
```bash
# From the root directory
python create_multiple_samples.py
```

## ⚙️ Configuration

### Environment Variables (Backend)
Create a `.env` file in the `backend` directory:

```env
FIREBASE_DATABASE_URL=https://your-project-id.firebaseio.com
FIREBASE_SERVICE_ACCOUNT={"type": "service_account", ...}
```

### Firebase Setup
1. Create a Firebase project
2. Enable Realtime Database
3. Set database rules to allow read/write
4. Generate service account key
5. Download and place in `backend/firebase-service-account.json`

## 🚀 Running the Application

### Development Mode

#### Backend
```bash
cd backend
python main.py
```
Backend will run on: http://localhost:8000

#### Frontend
```bash
cd frontend
npm start
```
Frontend will run on: http://localhost:3000

### Production Mode

#### Backend (Railway/Render)
```bash
# Deploy to Railway or Render
# Set environment variables in deployment platform
```

#### Frontend (Netlify/Vercel)
```bash
# Deploy to Netlify or Vercel
# Update API URL in environment variables
```

## 📊 API Endpoints

### Core Endpoints
- `GET /` - API health check
- `POST /upload-excel` - Upload Excel file
- `GET /data` - Retrieve all data
- `GET /data/{row_id}` - Retrieve specific row
- `DELETE /data` - Clear all data

### Session Management
- `POST /session/clear` - Clear session data (auto-called on page close)
- `GET /sessions/active` - Get active sessions info

## 🎯 Usage

### 1. Upload Excel File
- Drag and drop an Excel file onto the upload area
- Or click to browse and select a file
- Supported formats: .xlsx, .xls

### 2. View Data
- Data appears in a responsive table
- Sort by clicking column headers
- Search using the search box
- Navigate with pagination controls

### 3. View Statistics
- See data insights and analytics
- View row count, column count, and data types
- Monitor data distribution

### 4. Automatic Data Clearing
- Data is automatically cleared when you close the browser tab
- Data is cleared when you refresh the page
- Manual clear button available for immediate clearing

## 🔧 Testing

### Sample Files
Use the provided sample files to test different data types:

```bash
# Generate all sample files
python create_multiple_samples.py

# Test with different data types:
# - sample_employee_data.xlsx (HR data)
# - sample_sales_data.xlsx (Financial data)
# - sample_inventory_data.xlsx (Inventory data)
# - sample_student_data.xlsx (Academic data)
# - sample_customer_data.xlsx (CRM data)
# - sample_weather_data.xlsx (Time series data)
# - sample_simple_data.xlsx (Simple test data)
```

### Manual Testing
1. Start backend and frontend
2. Upload different sample files
3. Test sorting, searching, and pagination
4. Test automatic data clearing by closing/refreshing
5. Test manual data clearing

## 🚀 Deployment

### Backend Deployment (Railway)
1. Connect GitHub repository to Railway
2. Set environment variables in Railway dashboard
3. Deploy automatically on push

### Frontend Deployment (Netlify)
1. Connect GitHub repository to Netlify
2. Set build command: `npm run build`
3. Set publish directory: `build`
4. Add environment variable: `REACT_APP_API_URL`

### Environment Variables for Production
```env
# Backend (Railway)
FIREBASE_DATABASE_URL=https://your-project-id.firebaseio.com
FIREBASE_SERVICE_ACCOUNT={"type": "service_account", ...}

# Frontend (Netlify)
REACT_APP_API_URL=https://your-backend-url.railway.app
```

## 🔒 Security Features

- **CORS Protection**: Configured for specific origins
- **File Type Validation**: Only Excel files allowed
- **Column Name Sanitization**: Firebase-compatible column names
- **Session Management**: Automatic cleanup of expired sessions
- **Data Privacy**: Automatic data clearing on page close

## 🐛 Troubleshooting

### Common Issues

1. **Firebase Connection Error**
   - Check Firebase database URL
   - Verify service account JSON file
   - Ensure database rules allow read/write

2. **File Upload Issues**
   - Ensure file is Excel format (.xlsx, .xls)
   - Check file size (max 10MB recommended)
   - Verify backend is running

3. **Data Not Displaying**
   - Check browser console for errors
   - Verify API endpoints are accessible
   - Check Firebase data in console

4. **CORS Errors**
   - Update CORS origins in backend
   - Check frontend API URL configuration

### Debug Mode
```bash
# Backend with debug logging
cd backend
python main.py --debug

# Frontend with detailed logging
cd frontend
REACT_APP_DEBUG=true npm start
```

## 📈 Performance

- **File Processing**: Optimized with pandas
- **Data Serialization**: Efficient JSON conversion
- **Session Cleanup**: Automatic 24-hour expiry
- **Memory Management**: Temporary file cleanup
- **Caching**: Firebase real-time caching

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License.

## 🆘 Support

For support and questions:
- Check the troubleshooting section
- Review Firebase documentation
- Open an issue on GitHub

---

**🎉 Happy Data Processing!** 