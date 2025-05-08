
import streamlit as st
import numpy as np
import pickle

with open('saved_model/model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('saved_model/scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

st.title("🏠 House Price Prediction App")

area = st.number_input("Area (in sq ft)", min_value=300, step=100)
bedrooms = st.number_input("Number of Bedrooms", min_value=1, max_value=10)
bathrooms = st.number_input("Number of Bathrooms", min_value=1, max_value=10)
stories = st.number_input("Number of Stories", min_value=1, max_value=4)
parking = st.number_input("Parking Spaces", min_value=0, max_value=5)

if st.button("Predict Price"):
    features = np.array([[area, bedrooms, bathrooms, stories, parking]])
    features_scaled = scaler.transform(features)
    price = model.predict(features_scaled)[0]
    st.success(f"🏷️ Estimated House Price: ₹ {round(price, 2)}")
