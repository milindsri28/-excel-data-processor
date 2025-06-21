# 🚀 Deployment Guide - Excel Data Processor

This guide covers deploying the Excel Data Processor with multiple sample files and automatic data clearing functionality.

## 📋 Prerequisites

- GitHub account
- Firebase project with Realtime Database
- Railway account (for backend)
- Netlify/Vercel account (for frontend)

## 🔧 Pre-Deployment Setup

### 1. Firebase Configuration

1. **Create Firebase Project**
   ```bash
   # Go to Firebase Console
   # Create new project
   # Enable Realtime Database
   ```

2. **Set Database Rules**
   ```json
   {
     "rules": {
       ".read": true,
       ".write": true
     }
   }
   ```

3. **Generate Service Account Key**
   - Go to Project Settings > Service Accounts
   - Click "Generate new private key"
   - Download JSON file
   - Save as `firebase-service-account.json` in backend folder

### 2. Environment Variables

#### Backend (.env file)
```env
FIREBASE_DATABASE_URL=https://your-project-id.firebaseio.com
FIREBASE_SERVICE_ACCOUNT={"type": "service_account", ...}
```

#### Frontend (.env file)
```env
REACT_APP_API_URL=http://localhost:8000
```

## 🚀 Backend Deployment (Railway)

### 1. Connect to Railway

1. **Sign up/Login to Railway**
   - Go to [railway.app](https://railway.app)
   - Sign up with GitHub

2. **Create New Project**
   ```bash
   # Click "New Project"
   # Select "Deploy from GitHub repo"
   # Choose your repository
   ```

3. **Configure Project**
   ```bash
   # Set root directory to: backend
   # Set build command to: pip install -r requirements.txt
   # Set start command to: python main.py
   ```

### 2. Environment Variables (Railway)

Add these environment variables in Railway dashboard:

```env
FIREBASE_DATABASE_URL=https://your-project-id.firebaseio.com
FIREBASE_SERVICE_ACCOUNT={"type": "service_account", "project_id": "your-project", ...}
```

**Important**: For `FIREBASE_SERVICE_ACCOUNT`, copy the entire JSON content from your service account file.

### 3. Deploy

```bash
# Railway will automatically deploy when you push to GitHub
git add .
git commit -m "Add backend deployment configuration"
git push origin main
```

### 4. Get Backend URL

After deployment, Railway will provide a URL like:
```
https://your-app-name.railway.app
```

## 🌐 Frontend Deployment (Netlify)

### 1. Connect to Netlify

1. **Sign up/Login to Netlify**
   - Go to [netlify.com](https://netlify.com)
   - Sign up with GitHub

2. **Create New Site**
   ```bash
   # Click "New site from Git"
   # Choose GitHub
   # Select your repository
   ```

### 2. Build Settings

Configure build settings in Netlify:

```bash
# Build command
npm run build

# Publish directory
build

# Base directory
frontend
```

### 3. Environment Variables (Netlify)

Add environment variable in Netlify dashboard:

```env
REACT_APP_API_URL=https://your-backend-url.railway.app
```

### 4. Deploy

```bash
# Netlify will automatically deploy when you push to GitHub
git add .
git commit -m "Add frontend deployment configuration"
git push origin main
```

## 🔄 Alternative Deployment Options

### Backend Alternatives

#### Render
1. **Sign up at [render.com](https://render.com)**
2. **Create Web Service**
   ```bash
   # Connect GitHub repo
   # Set root directory: backend
   # Build command: pip install -r requirements.txt
   # Start command: python main.py
   ```

#### Heroku
1. **Sign up at [heroku.com](https://heroku.com)**
2. **Create app and connect GitHub**
3. **Set buildpacks**: `heroku/python`
4. **Add environment variables**

### Frontend Alternatives

#### Vercel
1. **Sign up at [vercel.com](https://vercel.com)**
2. **Import GitHub repository**
3. **Set framework preset**: Create React App
4. **Add environment variables**

## 🧪 Testing Deployment

### 1. Test Backend

```bash
# Test API health
curl https://your-backend-url.railway.app/

# Expected response:
# {"message": "Excel Data Processor API", "version": "1.0.0"}
```

### 2. Test Frontend

1. **Open your Netlify URL**
2. **Upload sample files**:
   - `sample_employee_data.xlsx`
   - `sample_sales_data.xlsx`
   - `sample_inventory_data.xlsx`
   - `sample_student_data.xlsx`
   - `sample_customer_data.xlsx`
   - `sample_weather_data.xlsx`
   - `sample_simple_data.xlsx`

### 3. Test Features

- ✅ **File Upload**: Drag & drop Excel files
- ✅ **Data Display**: View data in table format
- ✅ **Sorting**: Click column headers to sort
- ✅ **Search**: Use search box to filter data
- ✅ **Pagination**: Navigate through large datasets
- ✅ **Statistics**: View data insights
- ✅ **Auto-clear**: Close browser tab to clear data
- ✅ **Manual Clear**: Use clear button

## 🔒 Security Considerations

### 1. CORS Configuration

Update CORS origins in `backend/main.py`:

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "https://your-frontend-url.netlify.app",
        "https://your-frontend-url.vercel.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### 2. Firebase Security Rules

For production, consider stricter rules:

```json
{
  "rules": {
    "excel_data": {
      ".read": "auth != null",
      ".write": "auth != null"
    },
    "sessions": {
      ".read": "auth != null",
      ".write": "auth != null"
    }
  }
}
```

### 3. Environment Variables

- Never commit `.env` files to Git
- Use deployment platform's environment variable system
- Rotate service account keys regularly

## 🐛 Troubleshooting

### Common Issues

#### 1. Backend Deployment Issues

**Problem**: Railway deployment fails
```bash
# Solution: Check requirements.txt
# Ensure all dependencies are listed
# Check Python version compatibility
```

**Problem**: Firebase connection error
```bash
# Solution: Verify environment variables
# Check service account JSON format
# Ensure database URL is correct
```

#### 2. Frontend Deployment Issues

**Problem**: Build fails
```bash
# Solution: Check package.json
# Ensure all dependencies are installed
# Check for syntax errors
```

**Problem**: API calls fail
```bash
# Solution: Verify REACT_APP_API_URL
# Check CORS configuration
# Test API endpoints directly
```

#### 3. Data Issues

**Problem**: Data not clearing automatically
```bash
# Solution: Check browser console for errors
# Verify session/clear endpoint is working
# Test manual clear functionality
```

**Problem**: File upload fails
```bash
# Solution: Check file format (.xlsx, .xls)
# Verify file size (max 10MB)
# Check backend logs for errors
```

### Debug Commands

```bash
# Test backend locally
cd backend
python main.py

# Test frontend locally
cd frontend
npm start

# Test sample files
python test_sample_files.py

# Generate new sample files
python create_multiple_samples.py
```

## 📊 Monitoring

### 1. Railway Monitoring

- Check deployment logs
- Monitor resource usage
- Set up alerts for failures

### 2. Netlify Monitoring

- Check build logs
- Monitor site performance
- Set up form submissions (if needed)

### 3. Firebase Monitoring

- Monitor database usage
- Check authentication logs
- Set up alerts for quota limits

## 🔄 Continuous Deployment

### 1. Automatic Deployment

Both Railway and Netlify support automatic deployment:

```bash
# Push to main branch triggers deployment
git push origin main
```

### 2. Branch Deployments

Set up preview deployments for feature branches:

```bash
# Create feature branch
git checkout -b feature/new-feature

# Push to trigger preview deployment
git push origin feature/new-feature
```

## 📈 Performance Optimization

### 1. Backend Optimization

- Enable caching for static files
- Optimize database queries
- Use connection pooling

### 2. Frontend Optimization

- Enable code splitting
- Optimize bundle size
- Use CDN for static assets

### 3. Database Optimization

- Index frequently queried fields
- Optimize data structure
- Monitor query performance

## 🎯 Next Steps

After successful deployment:

1. **Test all sample files**
2. **Verify automatic data clearing**
3. **Monitor performance**
4. **Set up monitoring alerts**
5. **Document any custom configurations**
6. **Share the application with users**

## 📞 Support

For deployment issues:

1. Check the troubleshooting section
2. Review platform documentation
3. Check GitHub issues
4. Contact platform support

---

**�� Happy Deploying!** 