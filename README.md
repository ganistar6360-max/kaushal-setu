# Kaushal Setu — AI-Assisted RPL Skill Assessment Tool

**Smart India Hackathon 2026 — Problem Statement SIH26242**

An AI-powered web application that helps assess informal workers' trade skills against NSQF (National Skills Qualification Framework) criteria, currently supporting the **Electrician** trade.

## 🎯 Key Features

1. **Self-Declaration Form** — Workers describe their experience in free text
2. **AI Skill Mapping** — Suggests NSQF level based on experience (Gemini API or local keyword-based)
3. **Competency Checklist** — Structured 0-5 scoring for each NSQF skill criterion
4. **Assessor Dashboard** — Human assessors review AI suggestions and make final decisions
5. **Offline Support** — Local JSON storage or Firebase offline persistence

## 🛠️ Tech Stack

- **Frontend:** React (Vite), plain CSS
- **Backend:** Python Flask
- **Database:** Firebase Firestore (cloud) or Local JSON file (local setup)
- **AI:** Google Gemini API (cloud) or Keyword-based system (local)

## 🚀 Setup Options

### Option 1: Local Setup (No External Services)

**Perfect for testing without Firebase or Gemini API!**

See **[LOCAL_SETUP.md](LOCAL_SETUP.md)** for complete instructions.

Quick start:
```bash
# Backend
cd backend
pip install -r requirements-local.txt
python app.py

# Frontend (in another terminal)
cd frontend
npm install
npm run dev
```

Access at: http://localhost:3000

**Features:**
- ✅ No Firebase needed
- ✅ No Gemini API key needed
- ✅ Works offline
- ✅ Local JSON file storage
- ✅ Simple keyword-based AI

---

### Option 2: Cloud Setup (Firebase + Gemini)

**For production deployment with full AI capabilities.**

See **[SETUP.md](SETUP.md)** for complete instructions.

#### Backend Setup

```bash
cd backend
pip install -r requirements.txt
cp .env.example .env
# Edit .env with your GEMINI_API_KEY and add serviceAccountKey.json
python app.py
```

#### Frontend Setup

```bash
cd frontend
npm install
# Edit src/services/firebase.js with your Firebase config
npm run dev
```

## ⚠️ Important Note

**This tool is designed to SUPPORT an assessor's decision, not replace it.**

The assessor always has final override control.

## 🧪 Sample Test Data

**Candidate 1: Ramesh Kumar**
- 8 years informal experience doing household and small commercial wiring
- Expected NSQF Level: 4-5

**Candidate 2: Suresh Yadav**
- 3 years experience as a helper to a licensed electrician
- Expected NSQF Level: 2-3

## 📁 Project Structure

```
kaushal-setu/
├── backend/
│   ├── app.py                    # Main Flask application
│   ├── routes/                   # API route handlers
│   ├── services/                 # Business logic (AI, storage)
│   ├── data/                     # NSQF qualification data
│   ├── requirements.txt          # Cloud dependencies
│   └── requirements-local.txt    # Local setup dependencies
├── frontend/
│   ├── src/
│   │   ├── components/           # React components
│   │   └── services/             # API and Firebase clients
│   └── package.json
├── LOCAL_SETUP.md                # Local setup guide
└── SETUP.md                      # Cloud setup guide
```

## 🤝 Contributing

This is a Smart India Hackathon 2026 project. Contributions and suggestions are welcome!

