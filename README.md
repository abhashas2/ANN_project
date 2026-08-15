# 🧠 Deep Learning Projects — ANN Classification & Regression

A portfolio of end-to-end **Deep Learning projects** built using **Artificial Neural Networks (ANNs)** with TensorFlow/Keras and deployed as interactive **Streamlit web applications**.

This repository demonstrates two real-world Deep Learning use cases:

1. **Customer Churn Prediction — Binary Classification**
2. **Estimated Salary Prediction — Regression**

Both projects follow a complete Deep Learning workflow including data preprocessing, feature engineering, model training, evaluation, model serialization, prediction pipelines, Streamlit integration, and cloud deployment.

---

# 🚀 Projects

## 1️⃣ Customer Churn Prediction — ANN Classification

A Deep Learning-based binary classification application that predicts whether a bank customer is likely to churn.

### 🎯 Objective

The objective is to predict the probability of customer churn using demographic, financial, and account-related information.

The model can help identify customers who may be likely to leave a bank, allowing businesses to take proactive customer-retention measures.

### 🧠 Model

An **Artificial Neural Network (ANN)** built using **TensorFlow/Keras** is used for binary classification.

The trained ANN learns patterns from customer information and outputs a probability representing the likelihood of customer churn.

### 📊 Input Features

| Feature | Description |
|---|---|
| Geography | Customer's geographical location |
| Gender | Customer gender |
| Age | Customer age |
| Balance | Customer account balance |
| Credit Score | Customer credit score |
| Estimated Salary | Customer's estimated salary |
| Tenure | Number of years with the bank |
| Number of Products | Number of bank products used |
| Has Credit Card | Whether the customer has a credit card |
| Is Active Member | Whether the customer is an active bank member |

### 🔄 Prediction Pipeline

1. User enters customer information through the Streamlit interface.
2. Categorical features are encoded using saved encoders.
3. Geography is transformed using one-hot encoding.
4. Numerical features are transformed using the saved scaler.
5. The processed features are passed to the trained ANN.
6. The ANN generates a churn probability.
7. The application displays the final prediction and probability.

### 🖥️ Streamlit Application

The application is implemented using `app.py`.

The application provides:

- Interactive dropdowns
- Sliders
- Number input fields
- Real-time predictions
- Churn probability
- User-friendly interface

### 🌐 Live Demo

**Customer Churn Prediction App:**

https://annproject-z33rxxril6ldyp5sgrhunk.streamlit.app/

---

# 2️⃣ Estimated Salary Prediction — ANN Regression

A Deep Learning-based regression application that predicts a customer's **Estimated Salary** using an Artificial Neural Network.

### 🎯 Objective

The objective is to build a regression model that learns relationships between customer demographic, financial, and banking-related features and predicts the customer's estimated salary.

### 🧠 Model

An **Artificial Neural Network (ANN)** built using **TensorFlow/Keras** is used for regression.

The network contains:

- Dense layer with 64 neurons
- ReLU activation
- Dense layer with 32 neurons
- ReLU activation
- Output layer with 1 neuron
- Linear activation for continuous salary prediction

The model is trained using **Mean Squared Error (MSE)** as the loss function and **Mean Absolute Error (MAE)** as an evaluation metric.

### 📊 Input Features

The salary regression model uses customer-related features including:

| Feature | Description |
|---|---|
| Geography | Customer's geographical location |
| Gender | Customer gender |
| Age | Customer age |
| Credit Score | Customer credit score |
| Tenure | Number of years with the bank |
| Balance | Customer account balance |
| Number of Products | Number of bank products used |
| Has Credit Card | Whether the customer has a credit card |
| Is Active Member | Whether the customer is an active bank member |
| Exited | Whether the customer exited the bank |

### 🎯 Target Variable

The target variable for this regression problem is:

```text
EstimatedSalary
