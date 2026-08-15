import streamlit as st
import pandas as pd
import pickle
import numpy as np
from tensorflow.keras.models import load_model


# --------------------------------------------------
# Load trained model and preprocessing objects
# --------------------------------------------------

model = load_model("salary_regression_model.h5")

with open("scaler.pkl", "rb") as file:
    scaler = pickle.load(file)

with open("label_encoder.pkl", "rb") as file:
    label_encoder = pickle.load(file)

with open("onehot_encoder.pkl", "rb") as file:
    onehot_encoder = pickle.load(file)


# --------------------------------------------------
# Streamlit App
# --------------------------------------------------

st.set_page_config(
    page_title="Estimated Salary Prediction",
    page_icon="💰",
    layout="centered"
)

st.title("💰 Estimated Salary Prediction")
st.write(
    "Enter the customer details below to predict the estimated salary "
    "using a Deep Learning ANN regression model."
)


# --------------------------------------------------
# User Inputs
# --------------------------------------------------

credit_score = st.number_input(
    "Credit Score",
    min_value=300,
    max_value=900,
    value=650
)

geography = st.selectbox(
    "Geography",
    onehot_encoder.categories_[0]
)

gender = st.selectbox(
    "Gender",
    label_encoder.classes_
)

age = st.number_input(
    "Age",
    min_value=18,
    max_value=100,
    value=35
)

tenure = st.number_input(
    "Tenure",
    min_value=0,
    max_value=10,
    value=5
)

balance = st.number_input(
    "Balance",
    min_value=0.0,
    value=50000.0
)

num_of_products = st.number_input(
    "Number of Products",
    min_value=1,
    max_value=4,
    value=1
)

has_cr_card = st.selectbox(
    "Has Credit Card",
    [0, 1]
)

is_active_member = st.selectbox(
    "Is Active Member",
    [0, 1]
)

exited = st.selectbox(
    "Exited",
    [0, 1]
)


# --------------------------------------------------
# Prediction
# --------------------------------------------------

if st.button("Predict Estimated Salary"):

    # Encode Gender
    gender_encoded = label_encoder.transform([gender])[0]

    # Create input dataframe
    input_data = pd.DataFrame({
        "CreditScore": [credit_score],
        "Gender": [gender_encoded],
        "Age": [age],
        "Tenure": [tenure],
        "Balance": [balance],
        "NumOfProducts": [num_of_products],
        "HasCrCard": [has_cr_card],
        "IsActiveMember": [is_active_member],
        "Exited": [exited]
    })


    # --------------------------------------------------
    # One-hot encode Geography
    # --------------------------------------------------

    geo_encoded = onehot_encoder.transform(
        [[geography]]
    )

    geo_encoded_df = pd.DataFrame(
        geo_encoded,
        columns=onehot_encoder.get_feature_names_out(
            ["Geography"]
        )
    )


    # Combine input data with Geography encoding
    input_data = pd.concat(
        [
            input_data.reset_index(drop=True),
            geo_encoded_df.reset_index(drop=True)
        ],
        axis=1
    )


    # --------------------------------------------------
    # Scale input data
    # --------------------------------------------------

    input_data_scaled = scaler.transform(input_data)


    # --------------------------------------------------
    # Make prediction
    # --------------------------------------------------

    prediction = model.predict(input_data_scaled)

    predicted_salary = prediction[0][0]


    # --------------------------------------------------
    # Display result
    # --------------------------------------------------

    st.success(
        f"Estimated Salary: ${predicted_salary:,.2f}"
    )

    st.info(
        "Prediction generated using the trained ANN regression model."
    )