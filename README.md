# 📊 Excel Data Processor

Upload Excel files, view data in your browser, and analyze it instantly. Built with FastAPI, React, and Firebase. Deployed on Render.

## 🚀 Live Demo
- **Frontend**: [Your Netlify URL]
- **Backend**: [Your Render URL]

## ✨ Features
- 📁 Upload Excel files (.xlsx, .xls)
- 📊 View data in sortable, searchable table
- 📈 Get instant statistics and insights
- 🔒 Automatic data clearing for privacy
- 📱 Responsive design

## 🛠️ Quick Start

### Prerequisites
- Python 3.8+
- Node.js 14+
- Firebase project

### Local Development
```bash
# Clone repository
git clone https://github.com/milindsri28/excel-data-processor.git
cd excel-data-processor

# Backend
cd backend
pip install -r requirements.txt
cp env.example .env  # Add your Firebase credentials
python main.py

# Frontend (new terminal)
cd frontend
npm install
npm start
```

## 🚀 Deploy to Render

### Backend (Render)
1. Go to [render.com](https://render.com)
2. Create account with GitHub
3. Click "New Web Service"
4. Connect your repository
5. Configure:
   - **Root Directory**: `backend`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python main.py`
6. Add environment variables:
   ```
   FIREBASE_DATABASE_URL=https://your-project.firebaseio.com
   FIREBASE_SERVICE_ACCOUNT={"type": "service_account", ...}
   ```

### Frontend (Netlify)
1. Go to [netlify.com](https://netlify.com)
2. Click "New site from Git"
3. Connect your repository
4. Configure:
   - **Base directory**: `frontend`
   - **Build command**: `npm run build`
   - **Publish directory**: `build`
5. Add environment variable:
   ```
   REACT_APP_API_URL=https://your-app.onrender.com
   ```

## 📁 Sample Files
Try these sample Excel files:
- `sample_employee_data.xlsx` - Employee records
- `sample_sales_data.xlsx` - Sales data
- `sample_inventory_data.xlsx` - Inventory management
- `sample_student_data.xlsx` - Academic records
- `sample_customer_data.xlsx` - Customer data
- `sample_weather_data.xlsx` - Weather data
- `sample_simple_data.xlsx` - Simple test data

## 🔧 Generate Sample Files
```bash
python create_multiple_samples.py
```

## 🧪 Test Files
```bash
python test_sample_files.py
```

## 📊 API Endpoints
- `GET /` - Health check
- `POST /upload-excel` - Upload Excel file
- `GET /data` - Get all data
- `DELETE /data` - Clear all data
- `POST /session/clear` - Clear session data

## 🔒 Privacy
- Data is automatically cleared when you close the page
- No persistent storage
- Session-based data management

## 🐛 Troubleshooting
- Check Firebase credentials in `.env`
- Verify environment variables in Render/Netlify
- Check browser console for errors

---

**Built with ❤️ using FastAPI, React, and Firebase** 