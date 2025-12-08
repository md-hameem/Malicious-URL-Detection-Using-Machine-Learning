import pytest
import pickle
import pandas as pd
import sys
import re
from urllib.parse import urlparse
from tld import get_tld

# Import functions from app.py
sys.path.insert(0, 'E:/NS Final Work')

# Feature extraction functions (copied from app.py)
def having_ip_address(url):
    match = re.search(
        r'(([01]?\d\d?|2[0-4]\d|25[0-5])\.([01]?\d\d?|2[0-4]\d|25[0-5])\.([01]?\d\d?|2[0-4]\d|25[0-5])\.([01]?\d\d?|2[0-4]\d|25[0-5])\/'
        r'([01]?\d\d?|2[0-4]\d|25[0-5])\.([01]?\d\d?|2[0-4]\d|25[0-5])\.([01]?\d\d?|2[0-4]\d|25[0-5])\.([01]?\d\d?|2[0-4]\d|25[0-5]))',
        url
    )
    return 1 if match else 0

def abnormal_url(url):
    hostname = urlparse(url).hostname
    if hostname:
        return 0 if hostname in url else 1
    return 1

def count_directories(url):
    urldir = urlparse(url).path
    return urldir.count('/')

def shortening_service(url):
    match = re.search(
        r'bit\.ly|goo\.gl|shorte\.st|go2l\.ink|x\.co|ow\.ly|t\.co|tinyurl|tr\.im|is\.gd|cli\.gs|'
        r'yfrog\.com|migre\.me|ff\.im|tiny\.cc|url4\.eu|twit\.ac|su\.pr|twurl\.nl|snipurl\.com|'
        r'short\.to|BudURL\.com|ping\.fm|post\.ly|Just\.as|bkite\.com|snipr\.com|fic\.kr|loopt\.us|'
        r'doiop\.com|short\.ie|kl\.am|wp\.me|rubyurl\.com|om\.ly|to\.ly|bit\.do|t\.co|lnkd\.in|'
        r'db\.tt|qr\.ae|adf\.ly|goo\.gl|bitly\.com|cur\.lv|tinyurl\.com|ow\.ly|bit\.ly|ity\.im|'
        r'q\.gs|is\.gd|po\.st|bc\.vc|twitthis\.com|u\.to|j\.mp|buzurl\.com|cutt\.us|u\.bb|yourls\.org|'
        r'x\.co|prettylinkpro\.com|scrnch\.me|filoops\.info|vzturl\.com|qr\.net|1url\.com|tweez\.me|v\.gd|'
        r'tr\.im|link\.zip\.net',
        url
    )
    return 1 if match else 0

def count_dots(url):
    return url.count('.')

def count_hyphens(url):
    return url.count('-')

def count_underscores(url):
    return url.count('_')

def count_slashes(url):
    return url.count('/')

def count_questionmarks(url):
    return url.count('?')

def count_equals(url):
    return url.count('=')

def count_at(url):
    return url.count('@')

def count_ampersand(url):
    return url.count('&')

def count_exclamation(url):
    return url.count('!')

def count_space(url):
    return url.count(' ')

def count_tilde(url):
    return url.count('~')

def count_comma(url):
    return url.count(',')

def count_plus(url):
    return url.count('+')

def count_asterisk(url):
    return url.count('*')

def count_hashtag(url):
    return url.count('#')

def count_dollar(url):
    return url.count('$')

def count_percent(url):
    return url.count('%')

def https_token(url):
    return 1 if 'https' in urlparse(url).netloc else 0

def url_length(url):
    return len(url)

def hostname_length(url):
    hostname = urlparse(url).hostname
    return len(hostname) if hostname else 0

def suspicious_words(url):
    match = re.search(
        r'PayPal|login|signin|bank|account|update|free|lucky|service|bonus|ebayisapi|webscr',
        url
    )
    return 1 if match else 0

def digit_count(url):
    return sum(c.isdigit() for c in url)

def letter_count(url):
    return sum(c.isalpha() for c in url)

def fd_length(url):
    urlpath = urlparse(url).path
    try:
        return len(urlpath.split('/')[1])
    except:
        return 0

def tld_length(tld):
    try:
        return len(tld)
    except:
        return -1

def extract_url_features(url):
    """Extract features from URL"""
    try:
        # Get TLD
        try:
            res = get_tld(url, as_object=True, fail_silently=False, fix_protocol=True)
            tld = res.tld
        except:
            tld = ''
        
        # Extract all features with correct names
        features = {
            'use_of_ip': having_ip_address(url),
            'abnormal_url': abnormal_url(url),
            'count_.': count_dots(url),
            'count_-': count_hyphens(url),
            'count__': count_underscores(url),
            'count_/': count_slashes(url),
            'count_?': count_questionmarks(url),
            'count_=': count_equals(url),
            'count_@': count_at(url),
            'count_&': count_ampersand(url),
            'count_!': count_exclamation(url),
            'count_ ': count_space(url),
            'count_~': count_tilde(url),
            'count_,': count_comma(url),
            'count_+': count_plus(url),
            'count_*': count_asterisk(url),
            'count_#': count_hashtag(url),
            'count_$': count_dollar(url),
            'count_%': count_percent(url),
            'https': 1 if url.startswith('https') else 0,
            'has_ip': having_ip_address(url),
            'short_url': shortening_service(url),
            'url_length': url_length(url),
            'hostname_length': hostname_length(url),
            'suspicious': suspicious_words(url),
            'count_digits': digit_count(url),
            'count_letters': letter_count(url),
            'fd_length': fd_length(url),
            'tld_length': tld_length(tld),
            'count_dir': count_directories(url),
            'count_embed_domain': url.count('//') - 1
        }
        
        return pd.DataFrame([features])
    except Exception as e:
        print(f"Error extracting features: {e}")
        return None


def test_load_models():
    """Test if models can be loaded"""
    with open("models/final_random_forest_model.pkl", "rb") as f:
        model = pickle.load(f)
    with open("models/label_encoder.pkl", "rb") as f:
        label_encoder = pickle.load(f)
    
    assert model is not None, "Model should be loaded"
    assert label_encoder is not None, "Label encoder should be loaded"
    print("✓ Models loaded successfully")


def test_google_prediction():
    """Test prediction for google.com (should be benign)"""
    # Load models
    with open("models/final_random_forest_model.pkl", "rb") as f:
        model = pickle.load(f)
    with open("models/label_encoder.pkl", "rb") as f:
        label_encoder = pickle.load(f)
    
    # Test URL
    url = "https://www.google.com"
    
    # Extract features
    features_df = extract_url_features(url)
    print(f"\n✓ Features extracted for {url}")
    print(f"  Feature shape: {features_df.shape}")
    print(f"  Feature columns: {list(features_df.columns)}")
    print(f"\n  Sample features:")
    print(f"    - URL Length: {features_df['url_length'].values[0]}")
    print(f"    - HTTPS: {features_df['https'].values[0]}")
    print(f"    - Has IP: {features_df['has_ip'].values[0]}")
    print(f"    - Suspicious: {features_df['suspicious'].values[0]}")
    
    # Make prediction
    prediction = model.predict(features_df)[0]
    prediction_proba = model.predict_proba(features_df)[0]
    label = label_encoder.inverse_transform([prediction])[0]
    confidence = prediction_proba[prediction] * 100
    
    print(f"\n✓ Prediction made:")
    print(f"  - Predicted Label: {label}")
    print(f"  - Confidence: {confidence:.2f}%")
    print(f"  - All probabilities:")
    for cls, prob in zip(label_encoder.classes_, prediction_proba):
        print(f"    * {cls}: {prob*100:.2f}%")
    
    # Assert
    assert label.lower() == 'benign', f"Expected 'benign', got '{label}'"
    print(f"\n✅ TEST PASSED: Google.com correctly classified as BENIGN")


def test_malicious_url():
    """Test prediction for a clearly malicious URL"""
    # Load models
    with open("models/final_random_forest_model.pkl", "rb") as f:
        model = pickle.load(f)
    with open("models/label_encoder.pkl", "rb") as f:
        label_encoder = pickle.load(f)
    
    # Test URL
    url = "http://example-login-bank.com"
    
    # Extract features
    features_df = extract_url_features(url)
    print(f"\n✓ Features extracted for {url}")
    
    # Make prediction
    prediction = model.predict(features_df)[0]
    prediction_proba = model.predict_proba(features_df)[0]
    label = label_encoder.inverse_transform([prediction])[0]
    confidence = prediction_proba[prediction] * 100
    
    print(f"\n✓ Prediction made:")
    print(f"  - Predicted Label: {label}")
    print(f"  - Confidence: {confidence:.2f}%")
    print(f"  - All probabilities:")
    for cls, prob in zip(label_encoder.classes_, prediction_proba):
        print(f"    * {cls}: {prob*100:.2f}%")
    
    # Assert (should NOT be benign)
    assert label.lower() != 'benign', f"Expected malicious classification, got '{label}'"
    print(f"\n✅ TEST PASSED: Malicious URL correctly classified as {label.upper()}")


if __name__ == "__main__":
    print("="*60)
    print("TESTING URL MALICIOUS DETECTION MODEL")
    print("="*60)
    
    print("\n[TEST 1] Loading Models...")
    test_load_models()
    
    print("\n" + "="*60)
    print("[TEST 2] Testing Safe URL (Google.com)")
    print("="*60)
    test_google_prediction()
    
    print("\n" + "="*60)
    print("[TEST 3] Testing Malicious URL")
    print("="*60)
    test_malicious_url()
    
    print("\n" + "="*60)
    print("ALL TESTS COMPLETED!")
    print("="*60)
