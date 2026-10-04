# TODO Before Hackathon Monday

## ✅ Already Complete
- [x] Full backend with Flask, Firebase, Gemini AI
- [x] Complete frontend with React + Vite
- [x] All 3 screens: Declaration, Checklist, Dashboard
- [x] NSQF Electrician competency data
- [x] Offline persistence setup
- [x] Setup documentation

## 🔧 Required Configuration (Sunday - 30 mins)

### 1. Firebase Setup
- [ ] Create Firebase project at https://console.firebase.google.com
- [ ] Enable Firestore Database (test mode is fine)
- [ ] Download service account key → save as `backend/serviceAccountKey.json`
- [ ] Copy web config → paste into `frontend/src/services/firebase.js`

### 2. Gemini API Setup
- [ ] Get API key from https://ai.google.dev
- [ ] Create `backend/.env` file
- [ ] Add: `GEMINI_API_KEY=your_key_here`
- [ ] Add: `FIREBASE_CREDENTIALS=serviceAccountKey.json`

### 3. Install Dependencies
Backend:
```bash
cd backend
pip install -r requirements.txt
```

Frontend:
```bash
cd frontend
npm install
```

## 🚀 Test Run (Sunday - 15 mins)

1. Start backend:
   ```bash
   cd backend
   python app.py
   ```

2. Start frontend (new terminal):
   ```bash
   cd frontend
   npm run dev
   ```

3. Test flow:
   - [ ] Submit declaration for "Ramesh Kumar"
   - [ ] Verify AI suggestion appears
   - [ ] Fill checklist with scores
   - [ ] View in dashboard
   - [ ] Test Approve/Override buttons

## 📝 Demo Preparation (Sunday Evening)

- [ ] Read DEMO_SCRIPT.md thoroughly
- [ ] Prepare 2 sample candidate texts (Ramesh & Suresh)
- [ ] Practice the full demo flow 2-3 times
- [ ] Time yourself (should be under 5 minutes)
- [ ] Screenshot each screen for backup slides
- [ ] Prepare answers for Q&A (see DEMO_SCRIPT.md)

## 📊 Optional Enhancements (If Time Permits)

- [ ] Add a simple architecture diagram
- [ ] Create PowerPoint with screenshots
- [ ] Record a backup demo video
- [ ] Test on another computer/network
- [ ] Add more sample NSQF competencies

## 🎯 Monday Morning Checklist

- [ ] Laptop fully charged
- [ ] Both terminals running (backend + frontend)
- [ ] Browser open to localhost:3000
- [ ] Sample texts ready to paste
- [ ] Demo script printed/on phone
- [ ] Backup plan ready (screenshots, video)

## ⚠️ Known Issues to Mention

1. **"This is MVP scope"** - Only electrician trade (not 20+ trades)
2. **"Future enhancement"** - No video/image assessment yet
3. **"Demo mode"** - Using test Firebase (not production-grade security)

## 🏆 Key Selling Points

1. **Human-in-the-loop** - AI assists, assessor decides
2. **Consistency** - Standardized checklist reduces bias
3. **Offline-first** - Works in rural areas
4. **Scalable** - Firebase + Gemini can handle millions
5. **Fast** - Days → hours for RPL processing

## 📞 Emergency Contacts

If stuck on setup:
- Firebase docs: https://firebase.google.com/docs/firestore
- Gemini AI docs: https://ai.google.dev/docs
- React Vite docs: https://vitejs.dev

---

**Estimated Time Remaining: 1-2 hours**
**Confidence Level: HIGH ✅**

All code is complete. Just need config + practice!
