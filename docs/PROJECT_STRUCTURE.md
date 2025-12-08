# Project Structure

This document describes the organization of the Malicious URL Detection project.

## 📁 Directory Structure

```
Malicious-URL-Detection-Using-Machine-Learning/
│
├── 📱 app.py                          # Main Streamlit web application
├── 📋 requirements.txt                # Python dependencies
├── 📄 README.md                       # Project overview and instructions
├── 📄 LICENSE                         # Project license
├── 📄 .gitignore                      # Git ignore rules
│
├── 📂 data/                          # Dataset storage
│   └── raw/
│       └── malicious_phish.csv       # Training dataset (651K URLs)
│
├── 📂 models/                        # Trained ML models
│   ├── final_random_forest_model.pkl # Random Forest classifier
│   └── label_encoder.pkl             # Label encoder for classes
│
├── 📂 notebooks/                     # Jupyter notebooks
│   └── (analysis and training notebooks)
│
├── 📂 tests/                         # Test suite
│   ├── test_model.py                 # Comprehensive model tests
│   └── check_features.py             # Feature inspection utility
│
├── 📂 scripts/                       # Utility scripts
│   └── app_old.py                    # Previous version backup
│
├── 📂 docs/                          # Documentation
│   ├── PROJECT_STRUCTURE.md          # This file
│   └── STREAMLIT_GUIDE.md            # Streamlit app guide
│
└── 📂 reports/                       # Test reports and outputs
    ├── test_report_*.html            # HTML test reports
    ├── test_report_*.json            # JSON test reports
    └── test_report_*.txt             # Text test reports
```

## 🎯 Key Components

### Main Application
- **app.py**: Modern Streamlit web interface with:
  - Real-time URL scanning
  - Interactive visualizations (Plotly)
  - Whitelist override system (150+ trusted domains)
  - Security recommendations
  - Debug information

### Machine Learning Models
- **Random Forest Classifier**: 27 features, 4 classes
  - Classes: benign, phishing, malware, defacement
  - Trained on 651,191 URLs
  - Features: URL patterns, character counts, domain analysis

### Test Suite
- **test_model.py**: Comprehensive testing with 7 test cases
  - Model loading validation
  - Feature extraction validation
  - Safe/malicious URL testing
  - Whitelist override testing
  - Batch processing
  - Performance metrics
  - Generates HTML/JSON/TXT reports

- **check_features.py**: Utility to inspect model's expected features

### Data
- **malicious_phish.csv**: Training dataset
  - 651,191 total URLs
  - Distribution: benign (65.7%), defacement (14.8%), phishing (14.5%), malware (5.0%)

## 🚀 Quick Start

### Run the Application
```bash
streamlit run app.py
```

### Run Tests
```bash
python tests/test_model.py
```

### View Test Reports
Test reports are automatically generated in the `reports/` directory in three formats:
- HTML (interactive, styled)
- JSON (machine-readable)
- TXT (plain text)

## 📊 Key Features

### Whitelist Override System
The application includes an extensive whitelist of 150+ trusted domains to override incorrect model predictions. This addresses the training data issue where legitimate platforms (Google Docs, GitHub, etc.) hosting malicious content were labeled as malicious, causing the model to misclassify the main domains.

### Performance
- Average prediction time: ~23ms per URL
- Throughput: ~60 URLs/second
- Feature extraction: ~1ms
- Model prediction: ~22ms

## 🔧 Development

### Adding New Tests
Add test functions to `tests/test_model.py` and register them in the main execution block.

### Updating Whitelist
Modify the `safe_domains` list in `app.py` (around line 643) to add or remove trusted domains.

### Feature Engineering
All feature extraction functions are in `app.py`. Model expects exactly 27 features in a specific order.

## 📝 Notes

### Known Issues
- Model misclassifies many legitimate domains (Google, GitHub, etc.) as phishing
- Root cause: Training data labels URLs by content, not by domain reputation
- Solution: Whitelist override system provides practical workaround
- Proper fix: Retrain model with better feature engineering (domain vs. subdomain distinction)

### Version Warnings
- scikit-learn version mismatch warnings (1.6.1 vs 1.7.2) are non-critical
- Models function correctly despite version difference

## 👤 Author
Mohammad Hamim
ID: 202280090114

## 📅 Last Updated
December 8, 2025
