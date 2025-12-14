# Model Files


## Overview

This directory is intended to store the trained machine learning models for the Malicious URL Detection project.

**Included model files (when available):**
- `final_random_forest_model.pkl` — Trained Random Forest classifier (~245 MB)
- `label_encoder.pkl` — Label encoder for class mapping

---

## Download Pre-trained Models

Due to file size limitations, model files are not included in the Git repository.

You can download the pre-trained models from the following secure link:

👉 [Download Pre-trained Models (Google Drive)](https://drive.google.com/drive/folders/1Yyc8jiJUFvVebtVE6Ojnpnob75s1dbiP?usp=sharing)

---


## How to Generate Models Locally

If you prefer to train the models yourself:
1. Run the notebook: `notebooks/malicious_url_detection.ipynb`
2. The trained models will be saved automatically in this directory after training completes.

---

## Model Performance (Reference)

**Random Forest Model:**
- Accuracy: ~98%
- F1-Score (macro): ~0.97
- Precision (macro): ~0.97
- Recall (macro): ~0.97
