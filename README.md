# Customer Churn Prediction using Deep Learning (ANN)

An end-to-end **Deep Learning project** that predicts whether a bank customer is likely to churn based on customer demographic, financial, and account-related information.

The project uses an **Artificial Neural Network (ANN)** built with TensorFlow/Keras and integrates the trained Deep Learning model with a **Streamlit web application** for real-time customer churn prediction.

## 🚀 Live Demo

**Streamlit App:**
https://annproject-z33rxxril6ldyp5sgrhunk.streamlit.app/

## 📌 Project Overview

Customer churn is an important business problem for banks and other customer-focused organizations. Identifying customers who are likely to leave can help businesses take proactive retention measures.

This project develops a **Deep Learning-based binary classification system** that analyzes customer information and predicts the probability of customer churn.

The project covers the complete Deep Learning workflow:

* Data preprocessing
* Exploratory data analysis
* Categorical feature encoding
* Feature scaling
* Artificial Neural Network development
* Deep Learning model training
* Model evaluation
* Model serialization
* Prediction pipeline
* Streamlit application development
* Cloud deployment

## 🎯 Objective

The main objective is to develop an interactive **Deep Learning application** where users can enter customer information and receive a real-time churn prediction along with the predicted probability.

## 🧠 Deep Learning Model

An **Artificial Neural Network (ANN)** built using **TensorFlow/Keras** is used for binary classification.

The trained ANN model learns patterns from customer demographic, financial, and account-related features to estimate the likelihood of customer churn.

The trained model is saved as `churn_model.h5` and loaded during application runtime, allowing the application to generate predictions without retraining the model.

## 📊 Input Features

The Streamlit application accepts the following customer information:

| Feature            | Description                                         |
| ------------------ | --------------------------------------------------- |
| Geography          | Customer's geographical location                    |
| Gender             | Customer gender                                     |
| Age                | Customer age                                        |
| Balance            | Customer account balance                            |
| Credit Score       | Customer credit score                               |
| Estimated Salary   | Estimated customer salary                           |
| Tenure             | Number of years the customer has been with the bank |
| Number of Products | Number of bank products used by the customer        |
| Has Credit Card    | Whether the customer has a credit card              |
| Is Active Member   | Whether the customer is an active bank member       |

## 🔄 Deep Learning Prediction Pipeline

The application follows the same preprocessing pipeline used during model training:

1. User enters customer information through the Streamlit interface.
2. Categorical features are transformed using the saved encoders.
3. Geography is transformed using one-hot encoding.
4. Numerical features are transformed using the saved scaler.
5. The processed features are passed to the trained ANN model.
6. The ANN generates a churn probability.
7. The application displays the final churn prediction and probability.

## 🖥️ Streamlit Web Application

The trained Deep Learning model is integrated into an interactive **Streamlit web application** through `app.py`.

The application provides:

* Interactive dropdowns
* Sliders for numerical inputs
* Number input fields
* Real-time Deep Learning predictions
* Churn probability
* Simple and user-friendly interface

Example prediction:

> **Customer is likely to churn**

along with the corresponding prediction probability.

## 🛠️ Technologies Used

* **Python**
* **TensorFlow**
* **Keras**
* **Artificial Neural Networks (ANN)**
* **Pandas**
* **NumPy**
* **Scikit-learn**
* **Streamlit**
* **Matplotlib**
* **Seaborn**
* **Pickle**

## 📁 Project Structure

```text
ANN_project/
│
├── app.py
├── churn_model.h5
├── scaler.pkl
├── label_encoder_gender.pkl
├── onehot_encoder_geo.pkl
├── Churn_Modelling.csv
├── experiments.ipynb
├── prediction.ipynb
├── requirements.txt
└── README.md
```

## 📦 Important Files

### `app.py`

Contains the Streamlit web application and the complete Deep Learning prediction pipeline.

### `churn_model.h5`

Contains the trained **Artificial Neural Network (ANN)** Deep Learning model.

### `scaler.pkl`

Saved feature scaler used to transform numerical input features before passing them to the ANN.

### `label_encoder_gender.pkl`

Saved label encoder used to transform the Gender feature.

### `onehot_encoder_geo.pkl`

Saved one-hot encoder used to transform the Geography feature.

### `experiments.ipynb`

Contains Deep Learning model development, experimentation, and training work.

### `prediction.ipynb`

Contains prediction-related experimentation and testing.

### `requirements.txt`

Contains the Python dependencies required to run the Deep Learning application.

## ▶️ Run the Project Locally

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

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Streamlit application

```bash
streamlit run app.py
```

The application will open in your browser.

## ☁️ Deployment

The Deep Learning application is deployed using **Streamlit Community Cloud**.

Deployment configuration:

* Repository: `abhashas2/ANN_project`
* Branch: `main`
* Main file: `app.py`

The deployed application loads the trained ANN model and saved preprocessing objects from the GitHub repository.

## 💡 Key Learning Outcomes

Through this Deep Learning project, I worked on:

* Building an end-to-end Deep Learning pipeline
* Understanding and implementing Artificial Neural Networks
* Performing data preprocessing
* Handling categorical and numerical features
* Label encoding and one-hot encoding
* Feature scaling
* Training a binary classification ANN using TensorFlow/Keras
* Saving and loading trained Deep Learning models
* Building a real-time prediction pipeline
* Integrating a Deep Learning model with Streamlit
* Deploying a Deep Learning application to the cloud
* Managing project dependencies using `requirements.txt`
* Using GitHub for version control and project hosting

## 🔮 Future Improvements

Possible improvements for this Deep Learning project include:

* Adding model performance metrics to the web application
* Adding confusion matrix and classification metrics
* Improving probability visualization
* Adding prediction history
* Adding batch prediction using CSV uploads
* Adding model explainability
* Improving the user interface and visualization
* Adding model monitoring
* Adding authentication for production use

## 👨‍💻 Author

**Abhash**

Deep Learning | Machine Learning | Data Science

---

⭐ If you found this project useful, consider giving the repository a star!
