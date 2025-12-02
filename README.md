# Sacred Smoke - Python for Android

This repository contains Python 3.14.0 compiled for Android (aarch64-linux-android architecture).

## Contents

- Pre-compiled Python libraries
- OpenSSL headers and libraries
- Android build scripts
- Test suite for Android

## Firebase Hosting

This repository is configured to automatically deploy to Firebase Hosting when changes are pushed to the `main` branch.

### Setup Instructions

To enable automatic deployment, you need to configure the following GitHub secrets in your repository settings:

1. **FIREBASE_SERVICE_ACCOUNT**: A Firebase service account JSON key with hosting permissions
   - Go to [Firebase Console](https://console.firebase.google.com/)
   - Select your project
   - Go to Project Settings > Service Accounts
   - Generate a new private key
   - Copy the entire JSON content and add it as a repository secret

2. **FIREBASE_PROJECT_ID**: Your Firebase project ID
   - Find this in your Firebase Console project settings

### Manual Deployment

You can also trigger a deployment manually using the "Actions" tab in GitHub and running the "Deploy to Firebase Hosting" workflow.

## Local Development

To test the site locally, you can use any static file server. For example:

```bash
python3 -m http.server 8000
```

Then visit `http://localhost:8000` in your browser.

## More Information

For more information on using Python on Android, visit the [official Python documentation](https://docs.python.org/3/using/android.html).
