# Customer Churn Prediction using ANN

This project predicts whether a customer is likely to churn using an Artificial Neural Network (ANN).

## Project Overview

The model uses customer information such as:

- Credit Score
- Geography
- Gender
- Age
- Tenure
- Balance
- Number of Products
- Credit Card status
- Active Member status
- Estimated Salary

The trained ANN model is used to predict customer churn.

## Technologies Used

- Python
- TensorFlow / Keras
- Scikit-learn
- Pandas
- NumPy
- Streamlit

## Files

- `experiments.ipynb` - Model training and experimentation
- `prediction.ipynb` - Model prediction
- `app.py` - Streamlit web application
- `model.h5` - Trained ANN model
- `scaler.pkl` - Feature scaler
- `label_encoder_gender.pkl` - Gender label encoder
- `onehot_encoder_geo.pkl` - Geography encoder
- `requirements.txt` - Required Python libraries

## How to Run

Install the required libraries:

```bash
pip install -r requirements.txt
