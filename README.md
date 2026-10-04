# Kaushal Setu — AI-Assisted RPL Skill Assessment Tool

**Smart India Hackathon 2026 — Problem Statement SIH26242**

An AI-powered web application that helps assess informal workers' trade skills against NSQF (National Skills Qualification Framework) criteria, currently supporting the **Electrician** trade.

## 🎯 Key Features

1. **Self-Declaration Form** — Workers describe their experience in free text
2. **AI Skill Mapping** — Google Gemini API suggests NSQF level based on experience
3. **Competency Checklist** — Structured 0-5 scoring for each NSQF skill criterion
4. **Assessor Dashboard** — Human assessors review AI suggestions and make final decisions
5. **Offline Support** — Firebase offline persistence for no-connectivity scenarios

## 🛠️ Tech Stack

- **Frontend:** React (Vite), plain CSS
- **Backend:** Python Flask
- **Database:** Firebase Firestore
- **AI:** Google Gemini API (gemini-1.5-flash)

## 🚀 Quick Start

### Backend Setup

```bash
cd backend
pip install -r requirements.txt
cp .env.example .env
# Edit .env with your GEMINI_API_KEY and add serviceAccountKey.json
python app.py
```

### Frontend Setup

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

**Candidate 2: Suresh Yadav**
- 3 years experience as a helper to a licensed electrician

