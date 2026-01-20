"""
Wine Cultivar Origin Prediction System - Model Building Script
This script builds and saves the machine learning model
"""

import pandas as pd
import numpy as np
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib

def main():
    print("=" * 60)
    print("Wine Cultivar Origin Prediction System - Model Building")
    print("=" * 60)

    # Load wine dataset
    print("\n1. Loading Wine Dataset...")
    wine_data = load_wine()
    df = pd.DataFrame(data=wine_data.data, columns=wine_data.feature_names)
    df['cultivar'] = wine_data.target
    print(f"   Dataset loaded: {df.shape[0]} samples, {df.shape[1]} columns")

    # Check for missing values
    print("\n2. Checking for missing values...")
    missing_values = df.isnull().sum().sum()
    print(f"   Missing values: {missing_values}")

    # Feature Selection
    print("\n3. Selecting features...")
    selected_features = [
        'alcohol',
        'malic_acid',
        'total_phenols',
        'flavanoids',
        'color_intensity',
        'proline'
    ]

    X = df[selected_features]
    y = df['cultivar']
    print(f"   Selected {len(selected_features)} features")
    print(f"   Features: {', '.join(selected_features)}")

    # Split data
    print("\n4. Splitting data into train and test sets...")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    print(f"   Training samples: {X_train.shape[0]}")
    print(f"   Testing samples: {X_test.shape[0]}")

    # Feature Scaling
    print("\n5. Applying feature scaling (StandardScaler)...")
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    print("   Feature scaling completed")

    # Model Training
    print("\n6. Training Random Forest Classifier...")
    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42,
        max_depth=10,
        min_samples_split=2,
        min_samples_leaf=1
    )
    model.fit(X_train_scaled, y_train)
    print("   Model training completed")

    # Model Evaluation
    print("\n7. Evaluating model performance...")
    y_pred = model.predict(X_test_scaled)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"   Accuracy: {accuracy * 100:.2f}%")

    print("\n   Classification Report:")
    print(classification_report(y_test, y_pred,
                                target_names=['Cultivar 0', 'Cultivar 1', 'Cultivar 2']))

    print("\n   Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))

    # Feature Importance
    print("\n   Feature Importance:")
    for feature, importance in zip(selected_features, model.feature_importances_):
        print(f"   - {feature}: {importance:.4f}")

    # Save Model
    print("\n8. Saving model and preprocessing objects...")
    joblib.dump(model, 'wine_cultivar_model.pkl')
    print("   ✓ Model saved as 'wine_cultivar_model.pkl'")

    joblib.dump(scaler, 'scaler.pkl')
    print("   ✓ Scaler saved as 'scaler.pkl'")

    joblib.dump(selected_features, 'selected_features.pkl')
    print("   ✓ Feature names saved as 'selected_features.pkl'")

    # Test loaded model
    print("\n9. Testing saved model...")
    loaded_model = joblib.load('wine_cultivar_model.pkl')
    loaded_scaler = joblib.load('scaler.pkl')

    sample_input = X_test.iloc[0:1]
    sample_scaled = loaded_scaler.transform(sample_input)
    prediction = loaded_model.predict(sample_scaled)

    print(f"   Sample prediction: Cultivar {prediction[0]}")
    print(f"   Actual value: Cultivar {y_test.iloc[0]}")
    print(f"   Match: {'✓' if prediction[0] == y_test.iloc[0] else '✗'}")

    print("\n" + "=" * 60)
    print("Model building completed successfully!")
    print("=" * 60)

if __name__ == "__main__":
    main()
