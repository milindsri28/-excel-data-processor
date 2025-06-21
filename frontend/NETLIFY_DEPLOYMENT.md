# Netlify Deployment Guide

## Prerequisites
- Your Railway backend is deployed and running
- You have your Railway URL (e.g., `https://your-app-name.railway.app`)

## Step 1: Get Your Railway URL
1. Go to your Railway dashboard
2. Click on your backend service
3. Go to the "Settings" tab
4. Copy your application URL (it should look like `https://your-app-name.railway.app`)

## Step 2: Update Netlify Configuration
1. Open `netlify.toml` in the frontend folder
2. Replace `https://your-railway-app-name.railway.app` with your actual Railway URL
3. Save the file

## Step 3: Deploy to Netlify

### Option A: Deploy via Netlify UI (Recommended)
1. Go to [Netlify](https://netlify.com) and sign up/login
2. Click "New site from Git"
3. Connect your GitHub account
4. Select your repository (`-excel-data-processor`)
5. Set build settings:
   - **Base directory**: `frontend`
   - **Build command**: `npm run build`
   - **Publish directory**: `build`
6. Click "Deploy site"

### Option B: Deploy via Netlify CLI
1. Install Netlify CLI: `npm install -g netlify-cli`
2. Navigate to frontend directory: `cd frontend`
3. Run: `netlify deploy --prod`

## Step 4: Set Environment Variables in Netlify
1. Go to your Netlify site dashboard
2. Go to "Site settings" → "Environment variables"
3. Add variable:
   - **Key**: `REACT_APP_API_URL`
   - **Value**: Your Railway URL (e.g., `https://your-app-name.railway.app`)
4. Save and redeploy

## Step 5: Test Your Application
1. Visit your Netlify URL
2. Try uploading an Excel file
3. Verify that data is displayed correctly
4. Test the clear data functionality

## Troubleshooting

### CORS Issues
If you see CORS errors, make sure your Railway backend has the correct CORS configuration in `main.py`.

### API Connection Issues
- Verify your Railway URL is correct
- Check that your Railway backend is running
- Ensure environment variables are set correctly

### Build Errors
- Make sure all dependencies are in `package.json`
- Check that the build command is correct
- Verify the base directory is set to `frontend` 