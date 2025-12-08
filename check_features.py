import pickle

# Load model
with open("models/final_random_forest_model.pkl", "rb") as f:
    model = pickle.load(f)

print("Expected feature names from the trained model:")
print("=" * 60)
for i, feature in enumerate(model.feature_names_in_, 1):
    print(f"{i:2d}. '{feature}'")
print("=" * 60)
print(f"Total features: {len(model.feature_names_in_)}")
