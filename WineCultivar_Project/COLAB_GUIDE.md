# 🍷 Google Colab Guide - Wine Cultivar Model Comparison

## 📋 Overview

This guide explains how to run the Wine Cultivar Model Comparison notebook in Google Colab, comparing three machine learning classifiers:
- **Logistic Regression (LR)**
- **Decision Tree (DT)**
- **Support Vector Machine (SVM)**

---

## 🚀 Quick Start - Using Google Colab

### Method 1: Upload Notebook Directly

1. **Go to Google Colab**
   - Visit: https://colab.research.google.com/

2. **Upload the Notebook**
   - Click "File" → "Upload notebook"
   - Select `Wine_Cultivar_Model_Comparison.ipynb` from your computer
   - OR drag and drop the file

3. **Run All Cells**
   - Click "Runtime" → "Run all"
   - OR press `Ctrl+F9` (Windows/Linux) or `Cmd+F9` (Mac)
   - OR run each cell individually by clicking the play button (▶️) or pressing `Shift+Enter`

### Method 2: Open from GitHub

1. **Push to GitHub** (if not already done)
   ```bash
   git add WineCultivar_Project/Wine_Cultivar_Model_Comparison.ipynb
   git commit -m "Add model comparison notebook"
   git push
   ```

2. **Open in Colab**
   - Go to: https://colab.research.google.com/
   - Click "File" → "Open notebook"
   - Select "GitHub" tab
   - Enter your repository URL
   - Select the notebook file

3. **Run the Notebook**
   - All cells will load automatically
   - Run them sequentially or all at once

---

## 📊 What the Notebook Does

### Step-by-Step Process

1. **Import Libraries**
   - Loads all required packages (sklearn, pandas, numpy, matplotlib, seaborn)

2. **Load Wine Dataset**
   - Uses sklearn's built-in wine dataset
   - 178 samples, 13 features, 3 classes
   - No missing values

3. **Explore Data**
   - Display dataset information
   - Show class distribution
   - Visualize correlations

4. **Preprocess Data**
   - Split into train/test sets (80/20)
   - Apply StandardScaler for feature normalization
   - Prepare data for modeling

5. **Train Three Models**
   - **Logistic Regression**: Linear classifier
   - **Decision Tree**: Non-linear, tree-based classifier
   - **SVM**: Kernel-based classifier (RBF kernel)

6. **Evaluate Performance**
   - Calculate accuracy, precision, recall, F1-score
   - Generate classification reports
   - Create confusion matrices

7. **Compare Models**
   - Side-by-side performance comparison
   - Visual comparisons with charts
   - Identify best performing model

8. **Generate Insights**
   - Key observations
   - Recommendations
   - Summary tables

---

## 📈 Expected Results

Based on the wine dataset, you should see:

### Model Performance (Typical Results)

| Model | Accuracy | Precision | Recall | F1-Score |
|-------|----------|-----------|--------|----------|
| **Logistic Regression** | ~97% | ~97% | ~97% | ~97% |
| **Decision Tree** | ~94% | ~95% | ~94% | ~94% |
| **SVM** | ~97% | ~97% | ~97% | ~97% |

### Key Findings

✅ **All models achieve >90% accuracy**
- Wine dataset is well-suited for classification
- Clear separation between cultivar classes

✅ **Logistic Regression & SVM tie for best performance**
- Both achieve ~97% accuracy
- Minimal misclassifications

✅ **Decision Tree slightly lower but still excellent**
- ~94% accuracy
- More interpretable than other models

✅ **Feature scaling is critical**
- StandardScaler significantly improves performance
- Essential for Logistic Regression and SVM

---

## 🔬 Running Cell by Cell

### Recommended Execution Order

Run the cells in sequence from top to bottom:

#### 1. Setup (Cells 1-2)
```python
# Cell 1: Import libraries
# Cell 2: Load dataset
```
**Expected**: Libraries loaded, dataset loaded successfully

#### 2. Data Exploration (Cells 3-8)
```python
# Cells 3-8: Explore and visualize data
```
**Expected**: Dataset info, statistics, visualizations

#### 3. Preprocessing (Cells 9-11)
```python
# Cells 9-11: Split and scale data
```
**Expected**: Train/test sets created, features scaled

#### 4. Model 1 - Logistic Regression (Cells 12-14)
```python
# Train, evaluate, visualize LR
```
**Expected**: ~97% accuracy, classification report, confusion matrix

#### 5. Model 2 - Decision Tree (Cells 15-17)
```python
# Train, evaluate, visualize DT
```
**Expected**: ~94% accuracy, classification report, confusion matrix

#### 6. Model 3 - SVM (Cells 18-20)
```python
# Train, evaluate, visualize SVM
```
**Expected**: ~97% accuracy, classification report, confusion matrix

#### 7. Comparison (Cells 21-24)
```python
# Compare all models
```
**Expected**: Comparison tables, charts, insights

---

## 🎯 Understanding the Results

### Classification Report Explained

```
              precision    recall  f1-score   support

  Cultivar 0       1.00      1.00      1.00        12
  Cultivar 1       0.93      1.00      0.97        14
  Cultivar 2       1.00      0.90      0.95        10

    accuracy                           0.97        36
   macro avg       0.98      0.97      0.97        36
weighted avg       0.97      0.97      0.97        36
```

- **Precision**: Of predictions for a class, how many were correct?
- **Recall**: Of actual samples in a class, how many were found?
- **F1-Score**: Harmonic mean of precision and recall
- **Support**: Number of actual samples in each class

### Confusion Matrix Explained

```
Predicted:  C0  C1  C2
Actual C0:  12   0   0   (All 12 correctly predicted)
Actual C1:   0  14   0   (All 14 correctly predicted)
Actual C2:   0   1   9   (9 correct, 1 misclassified as C1)
```

- Diagonal values = correct predictions
- Off-diagonal values = misclassifications

---

## 🛠️ Troubleshooting

### Issue: Module not found
**Solution**: Colab has all required packages pre-installed. If error occurs, run:
```python
!pip install scikit-learn pandas numpy matplotlib seaborn
```

### Issue: Runtime disconnected
**Solution**:
- Click "Runtime" → "Reconnect"
- Re-run cells from the beginning

### Issue: Graphics not displaying
**Solution**:
- Colab supports matplotlib by default
- Try: `%matplotlib inline` in a cell before plotting

### Issue: Cells running slow
**Solution**:
- Normal for first run (cold start)
- Subsequent runs will be faster
- Consider using GPU: "Runtime" → "Change runtime type" → "GPU" (not necessary for this notebook)

---

## 💡 Tips for Google Colab

### Keyboard Shortcuts
- `Shift + Enter`: Run cell and move to next
- `Ctrl + Enter`: Run cell and stay
- `Ctrl + M B`: Insert cell below
- `Ctrl + M D`: Delete cell

### Saving Your Work
- Colab auto-saves to Google Drive
- File → Save a copy in Drive
- File → Download → .ipynb

### Sharing Results
- File → Share
- Generate shareable link
- Anyone with link can view (not edit)

---

## 📊 Alternative: Run Python Script

If you prefer running a Python script instead of Jupyter notebook:

```python
# In a Colab cell, run:
!wget https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO/main/WineCultivar_Project/model_comparison.py
!python model_comparison.py
```

Or upload `model_comparison.py` and run:
```python
!python model_comparison.py
```

---

## 📚 Dataset Information

### Wine Dataset Details

- **Source**: UCI Machine Learning Repository / sklearn
- **Samples**: 178 wine samples
- **Features**: 13 chemical properties
- **Classes**: 3 wine cultivars (varieties)
- **Task**: Multi-class classification

### Features Include:
1. Alcohol
2. Malic acid
3. Ash
4. Alkalinity of ash
5. Magnesium
6. Total phenols
7. Flavanoids
8. Nonflavanoid phenols
9. Proanthocyanins
10. Color intensity
11. Hue
12. OD280/OD315 of diluted wines
13. Proline

### Target Variable:
- **Cultivar**: 0, 1, or 2 (three different wine varieties)

---

## 🎓 Learning Objectives

After completing this notebook, you will understand:

✅ How to load and explore datasets in sklearn
✅ Importance of data preprocessing and feature scaling
✅ How to train multiple classification models
✅ How to evaluate model performance with multiple metrics
✅ How to compare models and select the best one
✅ How to interpret classification reports and confusion matrices

---

## 📝 Assignment Submission

If using this for coursework:

1. ✅ Run all cells in Google Colab
2. ✅ Review all outputs and visualizations
3. ✅ Take screenshots of key results
4. ✅ Download notebook: File → Download → .ipynb
5. ✅ Save outputs: File → Print → Save as PDF
6. ✅ Include in submission folder

---

## 🔗 Additional Resources

- [sklearn Wine Dataset Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_wine.html)
- [Logistic Regression](https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression)
- [Decision Trees](https://scikit-learn.org/stable/modules/tree.html)
- [Support Vector Machines](https://scikit-learn.org/stable/modules/svm.html)
- [Google Colab Documentation](https://colab.research.google.com/notebooks/intro.ipynb)

---

## ✅ Quick Checklist

Before running:
- [ ] Google Colab account (free Gmail account)
- [ ] Notebook file downloaded or GitHub link ready
- [ ] Internet connection

During execution:
- [ ] Run cells sequentially
- [ ] Check outputs after each cell
- [ ] Note any errors or warnings

After completion:
- [ ] Review all classification reports
- [ ] Compare model performances
- [ ] Understand which model performed best
- [ ] Save results (notebook + screenshots)

---

**Ready to start?** Upload the notebook to Google Colab and begin! 🚀

**Questions?** Check the troubleshooting section or refer to sklearn documentation.

---

**Good luck with your wine cultivar prediction analysis! 🍷**
