# EMOTION DETECTION WEB APP - Academic Submission

## 📋 Project Overview

An AI-powered web application that detects human emotions from facial images using deep learning. The system can analyze emotions from both uploaded images and live webcam capture.

**Student Information:**
- Name: [Your Full Name]
- Matric Number: [Your Matric Number]
- Department: [Your Department]
- Course: [Course Code/Name]

---

## 📁 Folder Structure (Academic Requirements)

This folder should be renamed to: **`SURNAME_MAT.MATRICNUMBER`**

Example: `ADEBAYO_MAT20191234` or `ADEBAYO_MAT20191234_EMOTION_DETECTION_WEB_APP`

### Contents:

```
SURNAME_MAT.MATRICNUMBER/
├── app.py                          # Flask backend application
├── model.py                        # Model training script
├── templates/
│   └── index.html                  # Web application frontend
├── static/                         # (Optional) CSS/JS files
├── database/
│   └── emotion_detection.db        # SQLite database
├── uploads/                        # Stored uploaded images
├── model.h5                        # Trained model file
├── requirements.txt                # Python dependencies
├── link_to_my_web_app.txt         # Hosting link
└── README_ACADEMIC_SUBMISSION.md   # This file
```

---

## 🚀 Quick Setup Guide

### Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 2: Train the Model (Optional)

```bash
python model.py
```

**Note:** The app works with a demo model if model.h5 is not present. For production, train with FER2013 dataset.

### Step 3: Run the Application

```bash
python app.py
```

Open browser: `http://127.0.0.1:5000`

---

## 💻 Features

### 1. Image Upload Detection
- Upload any image containing a face
- Automatic face detection using OpenCV
- Emotion classification with confidence scores
- Stores results in database

### 2. Webcam Live Capture
- Real-time webcam access
- Capture and analyze emotions instantly
- No need to save files manually

### 3. Database Tracking
- SQLite database stores all detections
- Records: user name, image path, emotion, confidence, timestamp
- View statistics and history

### 4. Emotion Categories
- Angry 😠
- Disgust 🤢
- Fear 😨
- Happy 😊
- Neutral 😐
- Sad 😢
- Surprised 😲

---

## 📊 Database Schema

```sql
CREATE TABLE emotion_records (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_name TEXT NOT NULL,
    image_path TEXT NOT NULL,
    detected_emotion TEXT NOT NULL,
    confidence REAL NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    source TEXT NOT NULL
);
```

**Fields:**
- `id`: Unique identifier
- `user_name`: Name of person using the app
- `image_path`: Path to saved image
- `detected_emotion`: Detected emotion label
- `confidence`: Model confidence (0-1)
- `timestamp`: When detection occurred
- `source`: 'upload' or 'webcam'

---

## 🎓 Training the Model

### Using FER2013 Dataset (Recommended)

1. Download FER2013 from Kaggle
2. Place `fer2013.csv` in the folder
3. Edit `model.py` line 281
4. Run: `python model.py`

### Using Custom Dataset

Create folder structure:
```
datasets/
├── angry/
├── disgust/
├── fear/
├── happy/
├── neutral/
├── sad/
└── surprised/
```

Add images to respective folders and run training.

---

## 🌐 Deployment Instructions

### Option 1: Render.com (Recommended)

1. Create account at https://render.com
2. Create new "Web Service"
3. Connect your GitHub repository
4. Configure:
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
5. Deploy
6. Update `link_to_my_web_app.txt` with your URL

### Option 2: Railway.app

1. Create account at https://railway.app
2. New Project → Deploy from GitHub
3. Select repository
4. Railway auto-detects Python
5. Add start command: `python app.py`
6. Deploy and get URL

### Option 3: PythonAnywhere (For Students)

1. Create free account at https://www.pythonanywhere.com
2. Upload files to web directory
3. Configure WSGI file
4. Reload web app
5. Get URL: `username.pythonanywhere.com`

**Update `link_to_my_web_app.txt` with your deployment link!**

---

## 🧪 Testing the Application

### Test Case 1: Upload Image
1. Open app in browser
2. Enter your name
3. Upload image with clear face
4. Click "Analyze Image"
5. Verify emotion detection

### Test Case 2: Webcam
1. Click "Use Webcam"
2. Allow camera access
3. Click "Capture & Analyze"
4. Verify detection

### Test Case 3: Database
1. Visit `/records` endpoint
2. Check stored detections
3. Visit `/stats` for statistics

---

## 📝 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Main web page |
| `/upload` | POST | Upload image for detection |
| `/webcam` | POST | Process webcam capture |
| `/records` | GET | View all database records |
| `/stats` | GET | Get app statistics |

---

## 🔧 Troubleshooting

### Issue: Model not found
**Solution:** Run `python model.py` to train the model, or the app will use demo predictions.

### Issue: No faces detected
**Solution:** Ensure image has clear, front-facing face with good lighting.

### Issue: Webcam not working
**Solution:** Check browser permissions and use HTTPS in production.

### Issue: Database error
**Solution:** Delete `database/emotion_detection.db` and restart app to recreate.

---

## 📚 Technologies Used

- **Backend**: Flask (Python web framework)
- **Frontend**: HTML5, CSS3, JavaScript
- **ML Framework**: TensorFlow/Keras
- **Computer Vision**: OpenCV
- **Database**: SQLite
- **Deployment**: Gunicorn WSGI server

---

## 📊 Model Architecture

- **Type**: Convolutional Neural Network (CNN)
- **Input**: 48x48 grayscale images
- **Layers**: 4 convolutional blocks + dense layers
- **Output**: 7 emotion classes (softmax activation)
- **Training**: FER2013 dataset (optional)

---

## 🎯 Academic Compliance Checklist

- [x] `app.py` - Flask backend ✅
- [x] `model.py` - Training script ✅
- [x] `templates/index.html` - Frontend ✅
- [x] `static/` folder - (Optional) ✅
- [x] `requirements.txt` - Dependencies ✅
- [x] `link_to_my_web_app.txt` - Hosting link ✅
- [x] `database/emotion_detection.db` - Database ✅
- [x] `model.h5` - Saved model ✅
- [x] GitHub upload ⏳
- [x] Web hosting ⏳

---

## 📦 Submission Checklist

Before submission:

1. **Rename folder** to `SURNAME_MAT.MATRICNUMBER`
2. **Train model** and verify `model.h5` exists
3. **Test locally** - ensure app runs without errors
4. **Upload to GitHub** repository
5. **Deploy to hosting** platform
6. **Update** `link_to_my_web_app.txt` with deployment URL
7. **Add your details** to all files (name, matric number)
8. **Zip folder** for submission if required

---

## 👨‍💻 Usage Guide

### For Offline Use:
1. Run locally using `python app.py`
2. Users access via `http://127.0.0.1:5000`
3. All data saved to local database

### For Online Use:
1. Deploy to hosting platform
2. Share public URL
3. Users can access from anywhere
4. Database persists on server

---

## 🎓 Learning Outcomes

This project demonstrates:
- Full-stack web development
- Deep learning model training
- Computer vision applications
- Database management
- Web deployment
- RESTful API design

---

## 📞 Support

For issues:
1. Check troubleshooting section
2. Review error messages
3. Verify all dependencies installed
4. Check Python version (3.8+)

---

## 📄 License

This is an academic project for educational purposes.

---

## 🙏 Acknowledgments

- FER2013 Dataset creators
- TensorFlow/Keras teams
- Flask framework developers
- OpenCV community

---

**Good luck with your submission! 🎓✨**

---

## Quick Commands Reference

```bash
# Setup
pip install -r requirements.txt

# Train model (optional)
python model.py

# Run app
python app.py

# View database records
curl http://127.0.0.1:5000/records

# Get statistics
curl http://127.0.0.1:5000/stats

# Deploy with gunicorn
gunicorn app:app --bind 0.0.0.0:5000
```

---

**Remember to update all files with your personal information before submission!**
