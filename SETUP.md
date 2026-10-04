# Setup Guide for Kaushal Setu

## Prerequisites

1. **Python 3.9+** - Check with `python --version`
2. **Node.js 18+** - Check with `node --version`
3. **Firebase Account** - Create a project at https://console.firebase.google.com
4. **Google Gemini API Key** - Get from https://ai.google.dev

## Step-by-Step Setup

### 1. Firebase Setup

1. Go to https://console.firebase.google.com
2. Create a new project (or use existing)
3. Enable Firestore Database:
   - Go to Build → Firestore Database
   - Click "Create Database"
   - Choose "Start in test mode"
   - Select your region

4. Get Web Config:
   - Go to Project Settings → General
   - Scroll to "Your apps" section
   - Click "Web" icon (</>)
   - Copy the firebaseConfig object

5. Get Service Account Key:
   - Go to Project Settings → Service Accounts
   - Click "Generate new private key"
   - Save the JSON file as `serviceAccountKey.json` in the `backend/` folder

### 2. Get Gemini API Key

1. Visit https://ai.google.dev
2. Click "Get API Key in Google AI Studio"
3. Create a new API key
4. Copy the key

### 3. Backend Configuration

```bash
cd backend
pip install -r requirements.txt
```

Create `.env` file:
```env
GEMINI_API_KEY=your_gemini_api_key_here
FIREBASE_CREDENTIALS=serviceAccountKey.json
```

Place your `serviceAccountKey.json` in the `backend/` folder.

### 4. Frontend Configuration

```bash
cd frontend
npm install
```

Edit `src/services/firebase.js` and replace the config:

```javascript
const firebaseConfig = {
  apiKey: "YOUR_API_KEY",
  authDomain: "YOUR_PROJECT.firebaseapp.com",
  projectId: "YOUR_PROJECT_ID",
  storageBucket: "YOUR_PROJECT.appspot.com",
  messagingSenderId: "YOUR_SENDER_ID",
  appId: "YOUR_APP_ID"
};
```

### 5. Run the Application

**Terminal 1 - Backend:**
```bash
cd backend
python app.py
```
Backend runs on http://localhost:5000

**Terminal 2 - Frontend:**
```bash
cd frontend
npm run dev
```
Frontend runs on http://localhost:3000

### 6. Test the Application

1. Open http://localhost:3000 in your browser
2. Fill out the Self-Declaration form with sample data
3. Submit and view AI-suggested NSQF level
4. Go to Competency Checklist and score the candidate
5. View results in Assessor Dashboard

## Troubleshooting

**Backend won't start:**
- Check Python version: `python --version`
- Verify all dependencies installed
- Check `.env` file exists with correct keys
- Verify `serviceAccountKey.json` is in backend folder

**Frontend won't start:**
- Check Node version: `node --version`
- Delete `node_modules` and run `npm install` again
- Verify Firebase config in `firebase.js`

**AI not working:**
- Verify Gemini API key is correct
- Check backend console for error messages
- Ensure you have internet connection

**Firestore errors:**
- Check Firebase service account key is valid
- Verify Firestore is enabled in Firebase Console
- Check Firestore rules allow read/write

## Demo Day Checklist

- [ ] Backend running on localhost:5000
- [ ] Frontend running on localhost:3000
- [ ] Firebase Firestore enabled
- [ ] Gemini API key working
- [ ] Test with 2 sample candidates
- [ ] Assessor dashboard showing results
- [ ] Prepared to explain offline functionality
- [ ] Ready to discuss future scope

