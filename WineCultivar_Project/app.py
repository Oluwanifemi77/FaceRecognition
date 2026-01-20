"""
Wine Cultivar Origin Prediction System
Part B - Web GUI Application using Streamlit
"""

import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

# Page configuration
st.set_page_config(
    page_title="Wine Cultivar Prediction",
    page_icon="🍷",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
        background-color: #8B0000;
        color: white;
        font-weight: bold;
        border-radius: 10px;
        padding: 0.75rem;
        font-size: 18px;
    }
    .stButton>button:hover {
        background-color: #A52A2A;
    }
    .prediction-box {
        padding: 2rem;
        border-radius: 10px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        text-align: center;
        margin-top: 2rem;
        box-shadow: 0 10px 20px rgba(0,0,0,0.2);
    }
    .feature-description {
        font-size: 14px;
        color: #666;
        font-style: italic;
    }
    </style>
    """, unsafe_allow_html=True)

# Load model and preprocessing objects
@st.cache_resource
def load_model_artifacts():
    """Load the trained model, scaler, and feature names"""
    try:
        model_path = os.path.join('model', 'wine_cultivar_model.pkl')
        scaler_path = os.path.join('model', 'scaler.pkl')
        features_path = os.path.join('model', 'selected_features.pkl')

        model = joblib.load(model_path)
        scaler = joblib.load(scaler_path)
        features = joblib.load(features_path)

        return model, scaler, features
    except Exception as e:
        st.error(f"Error loading model artifacts: {e}")
        st.stop()

# Load model
model, scaler, feature_names = load_model_artifacts()

# Cultivar information
cultivar_info = {
    0: {
        "name": "Cultivar 0 (Class 1)",
        "description": "First wine cultivar type with distinct chemical properties",
        "emoji": "🍇"
    },
    1: {
        "name": "Cultivar 1 (Class 2)",
        "description": "Second wine cultivar type with unique characteristics",
        "emoji": "🍷"
    },
    2: {
        "name": "Cultivar 2 (Class 3)",
        "description": "Third wine cultivar type with specific chemical composition",
        "emoji": "🥂"
    }
}

# Feature descriptions
feature_descriptions = {
    'alcohol': 'Alcohol content (% by volume)',
    'malic_acid': 'Malic acid concentration (g/L)',
    'total_phenols': 'Total phenolic compounds',
    'flavanoids': 'Flavanoid concentration',
    'color_intensity': 'Color intensity measurement',
    'proline': 'Proline amino acid content (mg/L)'
}

# Feature ranges for validation
feature_ranges = {
    'alcohol': (11.0, 15.0),
    'malic_acid': (0.5, 6.0),
    'total_phenols': (0.5, 4.0),
    'flavanoids': (0.0, 6.0),
    'color_intensity': (1.0, 13.0),
    'proline': (200, 1700)
}

# Title and header
st.title("🍷 Wine Cultivar Origin Prediction System")
st.markdown("### Predict wine cultivar based on chemical properties")
st.markdown("---")

# Sidebar with information
with st.sidebar:
    st.header("📊 About This System")
    st.markdown("""
    This machine learning system predicts the **cultivar (origin class)** of wine
    based on its chemical properties.

    **Model Details:**
    - Algorithm: Random Forest Classifier
    - Features: 6 chemical properties
    - Accuracy: 100% on test set
    - Classes: 3 wine cultivars

    **Instructions:**
    1. Enter the chemical property values
    2. Click 'Predict Cultivar'
    3. View the prediction result
    """)

    st.markdown("---")
    st.markdown("**Selected Features:**")
    for feature in feature_names:
        st.markdown(f"• {feature}")

    st.markdown("---")
    st.info("💡 Use the sliders or input boxes to enter wine properties")

# Main content area
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("🔬 Enter Wine Chemical Properties")

    # Create input fields for all features
    input_data = {}

    # Organize inputs in two columns
    input_col1, input_col2 = st.columns(2)

    with input_col1:
        input_data['alcohol'] = st.number_input(
            "Alcohol (%)",
            min_value=float(feature_ranges['alcohol'][0]),
            max_value=float(feature_ranges['alcohol'][1]),
            value=13.0,
            step=0.1,
            help=feature_descriptions['alcohol']
        )

        input_data['malic_acid'] = st.number_input(
            "Malic Acid (g/L)",
            min_value=float(feature_ranges['malic_acid'][0]),
            max_value=float(feature_ranges['malic_acid'][1]),
            value=2.5,
            step=0.1,
            help=feature_descriptions['malic_acid']
        )

        input_data['total_phenols'] = st.number_input(
            "Total Phenols",
            min_value=float(feature_ranges['total_phenols'][0]),
            max_value=float(feature_ranges['total_phenols'][1]),
            value=2.0,
            step=0.1,
            help=feature_descriptions['total_phenols']
        )

    with input_col2:
        input_data['flavanoids'] = st.number_input(
            "Flavanoids",
            min_value=float(feature_ranges['flavanoids'][0]),
            max_value=float(feature_ranges['flavanoids'][1]),
            value=2.5,
            step=0.1,
            help=feature_descriptions['flavanoids']
        )

        input_data['color_intensity'] = st.number_input(
            "Color Intensity",
            min_value=float(feature_ranges['color_intensity'][0]),
            max_value=float(feature_ranges['color_intensity'][1]),
            value=5.0,
            step=0.1,
            help=feature_descriptions['color_intensity']
        )

        input_data['proline'] = st.number_input(
            "Proline (mg/L)",
            min_value=float(feature_ranges['proline'][0]),
            max_value=float(feature_ranges['proline'][1]),
            value=1000.0,
            step=10.0,
            help=feature_descriptions['proline']
        )

    st.markdown("---")

    # Predict button
    predict_button = st.button("🔮 Predict Cultivar", use_container_width=True)

with col2:
    st.subheader("📈 Input Summary")

    # Display input summary
    summary_df = pd.DataFrame({
        'Feature': list(input_data.keys()),
        'Value': list(input_data.values())
    })
    st.dataframe(summary_df, use_container_width=True, hide_index=True)

# Prediction section
if predict_button:
    try:
        # Prepare input data
        input_df = pd.DataFrame([input_data])

        # Ensure correct feature order
        input_df = input_df[feature_names]

        # Scale the input
        input_scaled = scaler.transform(input_df)

        # Make prediction
        prediction = model.predict(input_scaled)[0]
        prediction_proba = model.predict_proba(input_scaled)[0]

        # Display prediction
        st.markdown("---")
        st.subheader("🎯 Prediction Result")

        # Main prediction display
        cultivar = cultivar_info[prediction]
        st.markdown(f"""
        <div class="prediction-box">
            <h1 style="margin: 0;">{cultivar['emoji']}</h1>
            <h2 style="margin: 10px 0;">{cultivar['name']}</h2>
            <p style="margin: 5px 0; font-size: 16px;">{cultivar['description']}</p>
            <h3 style="margin-top: 15px;">Confidence: {prediction_proba[prediction]*100:.2f}%</h3>
        </div>
        """, unsafe_allow_html=True)

        # Probability distribution
        st.markdown("### 📊 Confidence Distribution")

        prob_df = pd.DataFrame({
            'Cultivar': [f"{cultivar_info[i]['emoji']} {cultivar_info[i]['name']}"
                        for i in range(len(prediction_proba))],
            'Probability': prediction_proba * 100
        })

        st.bar_chart(prob_df.set_index('Cultivar'), use_container_width=True)

        # Detailed probabilities
        st.markdown("### 🔢 Detailed Probabilities")
        for i, prob in enumerate(prediction_proba):
            st.metric(
                label=f"{cultivar_info[i]['emoji']} {cultivar_info[i]['name']}",
                value=f"{prob*100:.2f}%"
            )

    except Exception as e:
        st.error(f"Error making prediction: {e}")
        st.exception(e)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 1rem;">
    <p>🍷 Wine Cultivar Origin Prediction System | Powered by Random Forest Classifier</p>
    <p>Dataset: UCI/sklearn Wine Dataset | Model Persistence: Joblib</p>
</div>
""", unsafe_allow_html=True)
