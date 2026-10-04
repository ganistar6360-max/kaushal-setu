# Kaushal Setu - LOCAL VERSION Setup Guide

## ✅ What Changed for Local Setup

This version runs **100% locally** without any external services:
- ❌ No Firebase needed
- ❌ No Gemini API key needed  
- ❌ No internet connection needed
- ✅ Local JSON file storage (backend/local_data.json)
- ✅ Simple keyword-based AI (replaces Gemini)

---

## 🚀 Quick Start (3 Steps)

### Step 1: Install Backend Dependencies

```bash
cd backend
pip install -r requirements-local.txt
```

This installs only Flask and Flask-CORS (no Firebase, no Gemini).

---

### Step 2: Install Frontend Dependencies

```bash
cd ../frontend
npm install
```

This installs React, Vite, and minimal dependencies.

---

### Step 3: Run the Application

**Open 2 terminal windows:**

**Terminal 1 - Start Backend:**
```bash
cd backend
python app.py
```

You should see:
```
* Running on http://127.0.0.1:5000
* Debug mode: on
```

**Terminal 2 - Start Frontend:**
```bash
cd frontend
npm run dev
```

You should see:
```
Local: http://localhost:3000/
```

---

## 🎯 Access the App

Open your browser: **http://localhost:3000**

---

## 📝 Test with Sample Data

### Test Worker Profile

**Name:** Ramesh Kumar

**Experience Text:**
```
I have worked for 5 years wiring houses and small shops. 
I can install distribution boards, do earthing, and read 
circuit diagrams. I know how to test circuits with a 
multimeter and follow safety codes.
```

**Expected AI Result:** NSQF Level 4

The local AI analyzes:
- Years of experience (5 years)
- Keywords: "distribution boards", "circuit diagrams", "multimeter", "safety codes"
- Suggests appropriate NSQF level

---

## 🗂️ Data Storage

All candidate data is stored in:
```
backend/local_data.json
```

This file is created automatically when you submit your first declaration.

---

## 🔧 How the Local AI Works

The keyword-based system analyzes:

**Level 5 Keywords:** supervise, manage, train, design, industrial (10+ years)
**Level 4 Keywords:** distribution board, troubleshoot, multimeter, testing (4+ years)  
**Level 3 Keywords:** wiring, basic, residential, house (2+ years)
**Level 2 Keywords:** apprentice, learning, beginner (0-2 years)

It combines keyword matching with years of experience to suggest the NSQF level.

---

## ✅ What's Working Locally

✅ Self-declaration form submission  
✅ Local AI skill level suggestion  
✅ Competency checklist scoring  
✅ Assessor dashboard  
✅ Approve/Override decisions  
✅ All data persists in local JSON file

---

## 🎉 You're Ready!

No configuration files needed. Just run the commands and start testing!
