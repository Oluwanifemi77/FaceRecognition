# Complete Deployment Guide

## Part 1: Running on Your Local PC

### Prerequisites
Download and install these first:

1. **Python 3.8+**: https://www.python.org/downloads/
   - ✅ During installation, CHECK "Add Python to PATH"

2. **Node.js 16+**: https://nodejs.org/
   - Download the LTS version

3. **Git**: https://git-scm.com/downloads
   - For cloning the repository

4. **Code Editor** (Optional but recommended):
   - VS Code: https://code.visualstudio.com/

---

## Part 2: Clone & Setup on Your PC

### Step 1: Clone the Repository

Open your terminal/command prompt and run:

```bash
# Clone the repository
git clone https://github.com/Oluwanifemi77/FaceRecognition.git

# Navigate into the project
cd FaceRecognition

# Switch to the correct branch
git checkout claude/emotion-recognition-app-011CUjdUcAu5XTU6ETgnpw5G
```

### Step 2: Setup Backend

```bash
# Navigate to backend folder
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows (Command Prompt):
venv\Scripts\activate

# On Windows (PowerShell):
venv\Scripts\Activate.ps1

# On macOS/Linux:
source venv/bin/activate

# Install Python dependencies (this takes 5-10 minutes)
pip install -r requirements.txt

# Create a demo model for testing
python create_demo_model.py
```

**Expected Output:**
```
Creating demo model...
✅ Demo model created successfully at: models/emotion_model.h5
```

### Step 3: Start Backend Server

```bash
# Make sure you're in the backend folder with venv activated
python app.py
```

**Expected Output:**
```
============================================================
🎭 Emotion Recognition API Server
============================================================
Server starting on http://127.0.0.1:5000
Model loaded: True
============================================================
```

**Keep this terminal window open!** The backend must stay running.

### Step 4: Setup Frontend (New Terminal)

Open a **NEW** terminal window:

```bash
# Navigate to project (adjust path to where you cloned)
cd FaceRecognition/frontend

# Install Node.js dependencies (takes 2-5 minutes)
npm install

# Start the development server
npm run dev
```

**Expected Output:**
```
  VITE v5.0.12  ready in 1234 ms

  ➜  Local:   http://localhost:3000/
  ➜  press h to show help
```

### Step 5: Open in Browser

Open your browser and go to: **http://localhost:3000**

You should see the Emotion Recognition app! 🎉

---

## Part 3: Testing Locally

### Upload an Image
1. Click "Upload Image" section
2. Drag & drop a photo with a face OR click to browse
3. Click "Analyze Emotion"
4. See results!

### Use Webcam
1. Scroll to "Webcam Capture" section
2. Click "Enable Webcam" (allow browser permissions)
3. Click "Capture Photo"
4. Click "Analyze Emotion"

### Test Images
For best results with the demo model:
- Use clear, front-facing photos
- Good lighting
- One face in the image
- Try different expressions!

---

## Part 4: Deploy to Vercel (Frontend)

### Option A: Deploy via Vercel Website (Easiest)

1. **Create Vercel Account**
   - Go to https://vercel.com
   - Sign up with GitHub

2. **Import Project**
   - Click "Add New..." → "Project"
   - Select your GitHub repository: `FaceRecognition`
   - Vercel will auto-detect it

3. **Configure Build Settings**
   - Framework Preset: **Vite**
   - Root Directory: **frontend**
   - Build Command: `npm run build`
   - Output Directory: `dist`
   - Install Command: `npm install`

4. **Environment Variables**
   Click "Environment Variables" and add:
   - Name: `VITE_API_URL`
   - Value: Your backend URL (see Part 5)

5. **Deploy**
   - Click "Deploy"
   - Wait 2-3 minutes
   - Get your URL: `https://your-app.vercel.app`

### Option B: Deploy via Vercel CLI

```bash
# Install Vercel CLI globally
npm install -g vercel

# Navigate to frontend folder
cd frontend

# Login to Vercel
vercel login

# Deploy
vercel

# Follow prompts:
# - Set up and deploy? Yes
# - Which scope? Select your account
# - Link to existing project? No
# - Project name? emotion-recognition
# - Directory? ./
# - Override settings? No

# Deploy to production
vercel --prod
```

---

## Part 5: Deploy Backend (Flask API)

### Option A: Deploy to Render (Recommended - Free Tier)

1. **Create Render Account**
   - Go to https://render.com
   - Sign up with GitHub

2. **Create New Web Service**
   - Click "New" → "Web Service"
   - Connect your GitHub repository
   - Select `FaceRecognition`

3. **Configure Service**
   - Name: `emotion-recognition-api`
   - Region: Choose closest to you
   - Branch: `claude/emotion-recognition-app-011CUjdUcAu5XTU6ETgnpw5G`
   - Root Directory: `backend`
   - Runtime: **Python 3**
   - Build Command: `pip install -r requirements.txt && python create_demo_model.py`
   - Start Command: `gunicorn app:app`

4. **Environment Variables**
   Add these:
   - `PYTHON_VERSION`: `3.11.0`
   - `FLASK_ENV`: `production`

5. **Deploy**
   - Click "Create Web Service"
   - Wait 5-10 minutes for first deployment
   - Get your URL: `https://emotion-recognition-api.onrender.com`

### Option B: Deploy to Railway

1. **Create Railway Account**
   - Go to https://railway.app
   - Sign up with GitHub

2. **Create New Project**
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose `FaceRecognition`

3. **Configure**
   - Add service: Python
   - Root directory: `backend`
   - Build command: `pip install -r requirements.txt`
   - Start command: `gunicorn app:app`

4. **Generate Domain**
   - Go to Settings → Generate Domain
   - Get URL: `https://your-app.railway.app`

---

## Part 6: Connect Frontend to Backend

After deploying backend, update frontend:

1. **Get Your Backend URL**
   - From Render: `https://emotion-recognition-api.onrender.com`
   - From Railway: `https://your-app.railway.app`

2. **Update Vercel Environment Variable**
   - Go to Vercel Dashboard
   - Select your project
   - Settings → Environment Variables
   - Update `VITE_API_URL` to your backend URL
   - Redeploy: Deployments → Click "..." → Redeploy

3. **Update CORS in Backend**

   Edit `backend/app.py` line 20-21:
   ```python
   CORS(app, resources={
       r"/*": {
           "origins": ["https://your-app.vercel.app", "http://localhost:3000"],
   ```

   Replace `your-app.vercel.app` with your actual Vercel URL.

   Commit and push:
   ```bash
   git add backend/app.py
   git commit -m "Update CORS for production"
   git push
   ```

---

## Part 7: Train a Real Model (Optional but Recommended)

The demo model has random weights. For accurate predictions:

### Download FER2013 Dataset

1. Go to https://www.kaggle.com/datasets/msambare/fer2013
2. Download `fer2013.csv`
3. Place in `backend/datasets/`

### Train the Model

```bash
cd backend

# Make sure virtual environment is activated
# venv\Scripts\activate (Windows) or source venv/bin/activate (Mac/Linux)

# Edit model_training.py
# Uncomment line 281:
# X_train, X_test, y_train, y_test = trainer.load_fer2013_dataset('datasets/fer2013.csv')

# Run training (takes 30-60 minutes)
python model_training.py
```

### Deploy Updated Model

**For Render/Railway:**
- The new model will be in `backend/models/emotion_model.h5`
- Commit and push:
  ```bash
  git add backend/models/emotion_model.h5
  git commit -m "Add trained emotion model"
  git push
  ```
- Render/Railway will auto-deploy

---

## Part 8: Troubleshooting

### Backend Issues

**Port already in use:**
```bash
# Windows
netstat -ano | findstr :5000
taskkill /PID <PID> /F

# Mac/Linux
lsof -ti:5000 | xargs kill -9
```

**Module not found errors:**
```bash
pip install -r requirements.txt --force-reinstall
```

**Model not loading:**
```bash
python create_demo_model.py
```

### Frontend Issues

**npm install fails:**
```bash
# Delete node_modules and try again
rm -rf node_modules package-lock.json
npm install
```

**Port 3000 in use:**
```bash
# Edit vite.config.js, change port to 3001
server: {
  port: 3001,
```

**API connection errors:**
- Check backend is running on port 5000
- Check CORS settings
- Check `VITE_API_URL` in frontend/.env

### Deployment Issues

**Vercel build fails:**
- Check build logs in Vercel dashboard
- Ensure `frontend/` is set as root directory
- Verify build command: `npm run build`

**Backend crashes on Render:**
- Check logs in Render dashboard
- Ensure `gunicorn` is in requirements.txt
- Verify Python version (3.8+)

**CORS errors in production:**
- Update backend CORS origins with your Vercel URL
- Redeploy backend after changes

---

## Part 9: Useful Commands

### Local Development

```bash
# Backend
cd backend
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux
python app.py

# Frontend
cd frontend
npm run dev

# Build for production
npm run build
npm run preview
```

### Git Commands

```bash
# Check status
git status

# Pull latest changes
git pull origin claude/emotion-recognition-app-011CUjdUcAu5XTU6ETgnpw5G

# Create new feature
git checkout -b my-new-feature
git add .
git commit -m "Add new feature"
git push origin my-new-feature
```

---

## Part 10: Production URLs

After deployment, you'll have:

- **Frontend**: `https://your-app.vercel.app`
- **Backend**: `https://your-api.render.com` or `https://your-app.railway.app`
- **GitHub**: `https://github.com/Oluwanifemi77/FaceRecognition`

### Share Your App

Once deployed, share your Vercel URL with anyone!
They can use it without installing anything.

---

## Need Help?

### Common Questions

**Q: Do I need to deploy backend to use the app?**
A: For local testing, no. For sharing with others, yes.

**Q: Is Vercel/Render free?**
A: Yes! Both have generous free tiers perfect for this project.

**Q: Can I use a custom domain?**
A: Yes! Both Vercel and Render support custom domains in settings.

**Q: How do I update my deployed app?**
A: Just push to GitHub. Vercel and Render auto-deploy on push.

**Q: The app is slow in production**
A: Free tiers have cold starts. First request takes 10-30 seconds. Consider upgrading or keeping it warm with a ping service.

---

## Summary Checklist

- [ ] Python, Node.js, Git installed
- [ ] Repository cloned
- [ ] Backend running locally (port 5000)
- [ ] Frontend running locally (port 3000)
- [ ] Tested image upload
- [ ] Tested webcam capture
- [ ] Backend deployed to Render/Railway
- [ ] Frontend deployed to Vercel
- [ ] Environment variables configured
- [ ] CORS updated for production
- [ ] Both frontend and backend connected

Congratulations! Your Emotion Recognition app is now live! 🎉
