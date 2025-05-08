import joblib
import numpy as np

# Load model and scaler
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))  # Go 1 level up
model = joblib.load(os.path.join(BASE_DIR, 'saved_model', 'model.pkl'))
scaler = joblib.load(os.path.join(BASE_DIR, 'saved_model', 'scaler.pkl'))

print("🏠 Welcome to House Price Predictor!")

try:
    area = float(input("Enter area in sq ft (100 - 10000): "))
    bedrooms = int(input("Enter number of bedrooms (1 - 10): "))
    bathrooms = int(input("Enter number of bathrooms (1 - 10): "))
    stories = int(input("Enter number of stories (1 - 4): "))
    parking = int(input("Enter number of parking spaces (0 - 5): "))

    # Input validation with fun touch 😄
    if not (100 <= area <= 10000):
        raise ValueError("❌ Area must be between 100 and 10,000 sq ft — Bhai, Taj Mahal thodi bana rahe ho! 🏰")
    if not (1 <= bedrooms <= 10):
        raise ValueError("❌ Bedrooms must be between 1 and 10 — 22 bedrooms? Are you building a hostel? 😅")
    if not (1 <= bathrooms <= 10):
        raise ValueError("❌ Bathrooms must be between 1 and 10 — Kitne bathrooms chahiye bhai? 😮")
    if not (1 <= stories <= 4):
        raise ValueError("❌ Stories must be between 1 and 4 — Lagta hai Burj Khalifa banana hai! 😂")
    if not (0 <= parking <= 5):
        raise ValueError("❌ Parking spaces must be between 0 and 5 — Itna toh mall mein bhi nahi hota! 🅿️")

    # Prediction
    features = np.array([[area, bedrooms, bathrooms, stories, parking]])
    features_scaled = scaler.transform(features)
    prediction = model.predict(features_scaled)[0]

    if prediction > 10_00_00_000:
        print(f"💰 Predicted House Price: ₹ {prediction:,.2f} (~{int(prediction/1e7)} crore 😅)")
    else:
        print(f"💰 Predicted House Price: ₹ {prediction:,.2f}")

except ValueError as e:
    print(e)
