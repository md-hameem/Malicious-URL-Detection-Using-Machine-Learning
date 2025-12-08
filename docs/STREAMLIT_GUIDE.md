# 🚀 Streamlit Web Application Guide

## Overview

The Streamlit application provides an interactive web interface for testing the malicious URL detection system. Users can enter URLs and get instant predictions with detailed analysis.

## Features

- **🔍 Real-time URL Analysis** - Instant predictions with confidence scores
- **📊 Visual Results** - Color-coded risk levels and probability charts
- **🔬 Feature Breakdown** - Detailed feature extraction and analysis
- **💡 Security Recommendations** - Actionable advice based on predictions
- **📱 Responsive Design** - Modern UI with gradient styling
- **📝 Example URLs** - Quick test with pre-filled examples

## Installation

1. **Install dependencies:**
   ```bash
   pip install streamlit
   ```

2. **Ensure models are trained:**
   Run the Jupyter notebook first to generate:
   - `models/final_random_forest_model.pkl`
   - `models/label_encoder.pkl`

## Running the Application

### Method 1: Command Line
```bash
streamlit run app.py
```

### Method 2: With Custom Port
```bash
streamlit run app.py --server.port 8080
```

### Method 3: With Browser Auto-open Disabled
```bash
streamlit run app.py --server.headless true
```

## Accessing the Application

After running the command, the app will be available at:
- **Local URL:** http://localhost:8501
- **Network URL:** http://YOUR_IP:8501

The terminal will display both URLs. Open either in your browser.

## Usage

### Basic Usage
1. **Enter URL** in the text input field
2. Click **"🚀 Analyze URL"** button
3. View the prediction results

### Example URLs
Use the preset example buttons for quick testing:
- **Safe URL** - https://www.google.com
- **Suspicious** - http://bit.ly/suspicious123
- **Test URL** - http://example-login-bank.com

### Understanding Results

#### Prediction Display
- **✅ SAFE** (Green) - Benign URL, low risk
- **⚠️ PHISHING** (Red) - Phishing attempt, high risk
- **☠️ MALWARE** (Dark Red) - Malware distribution, critical risk
- **🚨 DEFACEMENT** (Orange) - Defaced website, high risk

#### Metrics Shown
- **Classification** - The predicted category
- **Confidence Score** - Model's certainty (0-100%)
- **Risk Level** - Low/High/Critical assessment

#### Feature Analysis
Expand "🔬 Detailed Feature Analysis" to see:
- **Basic Features** - URL length, character counts
- **Security Features** - HTTPS, IP address, URL shortening
- **Structure Features** - Directory count, TLD length
- **All Features Table** - Complete feature breakdown

## Configuration

### Customizing the App

Edit `app.py` to customize:

```python
# Page configuration
st.set_page_config(
    page_title="Your Title",
    page_icon="🔒",
    layout="wide"  # or "centered"
)
```

### Styling

The app uses custom CSS for styling. Modify the CSS in the `st.markdown()` section:

```python
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    /* Add your custom styles */
    </style>
""", unsafe_allow_html=True)
```

## Troubleshooting

### Issue: Models not found
**Error:** "Failed to load models"

**Solution:**
1. Ensure you've run the Jupyter notebook
2. Check that `models/` directory exists
3. Verify these files exist:
   - `models/final_random_forest_model.pkl`
   - `models/label_encoder.pkl`

### Issue: Port already in use
**Error:** "Address already in use"

**Solution:**
```bash
streamlit run app.py --server.port 8502
```

### Issue: Import errors
**Error:** "ModuleNotFoundError"

**Solution:**
```bash
pip install -r requirements.txt
```

### Issue: TLD extraction fails
**Error:** TLD-related errors

**Solution:**
The app handles this gracefully. TLD length will be 0 if extraction fails.

## Features Explained

### 1. URL Input Section
- Main text input for URL entry
- Validation happens on button click
- Supports http:// and https:// protocols

### 2. Analysis Results
- **Verdict Display** - Large, color-coded result
- **Confidence Metrics** - Three-column metric display
- **Probability Chart** - Bar chart showing all class probabilities

### 3. Feature Analysis (Expandable)
Detailed breakdown of 30+ extracted features:
- Lexical features (length, characters)
- Security indicators (HTTPS, IP, shortening)
- Structural features (directories, TLD)
- Special character counts

### 4. Recommendations
Context-aware security advice:
- Safe URLs: General precautions
- Malicious URLs: Specific warnings and actions

### 5. Sidebar Information
- About the model
- Usage instructions
- Developer information

## API Endpoints (Future)

Currently, the app runs as a standalone web interface. For API access, consider deploying with:
- **Streamlit Cloud** - Free hosting
- **Docker** - Containerized deployment
- **Heroku** - Cloud platform

## Performance

- **Response Time:** < 1 second per URL
- **Concurrent Users:** Depends on hosting
- **Model Loading:** Cached after first load

## Security Considerations

⚠️ **Important:**
- This is a detection tool, not a guarantee
- Always exercise caution with unknown URLs
- Use in conjunction with other security measures
- Don't rely solely on automated detection

## Deployment Options

### Option 1: Streamlit Cloud (Recommended)
1. Push code to GitHub
2. Connect to Streamlit Cloud
3. Deploy with one click
4. Free hosting for public apps

### Option 2: Local Network
```bash
streamlit run app.py --server.address 0.0.0.0
```
Access from other devices on your network.

### Option 3: Docker
Create a `Dockerfile`:
```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8501
CMD ["streamlit", "run", "app.py"]
```

## Best Practices

1. **Always test locally first** before deployment
2. **Keep models updated** by retraining periodically
3. **Monitor performance** and log predictions
4. **Set up alerts** for high-risk detections
5. **Regular backups** of model files

## Support

For issues or questions:
- Check the main README.md
- Review error messages in terminal
- Ensure all dependencies are installed
- Verify model files exist

## Next Steps

After getting familiar with the app:
1. Train additional models in the notebook
2. Deploy to Streamlit Cloud for public access
3. Integrate with email filters or browser extensions
4. Add user authentication for enterprise use
5. Implement logging and analytics

---

**🎉 Enjoy using the Malicious URL Detection System!**

For more information, see the main [README.md](README.md)
