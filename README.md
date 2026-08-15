# 🧠 Deep Learning Projects — ANN Classification & Regression

A portfolio of end-to-end **Deep Learning projects** built using **Artificial Neural Networks (ANNs)** with **TensorFlow/Keras** and deployed using **Streamlit**.

This repository contains two real-world Deep Learning applications:

1. **Customer Churn Prediction — Binary Classification**
2. **Estimated Salary Prediction — Regression**

Both projects demonstrate a complete Machine Learning/Deep Learning workflow including:

* Data preprocessing
* Exploratory Data Analysis
* Feature encoding
* Feature scaling
* ANN model development
* Model training
* Model evaluation
* Model serialization
* Prediction pipeline
* Streamlit deployment

---

## 🚀 Projects

## 1️⃣ Customer Churn Prediction — ANN Classification

A Deep Learning-based binary classification application that predicts whether a bank customer is likely to churn.

### 🎯 Objective

The objective is to predict the probability of customer churn using demographic, financial, and account-related information.

The model can help identify customers who may be likely to leave a bank, allowing businesses to take proactive customer-retention measures.

### 🧠 Technology Stack

* Python
* NumPy
* Pandas
* Scikit-learn
* TensorFlow
* Keras
* Streamlit
* Pickle
* Jupyter Notebook

### 📊 Input Features

| Feature            | Description                              |
| ------------------ | ---------------------------------------- |
| Credit Score       | Customer credit score                    |
| Geography          | Customer's geographical location         |
| Gender             | Customer gender                          |
| Age                | Customer age                             |
| Tenure             | Number of years with the bank            |
| Balance            | Customer account balance                 |
| Number of Products | Number of bank products used             |
| Has Credit Card    | Whether the customer has a credit card   |
| Is Active Member   | Whether the customer is an active member |
| Estimated Salary   | Customer's estimated salary              |

### 🔄 Prediction Pipeline

1. User enters customer information through the Streamlit interface.
2. Gender is transformed using a saved Label Encoder.
3. Geography is transformed using One-Hot Encoding.
4. Numerical features are scaled using the saved StandardScaler.
5. The processed input is passed to the trained ANN.
6. The model generates a churn probability.
7. The application displays whether the customer is likely to churn.

### 🧠 Model

The classification model is an Artificial Neural Network built using TensorFlow/Keras.

The final output layer uses a **Sigmoid activation function** to produce a probability between 0 and 1.

### 🌐 Live Streamlit App

👉 **Customer Churn Prediction:**
https://annproject-z33rxxril6ldyp5sgrhunk.streamlit.app/

---

# 2️⃣ Estimated Salary Prediction — ANN Regression

A Deep Learning-based regression application that predicts a customer's **Estimated Salary** using an Artificial Neural Network.

### 🎯 Objective

The objective is to learn the relationship between customer demographic, financial, and banking-related features and predict the customer's estimated salary.

### 📊 Input Features

| Feature            | Description                              |
| ------------------ | ---------------------------------------- |
| Credit Score       | Customer credit score                    |
| Geography          | Customer's geographical location         |
| Gender             | Customer gender                          |
| Age                | Customer age                             |
| Tenure             | Number of years with the bank            |
| Balance            | Customer account balance                 |
| Number of Products | Number of bank products used             |
| Has Credit Card    | Whether the customer has a credit card   |
| Is Active Member   | Whether the customer is an active member |
| Exited             | Whether the customer exited the bank     |

### 🎯 Target Variable

```text
EstimatedSalary
```

### 🧠 Model Architecture

The regression model is an Artificial Neural Network built using TensorFlow/Keras.

The network contains:

* Input Layer
* Dense Layer — 64 neurons
* ReLU Activation
* Dense Layer — 32 neurons
* ReLU Activation
* Output Layer — 1 neuron
* Linear Activation

### 📉 Loss & Evaluation

The model is trained using:

* **Loss Function:** Mean Squared Error (MSE)
* **Evaluation Metric:** Mean Absolute Error (MAE)

### 🔄 Prediction Pipeline

1. User provides customer information.
2. Categorical variables are encoded.
3. Numerical features are scaled.
4. Preprocessed features are passed to the trained ANN.
5. The model predicts the estimated salary.
6. The predicted salary is displayed through the Streamlit interface.

### 🌐 Live Streamlit App

👉 **Estimated Salary Prediction:**
`PASTE-YOUR-REGRESSION-STREAMLIT-LINK-HERE`

---

# 📁 Repository Structure

```text
ANN_project/
│
├── Churn_Modelling.csv
│
├── experiments.ipynb
│   └── ANN Classification experiments
│
├── prediction.ipynb
│   └── Classification prediction pipeline
│
├── salary_regression.ipynb
│   └── ANN Regression model development
│
├── app.py
│   └── Streamlit application for churn prediction
│
├── churn_model.h5
│   └── Trained ANN classification model
│
├── salary_regression_model.h5
│   └── Trained ANN regression model
│
├── scaler.pkl
│   └── Feature scaling object
│
├── label_encoder_gender.pkl
│   └── Gender Label Encoder
│
├── onehot_encoder_geo.pkl
│   └── Geography One-Hot Encoder
│
├── requirements.txt
│   └── Project dependencies
│
├── customer_churn_prediction.pdf
│   └── Project documentation
│
└── README.md
```

---

# 🛠️ Installation & Usage

### 1. Clone the repository

```bash
git clone https://github.com/abhashas2/ANN_project.git
cd ANN_project
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

**Linux/Mac:**

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Streamlit application

```bash
streamlit run app.py
```

---

# 📚 Key Concepts Demonstrated

* Artificial Neural Networks
* Binary Classification
* Regression
* TensorFlow/Keras
* Dense Neural Networks
* Activation Functions
* ReLU
* Sigmoid
* Linear Activation
* Forward Propagation
* Backpropagation
* Loss Functions
* MSE
* MAE
* Feature Scaling
* Label Encoding
* One-Hot Encoding
* Model Serialization
* Pickle
* Streamlit Deployment
* End-to-End Deep Learning Pipeline

---

# 📈 Learning Outcomes

Through these projects, the following concepts were implemented practically:

* Building ANN models from scratch using TensorFlow/Keras
* Preparing structured datasets for Deep Learning
* Handling categorical and numerical features
* Applying feature encoding and scaling
* Training classification and regression networks
* Saving and loading trained models
* Building reusable prediction pipelines
* Creating interactive Streamlit applications
* Deploying Deep Learning models as web applications

---

# 🔗 Important Links

### 💻 GitHub Repository

https://github.com/abhashas2/ANN_project

### 🚀 Classification — Customer Churn

https://annproject-z33rxxril6ldyp5sgrhunk.streamlit.app/

### 🚀 Regression — Estimated Salary

`PASTE-YOUR-REGRESSION-STREAMLIT-LINK-HERE`

---

# 👨‍💻 Author

**Abhash**
IIT Bhubaneswar

---

⭐ If you find this project useful, consider giving the repository a star!
