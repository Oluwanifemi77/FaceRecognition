# System Architecture

## Overview

The Emotion Recognition application is built with a **client-server architecture** separating the React frontend from the Flask backend.

```
┌─────────────────────────────────────────────────────────────┐
│                         USER                                 │
│                     (Web Browser)                            │
└────────────────────────┬────────────────────────────────────┘
                         │
                         │ HTTP/HTTPS
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                   FRONTEND (React)                           │
│                  Port 3000 (dev) / Vercel                    │
├─────────────────────────────────────────────────────────────┤
│  Components:                                                 │
│  ├─ Navbar, Hero, Footer                                    │
│  ├─ ImageUpload (drag & drop + file picker)                │
│  ├─ WebcamCapture (live camera feed)                       │
│  ├─ ResultDisplay (emotion results)                         │
│  └─ ModelInfo (model details)                               │
│                                                              │
│  Libraries:                                                  │
│  ├─ React 18 (UI framework)                                │
│  ├─ TailwindCSS (styling)                                   │
│  ├─ Framer Motion (animations)                             │
│  ├─ Axios (HTTP client)                                     │
│  └─ react-webcam (camera access)                           │
└────────────────────────┬────────────────────────────────────┘
                         │
                         │ REST API (JSON)
                         │ /api/upload
                         │ /api/webcam
                         │ /api/predict
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                   BACKEND (Flask)                            │
│                Port 5000 (dev) / Render/Railway             │
├─────────────────────────────────────────────────────────────┤
│  API Layer (app.py)                                         │
│  ├─ Route handlers                                          │
│  ├─ CORS configuration                                      │
│  ├─ File upload handling                                    │
│  └─ Error handling                                          │
│                         │                                    │
│                         ▼                                    │
│  Service Layer (link_app.py)                                │
│  ├─ EmotionRecognitionService                              │
│  ├─ Image preprocessing                                     │
│  ├─ Base64 conversion                                       │
│  └─ Dataset management                                      │
│                         │                                    │
│                         ▼                                    │
│  ML Layer (face_emotions.py)                                │
│  ├─ FaceEmotionDetector class                              │
│  ├─ Face detection (OpenCV)                                │
│  ├─ Image preprocessing                                     │
│  └─ Emotion prediction                                      │
│                         │                                    │
│                         ▼                                    │
│  Model (emotion_model.h5)                                   │
│  └─ Trained CNN model                                       │
│                                                              │
│  Libraries:                                                  │
│  ├─ Flask (web framework)                                   │
│  ├─ TensorFlow/Keras (ML)                                   │
│  ├─ OpenCV (computer vision)                                │
│  ├─ NumPy (arrays)                                          │
│  └─ Pillow (image processing)                               │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                   FILE SYSTEM                                │
├─────────────────────────────────────────────────────────────┤
│  models/                                                     │
│  └─ emotion_model.h5 (trained CNN)                         │
│                                                              │
│  uploads/                                                    │
│  └─ user uploaded images                                    │
│                                                              │
│  datasets/ (for retraining)                                │
│  ├─ happy/                                                  │
│  ├─ sad/                                                    │
│  ├─ angry/                                                  │
│  ├─ surprised/                                              │
│  ├─ neutral/                                                │
│  ├─ fear/                                                   │
│  └─ disgust/                                                │
└─────────────────────────────────────────────────────────────┘
```

## Data Flow

### Image Upload Flow

```
1. User uploads image
   └─> Frontend (ImageUpload.jsx)

2. Image sent as FormData
   └─> POST /api/upload
       └─> Backend (app.py)

3. Save & process image
   └─> link_app.py (process_uploaded_image)
       └─> face_emotions.py (detect_and_predict)

4. Detect faces
   └─> OpenCV Haar Cascade
       └─> Returns face bounding boxes

5. Predict emotions
   └─> Preprocess face (grayscale, resize, normalize)
       └─> emotion_model.h5 (CNN prediction)
           └─> Softmax probabilities

6. Return results
   └─> JSON response to frontend
       └─> ResultDisplay.jsx renders results
```

### Webcam Capture Flow

```
1. User enables webcam
   └─> Frontend (WebcamCapture.jsx)
       └─> react-webcam captures frame

2. Capture as base64
   └─> Convert to base64 string

3. Send to backend
   └─> POST /api/webcam
       └─> Backend (app.py)

4. Decode & process
   └─> link_app.py (process_base64_image)
       └─> Decode base64 to image
           └─> face_emotions.py (detect_and_predict)

5. Same prediction flow as image upload
   └─> Return results to frontend
```

## Component Communication

### Frontend Components

```
App.jsx (Root)
├─ Navbar.jsx
├─ Hero.jsx
├─ ImageUpload.jsx
│  ├─ LoadingSpinner.jsx
│  └─ ResultDisplay.jsx
├─ WebcamCapture.jsx
│  ├─ LoadingSpinner.jsx
│  └─ ResultDisplay.jsx
├─ ModelInfo.jsx
└─ Footer.jsx

Utilities:
└─ utils/api.js (API calls)
```

### Backend Modules

```
app.py (Flask App)
├─ Routes
│  ├─ / (status)
│  ├─ /health
│  ├─ /api/upload
│  ├─ /api/webcam
│  ├─ /api/predict
│  └─ /api/model-info
│
├─ link_app.py (Service Layer)
│  └─ EmotionRecognitionService
│     ├─ process_uploaded_image()
│     ├─ process_webcam_frame()
│     ├─ process_base64_image()
│     └─ get_model_info()
│
└─ face_emotions.py (ML Layer)
   └─ FaceEmotionDetector
      ├─ detect_faces()
      ├─ preprocess_face()
      ├─ predict_emotion()
      └─ detect_and_predict()
```

## ML Model Architecture

```
Input: 48x48 grayscale image
│
├─ Conv2D(64) + BatchNorm + Conv2D(64) + MaxPool + Dropout
│
├─ Conv2D(128) + BatchNorm + Conv2D(128) + MaxPool + Dropout
│
├─ Conv2D(256) + BatchNorm + Conv2D(256) + MaxPool + Dropout
│
├─ Conv2D(512) + BatchNorm + Conv2D(512) + MaxPool + Dropout
│
├─ Flatten
│
├─ Dense(512) + BatchNorm + Dropout
│
├─ Dense(256) + BatchNorm + Dropout
│
└─ Dense(7) + Softmax
   │
   └─ Output: 7 emotion probabilities
      ├─ Angry
      ├─ Disgust
      ├─ Fear
      ├─ Happy
      ├─ Neutral
      ├─ Sad
      └─ Surprised
```

## Deployment Architecture

### Development

```
┌─────────────┐         ┌─────────────┐
│  Frontend   │   ←→    │   Backend   │
│ localhost:  │  CORS   │ localhost:  │
│    3000     │         │    5000     │
└─────────────┘         └─────────────┘
```

### Production

```
┌──────────────────┐         ┌─────────────────┐
│     Frontend     │   ←→    │     Backend     │
│    Vercel CDN    │  HTTPS  │  Render/Railway │
│   (Static Site)  │         │  (Python Server)│
└──────────────────┘         └─────────────────┘
        │                            │
        │                            │
        ▼                            ▼
┌──────────────────┐         ┌─────────────────┐
│   React Build    │         │  Gunicorn + ML  │
│   (SPA - dist/)  │         │     Model       │
└──────────────────┘         └─────────────────┘
```

## Technology Stack Summary

| Layer | Technology | Purpose |
|-------|-----------|---------|
| Frontend | React 18 | UI framework |
| Build Tool | Vite | Fast development & bundling |
| Styling | TailwindCSS | Utility-first CSS |
| Animation | Framer Motion | Smooth transitions |
| HTTP Client | Axios | API communication |
| Backend | Flask 3.0 | Web framework |
| ML Framework | TensorFlow 2.15 | Deep learning |
| Model Format | Keras .h5 | Trained model storage |
| Face Detection | OpenCV | Computer vision |
| Data Processing | NumPy, Pandas | Array operations |
| Production Server | Gunicorn | WSGI HTTP server |
| Frontend Deploy | Vercel | CDN & hosting |
| Backend Deploy | Render/Railway | Cloud hosting |

## Security Considerations

- **CORS**: Restricted to specific origins
- **File Size Limit**: 16MB max upload
- **File Type Validation**: Only images allowed
- **Input Sanitization**: Base64 validation
- **Error Handling**: No sensitive info exposed
- **HTTPS**: Enforced in production

## Scalability

### Current Limitations
- Single model instance per backend
- Synchronous processing
- No caching
- Cold starts on free tiers

### Future Improvements
- [ ] Redis caching for model predictions
- [ ] Async processing with Celery
- [ ] Multiple model instances
- [ ] CDN for uploaded images
- [ ] Database for user history
- [ ] Rate limiting
- [ ] WebSocket for real-time video

## Performance

### Expected Response Times

| Operation | Local | Production |
|-----------|-------|------------|
| Face Detection | 50-200ms | 100-300ms |
| Model Prediction | 50-150ms | 100-250ms |
| Total (Image) | 100-500ms | 200-800ms |
| Frontend Load | <1s | 1-3s |
| Backend Cold Start | N/A | 5-30s |

## Monitoring

### Key Metrics to Track

- API response times
- Model inference time
- Error rates
- Upload success rate
- Face detection success rate
- Memory usage
- CPU usage

### Logging

- All API requests logged
- Errors with stack traces
- Model predictions (optional)
- File uploads

## Development Workflow

```
1. Local Development
   ├─ Backend: python app.py
   └─ Frontend: npm run dev

2. Testing
   ├─ Manual testing in browser
   └─ API testing with Postman/curl

3. Git Workflow
   ├─ Create feature branch
   ├─ Make changes
   ├─ Commit & push
   └─ Merge to main

4. Deployment
   ├─ Push to GitHub
   ├─ Vercel auto-deploys frontend
   └─ Render auto-deploys backend
```

## Maintenance

### Regular Tasks

- [ ] Monitor error logs
- [ ] Update dependencies
- [ ] Retrain model with new data
- [ ] Backup datasets
- [ ] Review performance metrics

### Update Process

```bash
# Update backend
cd backend
pip install --upgrade -r requirements.txt

# Update frontend
cd frontend
npm update

# Test locally before deploying
```

---

For more details, see:
- [README.md](README.md) - Project overview
- [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) - Deployment instructions
- [QUICK_SETUP.md](QUICK_SETUP.md) - Quick start guide
