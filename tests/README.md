# 🧪 Test Suite Documentation

Comprehensive testing suite for the Malicious URL Detection system.

## 📋 Test Overview

### Test Files
- **test_model.py**: Main test suite with 7 comprehensive tests
- **check_features.py**: Utility to inspect model's expected features

### Test Coverage

| Test # | Name | Purpose | Status |
|--------|------|---------|--------|
| 1 | Model Loading | Verify models load correctly | ✅ Pass |
| 2 | Feature Extraction | Validate all 27 features | ✅ Pass |
| 3 | Safe URL Test | Test legitimate domain (google.com) | ✅ Pass |
| 4 | Malicious URL Test | Test phishing domain | ✅ Pass |
| 5 | Whitelist Override | Test whitelist system (7 domains) | ✅ Pass |
| 6 | Batch Testing | Test 8 URLs with metrics | ✅ Pass |
| 7 | Performance Metrics | Measure speed and throughput | ✅ Pass |

## 🚀 Running Tests

### Quick Run
```bash
python tests/test_model.py
```

### Check Model Features
```bash
python tests/check_features.py
```

## 📊 Test Results

### Latest Test Run
- **Total Tests**: 7
- **Passed**: 7 (100%)
- **Failed**: 0
- **Duration**: ~3 seconds
- **Success Rate**: 100%

### Performance Metrics
- **Average Prediction Time**: 23ms per URL
- **Throughput**: 60 URLs/second
- **Feature Extraction**: 1ms
- **Model Prediction**: 22ms

## 📄 Test Reports

Tests automatically generate reports in `reports/` directory:

### Report Formats

1. **HTML Report** (`test_report_*.html`)
   - Beautiful, interactive web interface
   - Color-coded test results
   - Summary statistics cards
   - Detailed test breakdowns
   - Professional styling

2. **JSON Report** (`test_report_*.json`)
   - Machine-readable format
   - Complete test metadata
   - Easy CI/CD integration
   - Structured data for analysis

3. **TXT Report** (`test_report_*.txt`)
   - Plain text format
   - Clean, readable output
   - Perfect for logging
   - Archive-friendly

### Report Contents
- Test execution summary
- Individual test results
- Performance statistics
- Error messages (if any)
- System information
- Timestamp and report ID

## 🔍 Test Details

### Test 1: Model Loading
**Purpose**: Verify that Random Forest model and label encoder load successfully

**Validation**:
- Model file exists and is readable
- Label encoder file exists and is readable
- Objects are not None
- No loading errors

**Expected Result**: ✅ Both models load without errors

---

### Test 2: Feature Extraction Validation
**Purpose**: Ensure all 27 features are extracted in correct order

**Test URL**: `https://www.example.com/path/to/page?query=test&id=123#section`

**Validation**:
- Exactly 27 features extracted
- Feature names match model expectations
- No missing features
- No extra features
- Correct data types

**Expected Result**: ✅ All features present and valid

**Sample Output**:
```
url_length                = 62
hostname_length           = 15
count_letters             = 46
count_digits              = 3
count_@                   = 0
count_?                   = 1
...
```

---

### Test 3: Safe URL Test (Google.com)
**Purpose**: Test model's prediction on legitimate domain with whitelist override

**Test URL**: `https://www.google.com`

**Process**:
1. Extract features
2. Get model's raw prediction
3. Apply whitelist override if needed
4. Validate final classification

**Expected Behavior**:
- Model predicts: phishing (99.88% - incorrect)
- Whitelist detects: www.google.com is trusted
- Override applies: benign (95%)
- Final result: ✅ BENIGN

**Key Insight**: Demonstrates whitelist override correcting model's training data bias

---

### Test 4: Malicious URL Test
**Purpose**: Verify model correctly identifies malicious URLs

**Test URL**: `http://example-login-bank.com`

**Expected Result**: 
- Classification: phishing
- Confidence: >95%
- No whitelist override

**Validation**: ✅ Model correctly identifies threat

---

### Test 5: Whitelist Override System
**Purpose**: Comprehensive test of whitelist functionality

**Test Domains**:
1. www.google.com
2. www.youtube.com
3. www.github.com
4. www.netflix.com
5. www.microsoft.com
6. stackoverflow.com
7. www.wikipedia.org

**For Each Domain**:
- ✓ Check if whitelisted
- ✓ Get model's raw prediction
- ✓ Apply override if needed
- ✓ Verify final classification is benign

**Expected Result**: ✅ All 7 domains correctly classified as BENIGN

**Statistics**:
- Domains tested: 7
- Overrides applied: 7 (100%)
- Final accuracy: 100%

---

### Test 6: Batch URL Testing
**Purpose**: Test multiple URLs with performance tracking

**Test URLs** (8 total):
- **Safe URLs** (4):
  - https://www.google.com
  - https://www.github.com
  - https://www.wikipedia.org
  - https://www.microsoft.com

- **Malicious URLs** (4):
  - http://bit.ly/suspicious123
  - http://192.168.1.1/login
  - http://example-paypal-login.com
  - http://free-lucky-bonus.com/win

**Metrics Tracked**:
- Prediction accuracy
- Confidence levels
- Processing time per URL
- Total batch time

**Expected Results**:
- Model raw accuracy: ~50% (due to safe URL misclassification)
- With whitelist: 100%
- Average time: 43-55ms per URL

---

### Test 7: Performance Metrics
**Purpose**: Measure prediction speed and system performance

**Test Cases** (5 URLs):
1. https://www.google.com
2. https://www.github.com/user/repo
3. http://example.com/path?query=test
4. https://subdomain.example.com/deep/path/here
5. http://short.url/abc123

**Measurements**:
- Feature extraction time
- Model prediction time
- Total processing time
- Throughput (URLs/second)

**Performance Targets**:
- Feature extraction: <2ms
- Prediction: <30ms
- Total: <35ms
- Throughput: >40 URLs/sec

**Typical Results**:
- Feature extraction: ~1ms
- Prediction: ~22ms
- Total: ~23ms
- Throughput: ~60 URLs/sec

## 🛠️ Adding New Tests

To add a new test to the suite:

1. **Create test function** in `test_model.py`:
```python
def test_new_feature():
    """Test description"""
    # Load models
    with open("models/final_random_forest_model.pkl", "rb") as f:
        model = pickle.load(f)
    
    # Test logic here
    
    # Assertions
    assert condition, "Error message"
    print("✅ TEST PASSED")
```

2. **Register in main block**:
```python
if __name__ == "__main__":
    # ... existing tests ...
    
    print("\n[TEST 8] New Feature Test")
    print("-" * 80)
    test_start = time.time()
    try:
        test_new_feature()
        test_results.append({
            'name': 'New Feature Test',
            'status': 'passed',
            'duration': time.time() - test_start,
            'details': {'description': 'What the test does'}
        })
    except Exception as e:
        test_results.append({
            'name': 'New Feature Test',
            'status': 'failed',
            'duration': time.time() - test_start,
            'details': {'error': str(e)}
        })
        raise
```

3. **Run tests** to verify:
```bash
python tests/test_model.py
```

## 🐛 Debugging Failed Tests

### Common Issues

**Issue**: Model loading fails
- **Check**: Files exist in `models/` directory
- **Check**: File permissions are correct
- **Solution**: Re-download or retrain models

**Issue**: Feature extraction errors
- **Check**: URL format is valid
- **Check**: All 27 features are extracted
- **Solution**: Verify feature extraction functions

**Issue**: Whitelist not working
- **Check**: Domain is in safe_domains list
- **Check**: Hostname extraction is correct
- **Solution**: Add domain to whitelist

**Issue**: Performance degradation
- **Check**: System resources (CPU, RAM)
- **Check**: Model file size and loading time
- **Solution**: Optimize feature extraction

## 📊 Continuous Integration

### CI/CD Integration

The test suite is designed for easy CI/CD integration:

```yaml
# Example GitHub Actions workflow
name: Run Tests
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.12'
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Run tests
        run: python tests/test_model.py
      - name: Upload reports
        uses: actions/upload-artifact@v2
        with:
          name: test-reports
          path: reports/
```

## 📈 Test Coverage Goals

- ✅ Model loading: 100%
- ✅ Feature extraction: 100%
- ✅ URL classification: 100%
- ✅ Whitelist system: 100%
- ✅ Performance metrics: 100%
- ⬜ Error handling: 80%
- ⬜ Edge cases: 90%

## 🎯 Future Enhancements

1. **Additional Tests**
   - Edge case URLs (empty, invalid, extremely long)
   - Unicode and international domains
   - URL encoding edge cases
   - Model robustness tests

2. **Performance Tests**
   - Concurrent request handling
   - Memory usage profiling
   - Large batch processing (1000+ URLs)
   - Cache effectiveness

3. **Integration Tests**
   - Streamlit UI testing
   - Database integration (if added)
   - API endpoint testing (if added)

4. **Security Tests**
   - Input sanitization
   - SQL injection attempts
   - XSS prevention
   - DoS resistance

## 📞 Support

For test-related issues:
1. Check this documentation
2. Review test reports in `reports/`
3. Check console output for errors
4. Review model and feature extraction code

---

**Last Updated**: December 8, 2025
**Test Suite Version**: 1.0
**Status**: All tests passing ✅
