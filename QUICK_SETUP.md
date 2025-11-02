# 🚀 Quick Setup (5 Minutes)

## Prerequisites Checklist
- [ ] Python 3.8+ installed → https://python.org/downloads
- [ ] Node.js 16+ installed → https://nodejs.org
- [ ] Git installed → https://git-scm.com

---

## Step 1: Get the Code (1 min)

```bash
git clone https://github.com/Oluwanifemi77/FaceRecognition.git
cd FaceRecognition
git checkout claude/emotion-recognition-app-011CUjdUcAu5XTU6ETgnpw5G
```

---

## Step 2: Backend Setup (3 min)

```bash
cd backend

# Windows
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python create_demo_model.py
python app.py

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python create_demo_model.py
python app.py
```

✅ Should see: `Server starting on http://127.0.0.1:5000`

**Keep this terminal open!**

---

## Step 3: Frontend Setup (1 min)

**Open NEW terminal:**

```bash
cd FaceRecognition/frontend
npm install
npm run dev
```

✅ Should see: `Local: http://localhost:3000/`

---

## Step 4: Open Browser

Go to: **http://localhost:3000**

🎉 Done! Try uploading an image or using your webcam!

---

## Deploy to Vercel (Production)

### Frontend:
1. Go to https://vercel.com
2. Sign in with GitHub
3. Import `FaceRecognition` repo
4. Set Root Directory: `frontend`
5. Click Deploy

### Backend:
1. Go to https://render.com
2. Sign in with GitHub
3. New Web Service → Select repo
4. Root Directory: `backend`
5. Build: `pip install -r requirements.txt && python create_demo_model.py`
6. Start: `gunicorn app:app`
7. Deploy

### Connect Them:
1. Copy your Render backend URL
2. In Vercel: Settings → Environment Variables
3. Add: `VITE_API_URL` = your Render URL
4. Redeploy in Vercel

---

## Troubleshooting

**"Port already in use":**
- Close other terminals running the app
- Restart your computer

**"Module not found":**
```bash
pip install -r requirements.txt
```

**Frontend won't start:**
```bash
rm -rf node_modules
npm install
```

**Can't find create_demo_model.py:**
```bash
# Make sure you're in the backend folder
cd backend
ls  # Should see create_demo_model.py
```

---

## File Structure Reference

```
FaceRecognition/
├── backend/              ← Flask API
│   ├── app.py           ← Main server
│   ├── requirements.txt ← Dependencies
│   └── models/          ← AI model here
└── frontend/            ← React app
    ├── src/             ← Components
    └── package.json     ← Dependencies
```

---

## What Each Terminal Does

**Terminal 1 (Backend):**
- Runs Python Flask server on port 5000
- Handles AI predictions
- Must stay open while using app

**Terminal 2 (Frontend):**
- Runs React development server on port 3000
- Shows the website
- Must stay open while using app

---

## Testing Checklist

- [ ] Backend running (check http://localhost:5000)
- [ ] Frontend running (check http://localhost:3000)
- [ ] Can upload image
- [ ] Can capture from webcam
- [ ] See emotion results

---

## Next Steps

1. ✅ Test locally
2. 📚 Read [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) for full deployment
3. 🎯 Train real model with FER2013 dataset
4. 🎨 Customize the UI
5. 🚀 Deploy to production

---

**Need detailed help?** → Read [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)

**Having issues?** → Check troubleshooting section above
