
import pickle
from utils import load_data, preprocess_data
from sklearn.linear_model import LinearRegression

df = load_data('data/housing.csv')
(X_train, X_test, y_train, y_test), scaler = preprocess_data(df)

model = LinearRegression()
model.fit(X_train, y_train)

with open('saved_model/model.pkl', 'wb') as f:
    pickle.dump(model, f)

with open('saved_model/scaler.pkl', 'wb') as f:
    pickle.dump(scaler, f)

print("✅ Model trained and saved successfully.")
