
# 🛡️ Malicious URL Detection Using Machine Learning

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://malicious-url-detection-hamim.streamlit.app/)

**Live Demo:** [https://malicious-url-detection-hamim.streamlit.app/](https://malicious-url-detection-hamim.streamlit.app/)

A modern, intelligent web application that uses Random Forest machine learning to detect and classify malicious URLs in real-time. Built with Streamlit, featuring an advanced whitelist override system and beautiful interactive visualizations.

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.52-red)
![scikit--learn](https://img.shields.io/badge/scikit--learn-1.7-orange)
![License](https://img.shields.io/badge/License-MIT-green)

**Author:** Mohammad Hamim  
**Student ID:** 202280090114  
**Course:** Network Security

---

## 🌟 Features

### 🎯 Real-Time URL Analysis
- **Instant Detection**: Analyze URLs in milliseconds with 60 URLs/second throughput
- **4 Threat Categories**: Benign, Phishing, Malware, Defacement
- **Confidence Scores**: Detailed probability breakdown for each category
- **27 Advanced Features**: URL patterns, character analysis, domain inspection

### 🎨 Modern User Interface
- **Glassmorphism Design**: Beautiful gradient backgrounds with frosted glass effects
- **Interactive Visualizations**: 
  - Real-time confidence gauge (Plotly)
  - Security score radar chart
  - Feature importance bar charts
- **Quick Test Buttons**: One-click testing with pre-populated URLs
- **Responsive Layout**: Works seamlessly on desktop and mobile

### 🔒 Intelligent Security System
- **Whitelist Override**: 150+ trusted domains (Google, GitHub, Microsoft, Netflix, etc.)
- **Security Recommendations**: Contextual advice based on URL classification
- **Debug Mode**: Transparent model predictions and override decisions
- **Real-Time Stats**: Live threat statistics and scanning metrics

### 📊 Comprehensive Testing
- **7-Test Suite**: Complete model validation
- **Performance Metrics**: Speed, accuracy, and throughput analysis
- **Beautiful Reports**: HTML, JSON, and TXT formats
- **100% Test Coverage**: All critical paths validated

---

## 🧠 Machine Learning Model

### Architecture
- **Algorithm**: Random Forest Classifier ⭐
- **Features**: 27 URL characteristics
- **Training Data**: 651,191 URLs
- **Classes**: 4 (benign, phishing, malware, defacement)

### Dataset
**Source:** [Malicious URLs Dataset](https://www.kaggle.com/datasets/sid321axn/malicious-urls-dataset)  
**Total Records:** 651,191 URLs  
**Data Sources:** ISCX URL 2016, PhishTank, PhishStorm, Malware Domain List

**Class Distribution:**
- Benign: 428,103 (65.7%)
- Defacement: 96,457 (14.8%)
- Phishing: 94,111 (14.5%)
- Malware: 32,520 (5.0%)

### Feature Categories
1. **URL Metrics**: Length, hostname length, directory count
2. **Character Counts**: Special characters (@, ?, -, =, etc.)
3. **Security Indicators**: HTTPS, IP address, suspicious words
4. **Domain Analysis**: TLD length, embedded domains, short URL services

### Performance
- **Prediction Speed**: ~23ms per URL
- **Throughput**: ~60 URLs/second
- **Feature Extraction**: ~1ms
- **Model Inference**: ~22ms
- **Accuracy**: ~98%
- **F1-Score**: ~0.97 (macro average)

---

## 🚀 Quick Start

### Prerequisites
- Python 3.12 or higher
- pip package manager
- Virtual environment (recommended)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/md-hameem/Malicious-URL-Detection-Using-Machine-Learning.git
   cd Malicious-URL-Detection-Using-Machine-Learning
   ```

2. **Create and activate virtual environment**
   ```bash
   # Windows
   python -m venv .venv
   .venv\Scripts\activate
   
   # Linux/Mac
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

5. **Open your browser**
   Navigate to `http://localhost:8501`

---

## 📁 Project Structure

```
Malicious-URL-Detection-Using-Machine-Learning/
├── 📱 app.py                          # Main Streamlit application
├── 📋 requirements.txt                # Python dependencies
├── 📄 README.md                       # This file
├── 📄 LICENSE                         # MIT License
│
├── 📂 data/                          # Dataset storage
│   └── raw/
│       └── malicious_phish.csv       # Training dataset (651K URLs)
│
├── 📂 models/                        # Trained ML models
│   # (Model files are not included in this version)
│
├── 📂 notebooks/                     # Jupyter notebooks
│   └── malicious_url_detection.ipynb # Analysis & training
│
├── 📂 tests/                         # Test suite
│   ├── test_model.py                 # Comprehensive tests
│   ├── check_features.py             # Feature inspection
│   └── README.md                     # Test documentation
│
├── 📂 scripts/                       # Utility scripts
│   └── app_old.py                    # Previous version backup
│
├── 📂 docs/                          # Documentation
│   ├── PROJECT_STRUCTURE.md          # Structure overview
│   ├── README_DETAILED.md            # Detailed guide
│   └── STREAMLIT_GUIDE.md            # App documentation
│
└── 📂 reports/                       # Test reports
    ├── test_report_*.html            # HTML reports
    ├── test_report_*.json            # JSON reports
    └── test_report_*.txt             # Text reports
```


See [docs/PROJECT_STRUCTURE.md](docs/PROJECT_STRUCTURE.md) for detailed information.

---

## Download Pre-trained Models

Due to file size limitations, model files are not included in the Git repository.

You can download the pre-trained models from the following secure link:

👉 [Download Pre-trained Models (Google Drive)](https://drive.google.com/drive/folders/1Yyc8jiJUFvVebtVE6Ojnpnob75s1dbiP?usp=sharing)

---

## 📖 Usage

### Web Interface

1. **Enter URL**: Type or paste any URL in the input field
2. **Quick Test**: Use preset buttons for Safe, Suspicious, or Risky URLs
3. **Scan**: Click "🚀 Scan Now" to analyze
4. **Review**: See classification, confidence, and recommendations
5. **Debug**: Expand debug section to see detailed model output

### Running Tests

```bash
# Run comprehensive test suite
python tests/test_model.py

# Check model features
python tests/check_features.py
```

Test reports are automatically generated in `reports/` directory in three formats:
- **HTML**: Interactive, styled web report (open in browser)
- **JSON**: Machine-readable data for CI/CD integration
- **TXT**: Plain text for logging and archiving

### Using the Model Programmatically

```python
# Example: Feature extraction and prediction (model loading code removed)
# See app.py for full implementation details
url = "https://example.com"
features_df = extract_url_features(url)  # Returns DataFrame with 27 features
# Model prediction code is not included in this version
```

---

## 🧪 Testing & Quality Assurance

### Comprehensive Test Suite
The project includes a robust testing framework with 7 comprehensive tests:

| Test # | Name | Purpose | Status |
|--------|------|---------|--------|
| 1 | Model Loading | Verify models load correctly | ✅ Pass |
| 2 | Feature Extraction | Validate all 27 features | ✅ Pass |
| 3 | Safe URL Test | Test legitimate domains | ✅ Pass |
| 4 | Malicious URL Test | Test phishing domains | ✅ Pass |
| 5 | Whitelist Override | Test 7 trusted domains | ✅ Pass |
| 6 | Batch Testing | Test 8 URLs with metrics | ✅ Pass |
| 7 | Performance Metrics | Measure speed/throughput | ✅ Pass |

### Test Results
- **Total Tests**: 7
- **Passed**: 7 (100%)
- **Duration**: ~3 seconds
- **Throughput**: 60 URLs/second

See [tests/README.md](tests/README.md) for detailed test documentation.

---

## 🔧 Configuration

### Whitelist Management
The application includes a whitelist of 150+ trusted domains. To modify:

Edit `safe_domains` list in `app.py` (around line 643):
```python
safe_domains = [
    'google.com', 'github.com', 'microsoft.com',
    # Add more trusted domains...
]
```

### Model Retraining
To retrain with updated data:
1. Place new data in `data/raw/`
2. Update feature extraction if needed
3. Run training notebook in `notebooks/`
4. Save new model to `models/`

---

## 🎯 Key Technologies

| Technology | Purpose |
|------------|---------|
| **Streamlit** | Modern web application framework |
| **scikit-learn** | Machine learning models |
| **Plotly** | Interactive visualizations |
| **pandas** | Data manipulation and analysis |
| **TLD** | Domain extraction and parsing |
| **Python 3.12** | Core programming language |

---

## ⚠️ Known Issues & Solutions

### Issue: Model Misclassifies Safe Domains
**Problem**: Model predicts google.com, github.com as phishing (98-100% confidence)

**Root Cause**: Training data labels URLs by content, not domain reputation. Google Docs/Drive used for phishing → model learns "google.com" = phishing

**Solution**: Whitelist override system with 150+ trusted domains provides practical workaround

**Proper Fix**: Retrain model with:
- Domain reputation features
- Distinction between main domain and subdomains
- Platform vs. content classification

See [docs/PROJECT_STRUCTURE.md](docs/PROJECT_STRUCTURE.md) for detailed analysis.

---

## 🚀 Implemented Features

- ✅ **Random Forest ML Model** (98% accuracy)
- ✅ **Modern Streamlit Web App** with glassmorphism design
- ✅ **Real-time URL Analysis** (60 URLs/second)
- ✅ **Interactive Plotly Visualizations**
- ✅ **150+ Domain Whitelist Override**
- ✅ **27 Feature Extraction**
- ✅ **Comprehensive Test Suite** (7 tests, 100% pass rate)
- ✅ **Automated Report Generation** (HTML/JSON/TXT)
- ✅ **Security Recommendations**
- ✅ **Debug Mode** for transparency

## 🔮 Future Enhancements

- [ ] Deep learning models (LSTM, CNN)
- [ ] RESTful API for integration
- [ ] Browser extension
- [ ] Docker containerization
- [ ] CI/CD pipeline
- [ ] Database for scan history
- [ ] Advanced threat intelligence
- [ ] Mobile application
- [ ] Real-time threat feeds

---

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Make your changes
4. Run tests: `python tests/test_model.py`
5. Commit changes (`git commit -m 'Add AmazingFeature'`)
6. Push to branch (`git push origin feature/AmazingFeature`)
7. Open a Pull Request

---

## 📚 Documentation

- **Main README**: This file
- **Detailed Guide**: [docs/README_DETAILED.md](docs/README_DETAILED.md)
- **Project Structure**: [docs/PROJECT_STRUCTURE.md](docs/PROJECT_STRUCTURE.md)
- **Streamlit Guide**: [docs/STREAMLIT_GUIDE.md](docs/STREAMLIT_GUIDE.md)
- **Test Documentation**: [tests/README.md](tests/README.md)

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Mohammad Hamim**  
- Student ID: 202280090114
- GitHub: [@md-hameem](https://github.com/md-hameem)
- Repository: [Malicious-URL-Detection-Using-Machine-Learning](https://github.com/md-hameem/Malicious-URL-Detection-Using-Machine-Learning)
- Course: Network Security

---

## 🙏 Acknowledgments

- **Dataset**: [Malicious URLs Dataset](https://www.kaggle.com/datasets/sid321axn/malicious-urls-dataset) by Siddhant Baldota
- **Data Sources**: ISCX URL 2016, PhishTank, PhishStorm, Malware Domain List
- **Frameworks**: Streamlit, scikit-learn, Plotly
- **Course**: Network Security

---

## 📞 Support

For questions, issues, or feedback:
- Open an [issue](https://github.com/md-hameem/Malicious-URL-Detection-Using-Machine-Learning/issues)
- Check the [documentation](docs/)
- Review [test reports](reports/)

---

## 📅 Project Status

**Last Updated**: December 8, 2025  
**Version**: 2.0  
**Status**: ✅ Active - Fully Functional

---

<div align="center">
  <strong>🛡️ Stay Safe Online!</strong>
  <br>
  <em>Protect yourself from malicious URLs with ML-powered detection</em>
  <br><br>
  <strong>⭐ Star this repository if you find it helpful!</strong>
</div>
