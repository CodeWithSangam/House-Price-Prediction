# 🏠 House Price Prediction using Machine Learning

A simple and beginner-friendly machine learning project that predicts house prices based on key property features like area, number of bedrooms, bathrooms, stories, and parking availability. This project was created as a capstone submission under the AICTE Internship Program.

---

## 📌 Project Overview

Accurately estimating the value of a property is one of the key problems in real estate. Buyers and sellers often struggle to determine the fair market price due to manual guesswork. This system uses historical housing data and a machine learning regression model to predict the price of a house based on user input.

---

## 👨‍💻 Developed By

**Sangam Gupta**  
B.Tech CSE (AI & ML) – KMCLU, Lucknow  
AICTE Student ID: STU61b9808063dff1639547008  
📧 Email: gsangam781@gmail.com

---

## 🧰 Tech Stack

- **Language**: Python  
- **Libraries**:  
  - `pandas`, `numpy` – Data handling  
  - `scikit-learn` – Machine Learning  
  - `joblib` – Model saving/loading  
  - `streamlit` – Web app interface  
- **IDE**: VS Code / Terminal

---

## 📁 Project Structure

house-price-prediction/
├── data/ # Dataset (CSV file)
├── saved_model/ # Trained model & scaler
├── src/ # Source code (training, utilities)
│ ├── train.py
│ ├── utils.py
│ └── predict.py
├── app/ # Optional: Streamlit Web UI
│ └── app.py
├── requirements.txt # Dependencies
└── README.md # This file


---

## 📊 Features Used

- Area (in sq. ft)
- Number of Bedrooms
- Number of Bathrooms
- Number of Stories
- Parking Space

---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/house-price-prediction.git
cd house-price-prediction

python -m venv venv
venv\Scripts\activate    # On Windows

pip install -r requirements.txt

python src/train.py

python predict.py

🏠 Welcome to House Price Predictor!
Enter area in sq ft: 2000
Enter number of bedrooms: 3
Enter number of bathrooms: 2
Enter number of stories: 2
Enter number of parking spaces: 1
💰 Predicted House Price: ₹ 5,500,000.00

