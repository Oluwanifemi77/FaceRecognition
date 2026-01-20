# 🚀 Deployment Guide - Wine Cultivar Prediction System

This guide provides step-by-step instructions for deploying the Wine Cultivar Prediction System to various cloud platforms.

## 📋 Pre-Deployment Checklist

Before deploying, ensure:
- ✅ All files are committed to GitHub
- ✅ requirements.txt is up to date
- ✅ Model files (.pkl) are present in the model/ directory
- ✅ app.py is in the root directory

## 🎯 Recommended: Streamlit Cloud Deployment

Streamlit Cloud is the easiest and recommended platform for deploying Streamlit applications.

### Step 1: Prepare GitHub Repository

1. **Push your code to GitHub**
   ```bash
   git add .
   git commit -m "Add Wine Cultivar Prediction System"
   git push origin main
   ```

2. **Ensure repository is public** (or you have Streamlit Cloud paid plan for private repos)

### Step 2: Deploy to Streamlit Cloud

1. **Go to Streamlit Cloud**
   - Visit: https://share.streamlit.io/
   - Sign in with your GitHub account

2. **Create New App**
   - Click "New app" button
   - Select your GitHub repository
   - Choose branch (e.g., main or master)
   - Set main file path: `WineCultivar_Project/app.py`
   - Set Python version: 3.9 or 3.10 (recommended)

3. **Configure Advanced Settings** (Optional)
   - Click "Advanced settings"
   - Set custom subdomain if desired
   - Configure secrets if needed (not required for this project)

4. **Deploy**
   - Click "Deploy!" button
   - Wait 2-5 minutes for deployment
   - Your app will be live at: `https://[your-app-name].streamlit.app`

5. **Update Submission File**
   - Copy the live URL
   - Update `WineCultivar_hosted_webGUI_link.txt` with the URL
   - Commit and push the updated file

### Streamlit Cloud Requirements
- Free tier includes:
  - Unlimited public apps
  - 1 GB RAM per app
  - Community support
  - Automatic updates from GitHub

---

## 🔧 Alternative: Render.com Deployment

Render provides free hosting for web applications.

### Step 1: Prepare for Render

1. **Add start script to repository**
   Create a file named `start.sh`:
   ```bash
   #!/bin/bash
   streamlit run app.py --server.port $PORT --server.address 0.0.0.0
   ```

2. **Make script executable**
   ```bash
   chmod +x start.sh
   ```

### Step 2: Deploy to Render

1. **Go to Render Dashboard**
   - Visit: https://render.com/
   - Sign up or log in

2. **Create New Web Service**
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Select the repository containing your project

3. **Configure Service**
   - Name: `wine-cultivar-prediction`
   - Environment: `Python 3`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `streamlit run app.py --server.port $PORT --server.address 0.0.0.0`
   - Instance Type: Free

4. **Environment Variables** (if needed)
   - Add any required environment variables
   - Not required for this basic setup

5. **Deploy**
   - Click "Create Web Service"
   - Wait for build and deployment (5-10 minutes)
   - Your app will be live at: `https://wine-cultivar-prediction.onrender.com`

---

## 🐍 Alternative: PythonAnywhere Deployment

PythonAnywhere offers free hosting for Python web applications.

### Step 1: Setup PythonAnywhere Account

1. **Create Account**
   - Visit: https://www.pythonanywhere.com/
   - Sign up for free "Beginner" account

2. **Upload Code**
   - Use "Files" tab to upload your project files
   - Or clone from GitHub using Bash console

### Step 2: Setup Virtual Environment

1. **Open Bash Console**
   ```bash
   mkvirtualenv --python=/usr/bin/python3.9 wine_env
   pip install streamlit pandas numpy scikit-learn joblib matplotlib seaborn
   ```

2. **Test Application**
   ```bash
   cd ~/WineCultivar_Project
   streamlit run app.py
   ```

### Step 3: Configure Web App

1. **Create New Web App**
   - Go to "Web" tab
   - Click "Add a new web app"
   - Choose manual configuration
   - Select Python 3.9

2. **Configure WSGI**
   - Note: Streamlit doesn't work well with PythonAnywhere's default setup
   - Consider using Flask wrapper or choose different platform

**Recommendation**: Use Streamlit Cloud or Render for easier Streamlit deployment.

---

## ☁️ Alternative: Vercel Deployment

Vercel can host Streamlit apps with some configuration.

### Note
Vercel is optimized for Next.js and static sites. For Streamlit apps, we recommend using Streamlit Cloud or Render instead.

---

## 🧪 Testing Deployed Application

After deployment, test your application:

### 1. Basic Functionality Test
- ✅ Application loads without errors
- ✅ All input fields are visible and functional
- ✅ Predict button works
- ✅ Predictions are displayed correctly

### 2. Sample Test Cases

**Test Case 1: High Alcohol Wine**
- alcohol: 14.5
- malic_acid: 1.5
- total_phenols: 2.8
- flavanoids: 3.5
- color_intensity: 7.0
- proline: 1200

**Test Case 2: Medium Intensity Wine**
- alcohol: 12.5
- malic_acid: 3.0
- total_phenols: 2.0
- flavanoids: 2.0
- color_intensity: 5.0
- proline: 800

**Test Case 3: Low Alcohol Wine**
- alcohol: 11.5
- malic_acid: 5.0
- total_phenols: 1.5
- flavanoids: 1.0
- color_intensity: 3.0
- proline: 500

### 3. Performance Check
- Response time should be < 3 seconds
- No memory errors or crashes
- Confidence scores displayed correctly

---

## 📝 Post-Deployment Steps

1. **Update Submission File**
   ```
   Edit: WineCultivar_hosted_webGUI_link.txt
   Add: Your deployed application URL
   ```

2. **Test Application**
   - Verify all features work
   - Test with sample inputs
   - Check predictions are correct

3. **Document URL**
   - Save the live URL
   - Include in your GitHub README
   - Update submission documentation

4. **Final Commit**
   ```bash
   git add WineCultivar_hosted_webGUI_link.txt README.md
   git commit -m "Update deployment URL"
   git push origin main
   ```

---

## 🔍 Troubleshooting

### Issue: Model files not loading
**Solution**: Ensure .pkl files are committed to GitHub and paths are correct in app.py

### Issue: Module not found errors
**Solution**: Verify requirements.txt includes all dependencies and versions are compatible

### Issue: Application crashes on startup
**Solution**: Check Streamlit logs, verify Python version compatibility (3.8-3.10)

### Issue: Predictions not working
**Solution**: Verify model files are in correct location relative to app.py

### Issue: Slow loading times
**Solution**: Consider reducing model size or optimizing feature preprocessing

---

## 📊 Monitoring and Maintenance

### Streamlit Cloud
- View logs in Streamlit Cloud dashboard
- Monitor app performance
- Check resource usage

### Render
- View logs in Render dashboard
- Set up health checks
- Monitor deployment status

---

## 🎓 Submission Checklist

Before submitting, verify:

- ✅ Application is deployed and accessible via URL
- ✅ All features work correctly
- ✅ URL is updated in WineCultivar_hosted_webGUI_link.txt
- ✅ GitHub repository is organized and complete
- ✅ README.md includes deployment information
- ✅ Application tested with multiple test cases
- ✅ Screenshots/demo prepared (optional)

---

## 📚 Additional Resources

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Streamlit Cloud Docs](https://docs.streamlit.io/streamlit-community-cloud)
- [Render Documentation](https://render.com/docs)
- [Python Anywhere Help](https://help.pythonanywhere.com/)

---

**Questions?** Check the platform documentation or contact support.

**Deadline**: Thursday, January 21, 2026, 11:59 PM

Good luck with your deployment! 🚀
