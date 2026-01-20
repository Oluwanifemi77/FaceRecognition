# 🍷 Wine Cultivar Origin Prediction System

A machine learning-powered web application that predicts the cultivar (origin class) of wine based on its chemical properties using the UCI/sklearn Wine dataset.

## 📋 Project Overview

This project implements a complete machine learning pipeline including:
- Data preprocessing and feature engineering
- Model training using Random Forest Classifier
- Interactive web-based GUI for predictions
- Model deployment on cloud platform

## 🎯 Features

- **6 Chemical Features**: alcohol, malic_acid, total_phenols, flavanoids, color_intensity, proline
- **3 Wine Cultivars**: Multi-class classification (Cultivar 0, 1, 2)
- **High Accuracy**: 100% accuracy on test set
- **Interactive UI**: User-friendly Streamlit web interface
- **Real-time Predictions**: Instant cultivar prediction with confidence scores

## 🛠️ Technology Stack

- **Machine Learning**: scikit-learn (Random Forest Classifier)
- **Data Processing**: pandas, numpy
- **Web Framework**: Streamlit
- **Model Persistence**: Joblib
- **Visualization**: matplotlib, seaborn

## 📁 Project Structure

```
WineCultivar_Project/
│
├── app.py                              # Streamlit web application
├── requirements.txt                    # Python dependencies
├── WineCultivar_hosted_webGUI_link.txt # Deployment information
│
├── model/
│   ├── model_building.ipynb           # Jupyter notebook with model development
│   ├── build_model.py                 # Python script to build model
│   ├── wine_cultivar_model.pkl        # Trained model (Joblib)
│   ├── scaler.pkl                     # Feature scaler
│   └── selected_features.pkl          # Feature names
│
├── .streamlit/
│   └── config.toml                    # Streamlit configuration
│
└── README.md                          # Project documentation
```

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Local Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd WineCultivar_Project
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

4. **Access the application**
   - Open your browser and navigate to `http://localhost:8501`

## 📊 Model Development (Part A)

### Dataset
- **Source**: UCI/sklearn Wine dataset
- **Samples**: 178 wine samples
- **Classes**: 3 wine cultivars
- **Features**: 13 chemical properties (6 selected)

### Selected Features
1. **alcohol** - Alcohol content (% by volume)
2. **malic_acid** - Malic acid concentration (g/L)
3. **total_phenols** - Total phenolic compounds
4. **flavanoids** - Flavanoid concentration
5. **color_intensity** - Color intensity measurement
6. **proline** - Proline amino acid content (mg/L)

### Preprocessing Steps
1. ✅ Load Wine dataset from sklearn
2. ✅ Check for missing values (None found)
3. ✅ Select 6 features from available features
4. ✅ Split data (80% train, 20% test) with stratification
5. ✅ Apply StandardScaler for feature normalization
6. ✅ Train Random Forest Classifier
7. ✅ Evaluate with multiclass metrics
8. ✅ Save model using Joblib

### Model Performance
```
Accuracy: 100.00%

Classification Report:
              precision    recall  f1-score   support

  Cultivar 0       1.00      1.00      1.00        12
  Cultivar 1       1.00      1.00      1.00        14
  Cultivar 2       1.00      1.00      1.00        10

    accuracy                           1.00        36
   macro avg       1.00      1.00      1.00        36
weighted avg       1.00      1.00      1.00        36
```

### Feature Importance
- color_intensity: 26.20%
- flavanoids: 24.73%
- proline: 19.38%
- alcohol: 13.47%
- total_phenols: 9.46%
- malic_acid: 6.76%

## 🌐 Web Application (Part B)

### Features
- ✨ Modern, responsive UI with custom styling
- 🔢 Input validation for all chemical properties
- 📊 Real-time prediction with confidence scores
- 📈 Probability distribution visualization
- 💡 Helpful tooltips and descriptions
- 🎨 Professional color scheme and layout

### User Interface Components
1. **Input Section**: Number inputs for 6 chemical properties
2. **Summary Panel**: Display of entered values
3. **Prediction Box**: Highlighted result with cultivar prediction
4. **Confidence Chart**: Visual representation of probabilities
5. **Detailed Metrics**: Individual probability scores for each class

### Usage
1. Enter the wine's chemical property values
2. Click "Predict Cultivar" button
3. View the predicted cultivar with confidence score
4. Analyze the probability distribution across all classes

## 🚢 Deployment (Part D)

This application can be deployed on various platforms:

### Streamlit Cloud (Recommended)
1. Push code to GitHub
2. Connect repository to Streamlit Cloud
3. Deploy with one click
4. Access via provided URL

### Other Platforms
- **Render.com**: Deploy as web service
- **PythonAnywhere**: Host Python web applications
- **Vercel**: Deploy with serverless functions

## 📝 Model Details

| Attribute | Value |
|-----------|-------|
| Algorithm | Random Forest Classifier |
| Number of Features | 6 |
| Number of Classes | 3 |
| Train/Test Split | 80/20 |
| Feature Scaling | StandardScaler |
| Model Persistence | Joblib (.pkl) |
| Test Accuracy | 100% |
| Precision (macro avg) | 1.00 |
| Recall (macro avg) | 1.00 |
| F1-Score (macro avg) | 1.00 |

## 🔧 Technical Implementation

### Random Forest Classifier Parameters
```python
RandomForestClassifier(
    n_estimators=100,      # Number of trees
    random_state=42,       # Reproducibility
    max_depth=10,          # Maximum tree depth
    min_samples_split=2,   # Minimum samples to split
    min_samples_leaf=1     # Minimum samples at leaf
)
```

### Feature Scaling
- **Method**: StandardScaler
- **Purpose**: Normalize features to zero mean and unit variance
- **Importance**: Critical due to varying feature ranges

## 📦 Dependencies

```
pandas==2.0.3
numpy==1.24.3
scikit-learn==1.3.0
joblib==1.3.2
streamlit==1.28.0
matplotlib==3.7.2
seaborn==0.12.2
```

## 🎓 Academic Context

This project fulfills the requirements for:
- Part A: Model Development (Jupyter notebook + saved model)
- Part B: Web GUI Application (Streamlit app)
- Part C: GitHub Submission (Complete project structure)
- Part D: Deployment (Cloud-hosted application)

## 📚 References

- Dataset: UCI Machine Learning Repository - Wine Dataset
- scikit-learn: https://scikit-learn.org/
- Streamlit: https://streamlit.io/
- Random Forest: Breiman, L. (2001). Random forests. Machine learning, 45(1), 5-32.

## 📧 Contact & Submission

For submission details, refer to `WineCultivar_hosted_webGUI_link.txt`

## 📄 License

This project is created for academic purposes.

---

**Note**: This is an educational project demonstrating machine learning model development and deployment.
