import streamlit as st
import pickle
import pandas as pd
import numpy as np
from urllib.parse import urlparse
import re
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="AI URL Security Scanner",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for modern styling with animations
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    .main {
        padding: 1rem 2rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    .stApp {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
    }
    
    .content-card {
        background: white;
        border-radius: 20px;
        padding: 2rem;
        box-shadow: 0 20px 60px rgba(0,0,0,0.3);
        margin: 1rem 0;
    }
    
    .prediction-box {
        padding: 3rem;
        border-radius: 20px;
        margin: 2rem 0;
        text-align: center;
        box-shadow: 0 10px 40px rgba(0,0,0,0.2);
        animation: slideIn 0.5s ease-out;
        position: relative;
        overflow: hidden;
    }
    
    @keyframes slideIn {
        from {
            opacity: 0;
            transform: translateY(-30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .benign {
        background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
        color: white;
    }
    
    .malicious {
        background: linear-gradient(135deg, #ee0979 0%, #ff6a00 100%);
        color: white;
    }
    
    .phishing {
        background: linear-gradient(135deg, #fc4a1a 0%, #f7b733 100%);
        color: white;
    }
    
    .malware {
        background: linear-gradient(135deg, #c21500 0%, #ffc500 100%);
        color: white;
    }
    
    .feature-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 15px;
        margin: 0.5rem 0;
        color: white;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        transition: transform 0.3s ease;
    }
    
    .feature-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.2);
    }
    
    .metric-container {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        padding: 1.5rem;
        border-radius: 15px;
        text-align: center;
        color: white;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    }
    
    .stButton>button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.75rem 2rem;
        font-weight: 600;
        font-size: 16px;
        transition: all 0.3s ease;
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.3);
    }
    
    .stTextInput>div>div>input {
        border-radius: 10px;
        border: 2px solid #667eea;
        padding: 1rem;
        font-size: 16px;
    }
    
    .sidebar .sidebar-content {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    .stats-badge {
        display: inline-block;
        background: white;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        margin: 0.25rem;
        font-weight: 600;
        color: #667eea;
        box-shadow: 0 3px 10px rgba(0,0,0,0.1);
    }
    
    .pulse {
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0% {
            box-shadow: 0 0 0 0 rgba(102, 126, 234, 0.7);
        }
        70% {
            box-shadow: 0 0 0 15px rgba(102, 126, 234, 0);
        }
        100% {
            box-shadow: 0 0 0 0 rgba(102, 126, 234, 0);
        }
    }
    
    .glow {
        box-shadow: 0 0 20px rgba(102, 126, 234, 0.5);
    }
    
    h1, h2, h3 {
        color: white !important;
        font-weight: 700 !important;
    }
    
    .stMarkdown {
        color: white;
    }
    
    div[data-testid="stExpander"] {
        background: white;
        border-radius: 15px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

# Helper functions for feature extraction
@st.cache_data
def load_models():
    """Load the trained model and label encoder"""
    try:
        with open("models/final_random_forest_model.pkl", "rb") as f:
            model = pickle.load(f)
        with open("models/label_encoder.pkl", "rb") as f:
            label_encoder = pickle.load(f)
        return model, label_encoder
    except Exception as e:
        st.error(f"Error loading models: {e}")
        return None, None

def having_ip_address(url):
    """Check if URL contains an IP address"""
    match = re.search(
        r'(([01]?\d\d?|2[0-4]\d|25[0-5])\.([01]?\d\d?|2[0-4]\d|25[0-5])\.([01]?\d\d?|2[0-4]\d|25[0-5])\.([01]?\d\d?|2[0-4]\d|25[0-5])\/'
        r'([01]?\d\d?|2[0-4]\d|25[0-5])\.([01]?\d\d?|2[0-4]\d|25[0-5])\.([01]?\d\d?|2[0-4]\d|25[0-5])\.([01]?\d\d?|2[0-4]\d|25[0-5]))',
        url
    )
    return 1 if match else 0

def abnormal_url(url):
    """Check if URL hostname is present in URL"""
    hostname = urlparse(url).hostname
    if hostname:
        return 0 if hostname in url else 1
    return 1

def count_directories(url):
    """Count number of directories in URL path"""
    urldir = urlparse(url).path
    return urldir.count('/')

def shortening_service(url):
    """Check if URL uses a shortening service"""
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

def http_secure(url):
    """Check if URL uses HTTPS"""
    return 1 if urlparse(url).scheme == 'https' else 0

def count_embedded_domains(url):
    """Count embedded domains in URL"""
    urldir = urlparse(url).path
    return urldir.count('//')

def first_dir_length(url):
    """Get length of first directory in URL"""
    urlpath = urlparse(url).path
    try:
        return len(urlpath.split('/')[1]) if len(urlpath.split('/')) > 1 else 0
    except:
        return 0

def tld_length(url):
    """Get length of top-level domain"""
    try:
        from tld import get_tld
        tld = get_tld(url, fail_silently=True)
        return len(tld) if tld else 0
    except:
        return 0

def suspicious_words(url):
    """Count suspicious words in URL"""
    match = re.search(
        r'PayPal|login|signin|bank|account|update|free|lucky|service|bonus|ebayisapi|webscr',
        url
    )
    return 1 if match else 0

def digit_count(url):
    """Count digits in URL"""
    return sum(c.isdigit() for c in url)

def letter_count(url):
    """Count letters in URL"""
    return sum(c.isalpha() for c in url)

def extract_url_features(url):
    """Extract all features from a URL"""
    features = {}
    
    # Basic lexical features
    features['url_length'] = len(url)
    hostname = urlparse(url).netloc
    features['hostname_length'] = len(hostname)
    features['count_letters'] = letter_count(url)
    features['count_digits'] = digit_count(url)
    
    # Special characters
    special_chars = ['@', '?', '-', '=', '.', '#', '%', '+', '$', '!', '*', ',', '//']
    for ch in special_chars:
        features[f"count_{ch.replace('//', 'slashes')}"] = url.count(ch)
    
    features['count_www'] = url.count('www')
    
    # Domain-based features
    features['has_ip'] = having_ip_address(url)
    features['abnormal_url'] = abnormal_url(url)
    features['short_url'] = shortening_service(url)
    features['https'] = http_secure(url)
    features['count_dir'] = count_directories(url)
    features['count_embed_domain'] = count_embedded_domains(url)
    features['fd_length'] = first_dir_length(url)
    features['tld_length'] = tld_length(url)
    features['suspicious'] = suspicious_words(url)
    
    return pd.DataFrame([features])

def get_risk_level(label):
    """Map label to risk level and color"""
    risk_mapping = {
        'benign': ('✅ SAFE', 'Low Risk', '#10b981', 'benign'),
        'phishing': ('⚠️ PHISHING', 'High Risk', '#ef4444', 'malicious'),
        'malware': ('☠️ MALWARE', 'Critical Risk', '#dc2626', 'malicious'),
        'defacement': ('🚨 DEFACEMENT', 'High Risk', '#f59e0b', 'malicious')
    }
    return risk_mapping.get(label.lower(), ('⚠️ UNKNOWN', 'Unknown', '#6b7280', 'malicious'))

# Main app
def main():
    # Header
    st.title("🔒 Malicious URL Detection System")
    st.markdown("### Powered by Machine Learning")
    st.markdown("---")
    
    # Sidebar
    with st.sidebar:
        st.header("📊 About")
        st.info(
            """
            This application uses a **Random Forest** machine learning model 
            trained on 651,191 URLs to detect:
            - ✅ Benign URLs
            - ⚠️ Phishing attempts
            - ☠️ Malware distribution
            - 🚨 Website defacement
            
            **Accuracy:** ~98%
            """
        )
        
        st.header("🎯 How to Use")
        st.markdown(
            """
            1. Enter a URL in the text box
            2. Click **Analyze URL**
            3. View the prediction and features
            4. Check the confidence score
            """
        )
        
        st.header("👤 Developer")
        st.markdown(
            """
            **Mohammad Hamim**  
            Student ID: 202280090114  
            Network Security Course
            """
        )
    
    # Load models
    model, label_encoder = load_models()
    
    if model is None or label_encoder is None:
        st.error("⚠️ Failed to load models. Please ensure model files exist in the 'models/' directory.")
        return
    
    # Main content
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("🔍 Enter URL to Analyze")
        url_input = st.text_input(
            "URL",
            placeholder="https://example.com",
            help="Enter the complete URL including http:// or https://"
        )
        
        analyze_button = st.button("🚀 Analyze URL", type="primary", use_container_width=True)
    
    with col2:
        st.subheader("📝 Examples")
        example_urls = {
            "Safe URL": "https://www.google.com",
            "Suspicious": "http://bit.ly/suspicious123",
            "Test URL": "http://example-login-bank.com"
        }
        
        for label, url in example_urls.items():
            if st.button(label, use_container_width=True):
                url_input = url
                st.rerun()
    
    # Analysis
    if analyze_button and url_input:
        with st.spinner("🔄 Analyzing URL..."):
            try:
                # Extract features
                features_df = extract_url_features(url_input)
                
                # Make prediction
                prediction = model.predict(features_df)[0]
                prediction_proba = model.predict_proba(features_df)[0]
                label = label_encoder.inverse_transform([prediction])[0]
                confidence = prediction_proba[prediction] * 100
                
                # Get risk information
                verdict, risk_level, color, css_class = get_risk_level(label)
                
                # Display results
                st.markdown("---")
                st.subheader("📊 Analysis Results")
                
                # Prediction box
                st.markdown(
                    f"""
                    <div class="prediction-box {css_class}">
                        <h1>{verdict}</h1>
                        <h3>{risk_level}</h3>
                        <h2>Confidence: {confidence:.2f}%</h2>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                
                # Detailed results
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.metric("Classification", label.upper())
                
                with col2:
                    st.metric("Confidence Score", f"{confidence:.2f}%")
                
                with col3:
                    st.metric("Risk Level", risk_level)
                
                # Probability distribution
                st.subheader("📈 Prediction Probabilities")
                prob_df = pd.DataFrame({
                    'Category': label_encoder.classes_,
                    'Probability': prediction_proba * 100
                }).sort_values('Probability', ascending=False)
                
                st.bar_chart(prob_df.set_index('Category'))
                
                # Feature analysis
                with st.expander("🔬 Detailed Feature Analysis", expanded=False):
                    st.subheader("Extracted Features")
                    
                    # Key features
                    col1, col2, col3 = st.columns(3)
                    
                    with col1:
                        st.markdown("#### 📏 Basic Features")
                        st.markdown(f"**URL Length:** {features_df['url_length'].values[0]}")
                        st.markdown(f"**Hostname Length:** {features_df['hostname_length'].values[0]}")
                        st.markdown(f"**Letter Count:** {features_df['count_letters'].values[0]}")
                        st.markdown(f"**Digit Count:** {features_df['count_digits'].values[0]}")
                    
                    with col2:
                        st.markdown("#### 🔐 Security Features")
                        st.markdown(f"**HTTPS:** {'Yes ✅' if features_df['https'].values[0] else 'No ❌'}")
                        st.markdown(f"**Has IP:** {'Yes ⚠️' if features_df['has_ip'].values[0] else 'No ✅'}")
                        st.markdown(f"**Shortened URL:** {'Yes ⚠️' if features_df['short_url'].values[0] else 'No ✅'}")
                        st.markdown(f"**Suspicious Words:** {'Yes ⚠️' if features_df['suspicious'].values[0] else 'No ✅'}")
                    
                    with col3:
                        st.markdown("#### 📂 Structure Features")
                        st.markdown(f"**Directory Count:** {features_df['count_dir'].values[0]}")
                        st.markdown(f"**TLD Length:** {features_df['tld_length'].values[0]}")
                        st.markdown(f"**Embedded Domains:** {features_df['count_embed_domain'].values[0]}")
                        st.markdown(f"**Special Chars:** {features_df['count_@'].values[0] + features_df['count_?'].values[0]}")
                    
                    # All features table
                    st.markdown("#### 📋 All Features")
                    features_display = features_df.T
                    features_display.columns = ['Value']
                    st.dataframe(features_display, use_container_width=True)
                
                # Recommendations
                st.subheader("💡 Recommendations")
                if label.lower() == 'benign':
                    st.success("✅ This URL appears to be safe. However, always exercise caution when clicking unknown links.")
                else:
                    st.error(
                        f"""
                        ⚠️ **WARNING: This URL is classified as {label.upper()}**
                        
                        **Do NOT:**
                        - Click on this link
                        - Enter personal information
                        - Download any files
                        
                        **Recommended Actions:**
                        - Report to your IT security team
                        - Block this domain
                        - Delete any emails containing this link
                        """
                    )
                
            except Exception as e:
                st.error(f"❌ Error analyzing URL: {str(e)}")
                st.info("Please ensure the URL is properly formatted (e.g., https://example.com)")
    
    elif analyze_button:
        st.warning("⚠️ Please enter a URL to analyze")
    
    # Footer
    st.markdown("---")
    st.markdown(
        """
        <div style='text-align: center; color: #666;'>
            <p>🔒 <strong>Malicious URL Detection System</strong> | Powered by Random Forest ML</p>
            <p>Network Security Course Project | Mohammad Hamim (202280090114)</p>
        </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
