# Model Files

This directory contains the trained machine learning models:

- `final_random_forest_model.pkl` - Trained Random Forest classifier (245 MB)
- `label_encoder.pkl` - Label encoder for class mapping

## Note

Due to file size limitations, model files are not included in the Git repository. 

### To generate the models:

1. Run the complete notebook: `notebooks/malicious_url_detection.ipynb`
2. The models will be automatically saved in this directory after training

### Download Pre-trained Models

Alternatively, you can download the pre-trained models from:
- [Add your file hosting link here - e.g., Google Drive, Dropbox, or GitHub Releases]

## Model Performance

**Random Forest Model:**
- Accuracy: ~98%
- F1-Score (macro): ~0.97
- Precision (macro): ~0.97
- Recall (macro): ~0.97
