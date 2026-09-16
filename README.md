# 🎓 Student Dropout Prediction

## 📌 Project Overview

Student Dropout Prediction is a Machine Learning project that predicts whether a student is at risk of dropping out based on student-related information.

The project follows a complete Machine Learning workflow from data exploration and preprocessing to model training, evaluation, and prediction.

## 🎯 Objective

The main objectives of this project are to:

* Predict student dropout.
* Calculate dropout probability.
* Identify the student's risk category.
* Demonstrate how Machine Learning can support an educational early-warning system.

## 📊 Dataset

A publicly available student dataset was used for this project.

The dataset was explored using Python and Pandas to understand its structure, features, data types, and dropout distribution.

**Target Variable:** `Dropout`

## 🧹 Data Preprocessing

The following preprocessing steps were performed:

* Checked missing values
* Checked duplicate records
* Handled missing values
* Identified numerical and categorical features
* Encoded categorical variables
* Scaled numerical features
* Prepared the data for Machine Learning

A preprocessing pipeline was used to apply the required transformations consistently.

## 🔎 Exploratory Data Analysis

Exploratory Data Analysis was performed using:

* Pandas
* Matplotlib
* Seaborn

The analysis examined factors such as:

* GPA
* Attendance
* Study Hours
* Stress Levels
* Dropout distribution
* Relationships between student features and dropout

## 🤖 Machine Learning Model

This is a **classification problem**, so **Logistic Regression** was selected as the Machine Learning model.

The dataset was divided into:

* **80% Training Data**
* **20% Testing Data**

The model was trained using the training dataset and evaluated using the testing dataset.

## 📈 Model Evaluation

The model was evaluated using classification metrics including:

* Accuracy
* Precision
* Recall
* F1-Score
* Confusion Matrix
* ROC-AUC

The actual evaluation results are available in the Jupyter/Colab notebook.

## 🔮 Student Risk Prediction Application

A Machine Learning application was developed to allow users to enter student information and receive a prediction.

The application provides:

* Dropout prediction
* Dropout probability
* Risk category
* Assessment message

### Risk Categories

| Dropout Probability | Risk Category  |
| ------------------- | -------------- |
| Below 30%           | 🟢 Low Risk    |
| 30%–59%             | 🟡 Medium Risk |
| 60% or above        | 🔴 High Risk   |

## 🏫 Educational Early-Warning System

This project demonstrates how Machine Learning can potentially support an educational early-warning system.

The system can provide a risk signal that may help educators identify students who could benefit from additional academic or support services.

The prediction should be considered a decision-support tool rather than a final judgment about an individual student.

## 🔄 Project Workflow

```text
Dataset
   ↓
Data Exploration
   ↓
Data Cleaning
   ↓
Data Preprocessing
   ↓
Exploratory Data Analysis
   ↓
Train/Test Split
   ↓
Logistic Regression
   ↓
Model Evaluation
   ↓
Student Risk Prediction
   ↓
Application Deployment
```

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn
* Gradio
* Google Colab
* GitHub

## 📁 Project Structure

```text
Student-Dropout-Prediction/
│
├── Student_Dropout_Prediction.ipynb
├── README.md
└── requirements.txt
```

## 🌐 Live Application

https://5401b03bfa86aeabb1.gradio.live/

## 📸 Final Prediction

The final application generates a student dropout prediction, dropout probability, and risk category based on the trained Logistic Regression model.

Screenshots of the final application and prediction can be added to this repository.

## 📚 Learning Outcomes

Through this project, I learned how to:

* Explore and understand a dataset
* Clean and preprocess data
* Perform Exploratory Data Analysis
* Train a classification model
* Evaluate Machine Learning performance
* Generate prediction probabilities
* Build a Machine Learning application
* Document and prepare an end-to-end ML project for deployment

## 👩‍💻 Project

**Student Dropout Prediction — Machine Learning Project**
