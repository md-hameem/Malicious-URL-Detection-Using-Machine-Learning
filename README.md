# Malicious URL Detection Using Machine Learning

A comprehensive machine learning project for detecting and classifying malicious URLs into four categories: Benign, Defacement, Phishing, and Malware.

**Author:** Mohammad Hamim  
**Student ID:** 202280090114  
**Course:** Network Security

---

## 📋 Project Overview

Malicious URLs are a primary attack vector in cybersecurity, enabling phishing attacks, malware distribution, website defacement, and credential theft. This project develops a machine learning-based classification system that can identify malicious URLs with high accuracy, providing a defense mechanism for cybersecurity systems including:

- Email filters
- Network firewalls
- Browser protection mechanisms
- Security monitoring tools

---

## 🎯 Features

### URL Classification Categories
- **Benign** — Safe, legitimate URLs
- **Defacement** — Compromised websites
- **Phishing** — Fraudulent links designed to steal information
- **Malware** — URLs hosting malicious software

### Feature Engineering (30+ Features)
- **Lexical Features:** URL length, hostname length, character counts
- **Special Characters:** Detection of @, ?, -, =, ., #, %, +, $, !, *, etc.
- **Structural Features:** IP address presence, HTTPS protocol, directory count
- **Behavioral Features:** URL shortening detection, suspicious keywords, abnormal patterns

---

## 📊 Dataset

**Source:** [Malicious URLs Dataset](https://www.kaggle.com/datasets/sid321axn/malicious-urls-dataset) (Kaggle)  
**Total Records:** 651,191 URLs  
**Data Sources:** ISCX URL 2016, PhishTank, PhishStorm, Malware Domain List

**Class Distribution:**
- Benign: 66%
- Defacement: 15%
- Phishing: 14%
- Malware: 5%

---

## 🤖 Machine Learning Models

### Machine Learning Models
1. **Decision Tree**
2. **Random Forest** ⭐ (Best Model)
3. **Extra Trees Classifier**
4. **AdaBoost**
5. **Gaussian Naive Bayes**
6. **SGD Classifier**
7. **Gradient Boosting**
8. **XGBoost**

### Best Model Performance
- **Model:** Random Forest (Tuned)
- **Accuracy:** ~98%
- **F1-Score:** ~0.97 (macro average)
- **Precision:** ~0.97 (macro average)
- **Recall:** ~0.97 (macro average)

---

## 🚀 Getting Started

### Prerequisites
```bash
Python 3.8+
pip
```

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/malicious-url-detection.git
   cd malicious-url-detection
   ```

2. **Create virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Download dataset**
   The notebook automatically downloads the dataset using `kagglehub`. Ensure you have a Kaggle account and API key configured.

---

## 📁 Project Structure

```
malicious-url-detection/
├── notebooks/
│   └── malicious_url_detection.ipynb    # Main analysis notebook
├── models/
│   ├── final_random_forest_model.pkl    # Random Forest model
│   ├── label_encoder.pkl                # Label encoder
│   └── README.md                        # Model documentation
├── data/
│   └── raw/                             # Dataset folder
├── app.py                               # Streamlit web application
├── STREAMLIT_GUIDE.md                   # Streamlit app documentation
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

---

## 💻 Usage

### Option 1: Running the Notebook

1. **Start Jupyter Notebook**
   ```bash
   jupyter notebook
   ```

2. **Open** `notebooks/malicious_url_detection.ipynb`

3. **Run all cells** to:
   - Download and load the dataset
   - Perform feature engineering
   - Train traditional ML and deep learning models
   - Generate visualizations
   - Save all trained models

### Option 2: Streamlit Web Application 🚀

1. **Install Streamlit**
   ```bash
   pip install streamlit
   ```

2. **Start the application**
   ```bash
   streamlit run app.py
   ```

3. **Access the app**
   - Open your browser to http://localhost:8501
   - Enter a URL in the text box
   - Click "🚀 Analyze URL"
   - View detailed predictions and feature analysis

4. **Features:**
   - Real-time URL analysis with instant results
   - Visual prediction display with color-coded risk levels
   - Detailed feature extraction breakdown
   - Security recommendations
   - Example URLs for quick testing

For complete documentation, see [STREAMLIT_GUIDE.md](STREAMLIT_GUIDE.md)

### Option 3: Using the Trained Model Programmatically

```python
import pickle
import pandas as pd
from urllib.parse import urlparse

# Load the model
with open("models/final_random_forest_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("models/label_encoder.pkl", "rb") as f:
    label_encoder = pickle.load(f)

# Extract features from URL (use feature extraction functions from notebook)
url = "http://suspicious-site.com/login"
features = extract_url_features(url)  # See notebook for function

# Predict
prediction = model.predict(features)[0]
label = label_encoder.inverse_transform([prediction])[0]

print(f"URL: {url}")
print(f"Prediction: {label}")
```

---

## 📈 Results & Visualizations

The project includes comprehensive visualizations:

1. **Class Distribution Analysis** — Dataset balance and statistics
2. **URL Length Analysis** — Patterns across different URL types
3. **Feature Distribution** — Box plots and comparisons
4. **Security Features** — HTTPS usage, IP presence, suspicious keywords
5. **Correlation Heatmap** — Feature relationships
6. **Model Performance** — Comparison across all models
7. **Confusion Matrix** — Detailed classification results
8. **ROC Curves** — Multi-class performance evaluation
9. **Learning Curves** — Model training progress

---

## 🔍 Key Findings

1. **Random Forest** achieved the best overall performance with proper hyperparameter tuning
2. **Benign URLs** have the highest classification accuracy
3. **URL length** and **special character features** are strong indicators for malware detection
4. **HTTPS usage** is significantly higher in benign URLs compared to malicious ones
5. **Phishing URLs** often contain suspicious keywords (login, bank, secure, etc.)

---

## 🛠️ Technologies Used

### Core Technologies
- **Python 3.12**
- **pandas** — Data manipulation
- **numpy** — Numerical computing

### Machine Learning
- **scikit-learn** — Traditional ML models
- **XGBoost** — Gradient boosting

### Visualization
- **matplotlib & seaborn** — Data visualization
- **Interactive plots** — Model comparison

### Utilities
- **tld** — Top-level domain extraction
- **kagglehub** — Dataset management
- **Jupyter Notebook** — Interactive development

---

## 🚀 Implemented Features

- [x] **Traditional ML models** (8 algorithms)
- [x] **Interactive Streamlit web app** 🎨
- [x] **Real-time URL analysis** with instant predictions
- [x] **Comprehensive visualizations**
- [x] **Feature extraction** (30+ features)
- [x] **Hyperparameter tuning** (GridSearchCV)
- [x] **Model comparison** and evaluation
- [x] **Cross-validation** for robust performance

## 🔮 Future Improvements

- [ ] Deep learning models (LSTM, CNN)
- [ ] Real-time URL scanning API
- [ ] Browser extension integration
- [ ] Docker containerization
- [ ] Continuous model retraining with new data
- [ ] Mobile application
- [ ] Database for scan history
- [ ] Advanced threat intelligence integration

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Mohammad Hamim**  
Student ID: 202280090114  
Network Security Course Project

---

## 🙏 Acknowledgments

- Dataset: [Malicious URLs Dataset](https://www.kaggle.com/datasets/sid321axn/malicious-urls-dataset) by Siddhant Baldota
- Data Sources: ISCX URL 2016, PhishTank, PhishStorm, Malware Domain List
- Course: Network Security

---

## 📧 Contact

For questions or feedback, please open an issue on GitHub.

---

## ⭐ Star this repository if you find it helpful!
