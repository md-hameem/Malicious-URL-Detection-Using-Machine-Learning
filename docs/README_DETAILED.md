# 🛡️ Malicious URL Detection Using Machine Learning

A modern, intelligent web application that uses Random Forest machine learning to detect and classify malicious URLs in real-time. Built with Streamlit, featuring an advanced whitelist override system and beautiful interactive visualizations.

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.52-red)
![scikit--learn](https://img.shields.io/badge/scikit--learn-1.7-orange)
![License](https://img.shields.io/badge/License-MIT-green)

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
- **Whitelist Override**: 150+ trusted domains (Google, GitHub, Microsoft, etc.)
- **Security Recommendations**: Contextual advice based on URL classification
- **Debug Mode**: Transparent model predictions and override decisions
- **Real-Time Stats**: Live threat statistics and scanning metrics

### 📊 Comprehensive Testing
- **7-Test Suite**: Complete model validation
- **Performance Metrics**: Speed, accuracy, and throughput analysis
- **Beautiful Reports**: HTML, JSON, and TXT formats
- **100% Test Coverage**: All critical paths validated

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

Test reports are automatically generated in `reports/` directory.

## 🧠 Machine Learning Model

### Architecture
- **Algorithm**: Random Forest Classifier
- **Features**: 27 URL characteristics
- **Training Data**: 651,191 URLs
- **Classes**: 4 (benign, phishing, malware, defacement)

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

## 📁 Project Structure

```
├── 📱 app.py                    # Main Streamlit application
├── 📋 requirements.txt          # Python dependencies
├── 📂 data/                    # Training dataset (651K URLs)
├── 📂 models/                  # Trained ML models
├── 📂 tests/                   # Comprehensive test suite
├── 📂 scripts/                 # Utility scripts
├── 📂 docs/                    # Documentation
└── 📂 reports/                 # Test reports
```

See [PROJECT_STRUCTURE.md](docs/PROJECT_STRUCTURE.md) for detailed structure.

## 🔧 Configuration

### Whitelist Management
Edit the `safe_domains` list in `app.py` (line ~643) to add/remove trusted domains:

```python
safe_domains = [
    'google.com', 'github.com', 'microsoft.com',
    # Add more trusted domains...
]
```

### Model Retraining
To retrain the model with updated data:
1. Place new training data in `data/raw/`
2. Update feature extraction if needed
3. Run training notebook in `notebooks/`
4. Save new model to `models/`

## 🎯 Key Technologies

| Technology | Purpose |
|------------|---------|
| **Streamlit** | Web application framework |
| **scikit-learn** | Machine learning models |
| **Plotly** | Interactive visualizations |
| **pandas** | Data manipulation |
| **TLD** | Domain extraction |

## 📊 Test Reports

The test suite generates comprehensive reports:

- **HTML**: Beautiful, interactive web report
- **JSON**: Machine-readable format for CI/CD
- **TXT**: Plain text for logging

Example test results:
- ✅ 7/7 tests passed (100%)
- ⏱️ 3.06 seconds total duration
- 🎯 100% whitelist override success
- 📈 60 URLs/second throughput

## ⚠️ Known Issues & Solutions

### Issue: Model Misclassifies Safe Domains
**Problem**: Model predicts google.com, github.com as phishing (98-100% confidence)

**Root Cause**: Training data labels URLs by content, not domain reputation. Google Docs/Drive used for phishing → model learns "google.com" = phishing

**Solution**: Whitelist override system with 150+ trusted domains provides practical workaround

**Proper Fix**: Retrain model with:
- Domain reputation features
- Distinction between main domain and subdomains
- Platform vs. content classification

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests: `python tests/test_model.py`
5. Submit a pull request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Mohammad Hamim**
- Student ID: 202280090114
- GitHub: [@md-hameem](https://github.com/md-hameem)
- Repository: [Malicious-URL-Detection-Using-Machine-Learning](https://github.com/md-hameem/Malicious-URL-Detection-Using-Machine-Learning)

## 🙏 Acknowledgments

- Training dataset: [Malicious URLs Dataset](https://www.kaggle.com/datasets/sid321axn/malicious-urls-dataset)
- Streamlit for the amazing web framework
- scikit-learn for ML tools
- Plotly for beautiful visualizations

## 📅 Last Updated

December 8, 2025

---

<div align="center">
  <strong>🛡️ Stay Safe Online!</strong>
  <br>
  <em>Protect yourself from malicious URLs with ML-powered detection</em>
</div>
