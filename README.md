# Emotion Recognition Web Application

A complete, production-grade AI-powered web application that detects human emotions from facial images using deep learning. Built with React, TailwindCSS, Flask, and TensorFlow.

![Emotion Recognition](https://img.shields.io/badge/AI-Emotion%20Recognition-blue)
![React](https://img.shields.io/badge/React-18.2-61DAFB?logo=react)
![Flask](https://img.shields.io/badge/Flask-3.0-000000?logo=flask)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.15-FF6F00?logo=tensorflow)

---

## 📖 Quick Links

- **🚀 [5-Minute Setup Guide](QUICK_SETUP.md)** - Get running locally fast!
- **☁️ [Complete Deployment Guide](DEPLOYMENT_GUIDE.md)** - Deploy to Vercel & Render
- **📚 Full Documentation** - You're reading it!

---

## Features

- **Modern React UI** with TailwindCSS and Framer Motion animations
- **Dual Input Methods**: Upload images or use webcam for real-time capture
- **Advanced ML Model**: CNN-based emotion recognition with 7 emotion classes
- **Face Detection**: OpenCV Haar Cascade for robust face detection
- **Detailed Results**: Confidence scores and probability distributions for all emotions
- **Responsive Design**: Mobile-friendly interface
- **RESTful API**: Clean Flask backend with CORS support
- **Model Retraining**: Automatic dataset collection for continuous improvement

## Detected Emotions

- 😊 Happy
- 😢 Sad
- 😠 Angry
- 😲 Surprised
- 😐 Neutral
- 😨 Fear
- 🤢 Disgust

## Tech Stack

### Frontend
- **React 18** - Modern UI library
- **Vite** - Lightning-fast build tool
- **TailwindCSS** - Utility-first CSS framework
- **Framer Motion** - Smooth animations
- **Axios** - HTTP client
- **React Webcam** - Webcam integration

### Backend
- **Flask** - Python web framework
- **TensorFlow/Keras** - Deep learning framework
- **OpenCV** - Computer vision library
- **NumPy & Pandas** - Data processing

### ML Model
- **CNN Architecture** - Custom convolutional neural network
- **Transfer Learning** - Optional MobileNetV2 support
- **Data Augmentation** - Improved model generalization

## Project Structure

```
FaceRecognition/
├── backend/
│   ├── app.py                 # Flask API server
│   ├── face_emotions.py       # Face detection & emotion prediction
│   ├── model_training.py      # CNN model training script
│   ├── link_app.py           # Service layer for modularity
│   ├── requirements.txt      # Python dependencies
│   ├── models/               # Trained models
│   ├── uploads/              # Uploaded images
│   └── datasets/             # Training data (organized by emotion)
│       ├── happy/
│       ├── sad/
│       ├── angry/
│       ├── surprised/
│       ├── neutral/
│       ├── fear/
│       └── disgust/
│
└── frontend/
    ├── src/
    │   ├── components/       # React components
    │   │   ├── Navbar.jsx
    │   │   ├── Hero.jsx
    │   │   ├── ImageUpload.jsx
    │   │   ├── WebcamCapture.jsx
    │   │   ├── ResultDisplay.jsx
    │   │   ├── ModelInfo.jsx
    │   │   ├── LoadingSpinner.jsx
    │   │   └── Footer.jsx
    │   ├── utils/
    │   │   └── api.js        # API utility functions
    │   ├── App.jsx           # Main app component
    │   ├── main.jsx          # Entry point
    │   └── index.css         # Global styles
    ├── package.json
    ├── vite.config.js
    ├── tailwind.config.js
    └── postcss.config.js
```

## Installation & Setup

### Prerequisites
- Python 3.8+
- Node.js 16+
- npm or yarn

### Backend Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

3. Install Python dependencies:
```bash
pip install -r requirements.txt
```

4. Create necessary directories:
```bash
mkdir -p models uploads datasets
```

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install Node.js dependencies:
```bash
npm install
```

## Training the Model

Before running the application, you need to train the emotion recognition model:

### Option 1: Use FER2013 Dataset (Recommended)

1. Download the FER2013 dataset from [Kaggle](https://www.kaggle.com/datasets/msambare/fer2013)
2. Place `fer2013.csv` in the `backend/datasets/` directory
3. Update `model_training.py` to use FER2013:

```python
# In model_training.py main() function, uncomment:
X_train, X_test, y_train, y_test = trainer.load_fer2013_dataset('datasets/fer2013.csv')
```

4. Run training:
```bash
cd backend
python model_training.py
```

### Option 2: Use Custom Dataset

1. Organize your images in the following structure:
```
backend/datasets/
├── happy/*.jpg
├── sad/*.jpg
├── angry/*.jpg
├── surprised/*.jpg
├── neutral/*.jpg
├── fear/*.jpg
└── disgust/*.jpg
```

2. Run training:
```bash
cd backend
python model_training.py
```

Training typically takes 30-60 minutes depending on your hardware. The trained model will be saved as `backend/models/emotion_model.h5`.

## Running the Application

### Start the Backend Server

```bash
cd backend
python app.py
```

The Flask server will start on `http://localhost:5000`

### Start the Frontend Development Server

In a new terminal:

```bash
cd frontend
npm run dev
```

The React app will start on `http://localhost:3000`

### Access the Application

Open your browser and navigate to `http://localhost:3000`

## API Endpoints

### `GET /`
Get API status and available endpoints

### `GET /health`
Health check endpoint

### `POST /api/upload`
Upload an image for emotion detection
- **Content-Type**: `multipart/form-data`
- **Body**: `image` file
- **Response**: JSON with emotion detection results

### `POST /api/webcam`
Process a webcam frame
- **Content-Type**: `application/json`
- **Body**: `{ "image": "base64_encoded_image" }`
- **Response**: JSON with emotion detection results

### `POST /api/predict`
Predict emotion from base64 image
- **Content-Type**: `application/json`
- **Body**: `{ "image": "base64_encoded_image" }`
- **Response**: JSON with emotion detection results

### `GET /api/model-info`
Get information about the loaded model
- **Response**: JSON with model details

## Usage

### Upload Image
1. Click on the "Upload Image" section
2. Drag and drop an image or click to browse
3. Click "Analyze Emotion" to process
4. View detailed results with confidence scores

### Webcam Capture
1. Navigate to the "Webcam Capture" section
2. Click "Enable Webcam" to start your camera
3. Click "Capture Photo" when ready
4. Click "Analyze Emotion" to process
5. View results or retake photo

## Model Architecture

The CNN model consists of:
- **4 Convolutional Blocks** with BatchNormalization and MaxPooling
- **Dropout Layers** for regularization (0.25-0.5)
- **Dense Layers** (512 → 256 → 7 output classes)
- **Data Augmentation** (rotation, shift, flip, zoom)
- **Early Stopping** and Learning Rate Reduction callbacks

### Input
- Grayscale images (48x48 pixels)
- Normalized pixel values (0-1)

### Output
- 7 emotion probabilities (softmax activation)

## Deployment

### Backend Deployment (Railway/Render)

1. Create a `Procfile`:
```
web: gunicorn app:app
```

2. Set environment variables:
```
FLASK_ENV=production
```

3. Deploy to Railway or Render following their documentation

### Frontend Deployment (Vercel)

1. Update `vite.config.js` with production API URL
2. Build the production bundle:
```bash
npm run build
```

3. Deploy to Vercel:
```bash
npm install -g vercel
vercel
```

## Troubleshooting

### Backend Issues

**Model not loading:**
- Ensure `emotion_model.h5` exists in `backend/models/`
- Check file permissions
- Verify TensorFlow installation

**Import errors:**
- Reinstall dependencies: `pip install -r requirements.txt --force-reinstall`
- Check Python version (3.8+)

### Frontend Issues

**API connection errors:**
- Verify backend is running on port 5000
- Check CORS settings in `app.py`
- Update API URL in `frontend/src/utils/api.js`

**Webcam not working:**
- Grant browser camera permissions
- Use HTTPS in production
- Check browser compatibility

## Performance Optimization

- Model typically processes images in 100-500ms
- Face detection handles multiple faces
- Supports images up to 16MB
- Webcam captures at optimal resolution (1280x720)

## Future Enhancements

- [ ] Real-time video emotion tracking
- [ ] Emotion timeline visualization
- [ ] Multi-language support
- [ ] Voice emotion detection
- [ ] User authentication
- [ ] Emotion history dashboard
- [ ] Export results as PDF/CSV

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is open source and available under the MIT License.

## Acknowledgments

- FER2013 dataset creators
- TensorFlow and Keras teams
- OpenCV community
- React and TailwindCSS communities

## Support

For issues, questions, or suggestions, please open an issue on GitHub.

---

**Made with ❤️ using AI & Machine Learning**
