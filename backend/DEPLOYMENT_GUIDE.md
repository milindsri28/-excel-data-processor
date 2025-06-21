# Deployment Guide

## Firebase Configuration for Deployment

When deploying to cloud platforms (Railway, Render, etc.), you need to set up Firebase environment variables instead of using the local service account file.

### Required Environment Variables

1. **FIREBASE_DATABASE_URL**: Your Firebase Realtime Database URL
   - Format: `https://your-project-id.firebaseio.com`
   - Get this from your Firebase Console → Realtime Database

2. **FIREBASE_SERVICE_ACCOUNT**: Your Firebase service account JSON as a string
   - This is the entire content of your `firebase-service-account.json` file
   - Must be a valid JSON string

### How to Get Firebase Service Account

1. Go to [Firebase Console](https://console.firebase.google.com/)
2. Select your project
3. Go to Project Settings (gear icon)
4. Go to Service Accounts tab
5. Click "Generate new private key"
6. Download the JSON file
7. Copy the entire content of the JSON file

### Setting Environment Variables

#### For Railway:
1. Go to your Railway project dashboard
2. Click on your service
3. Go to Variables tab
4. Add the following variables:
   - `FIREBASE_DATABASE_URL`: Your database URL
   - `FIREBASE_SERVICE_ACCOUNT`: The entire JSON content (as a single line)

#### For Render:
1. Go to your Render dashboard
2. Select your service
3. Go to Environment tab
4. Add the following variables:
   - `FIREBASE_DATABASE_URL`: Your database URL
   - `FIREBASE_SERVICE_ACCOUNT`: The entire JSON content (as a single line)

#### For Other Platforms:
Set the same environment variables in your platform's configuration.

### Example Environment Variables

```
FIREBASE_DATABASE_URL=https://my-project-12345.firebaseio.com
FIREBASE_SERVICE_ACCOUNT={"type":"service_account","project_id":"my-project-12345","private_key_id":"abc123","private_key":"-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC...","client_email":"firebase-adminsdk-abc123@my-project-12345.iam.gserviceaccount.com","client_id":"123456789","auth_uri":"https://accounts.google.com/o/oauth2/auth","token_uri":"https://oauth2.googleapis.com/token","auth_provider_x509_cert_url":"https://www.googleapis.com/oauth2/v1/certs","client_x509_cert_url":"https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-abc123%40my-project-12345.iam.gserviceaccount.com"}
```

### Important Notes

- The `FIREBASE_SERVICE_ACCOUNT` must be the entire JSON content as a single line
- Make sure there are no extra spaces or line breaks in the JSON string
- The JSON must be valid and complete
- Never commit your actual service account file to version control
- The local `firebase-service-account.json` file is only for development

### Troubleshooting

If you get errors about missing Firebase configuration:
1. Check that both environment variables are set
2. Verify the JSON in `FIREBASE_SERVICE_ACCOUNT` is valid
3. Ensure the `FIREBASE_DATABASE_URL` is correct
4. Make sure your Firebase project has Realtime Database enabled 