# Heart Disease Prediction System

## AI-Powered Medical Risk Assessment and Disease Prediction

### Project Overview

The Heart Disease Prediction System is a Machine Learning-based healthcare application designed to predict the likelihood of heart disease using patient medical information. The system analyzes various health parameters such as age, blood pressure, cholesterol levels, heart rate, and other clinical indicators to provide an intelligent risk assessment.

The application is developed using Python, Streamlit, Scikit-Learn, Plotly, and ReportLab, providing an interactive dashboard, patient risk assessment module, and downloadable PDF reports.

---

## Objective

To predict the possibility of heart disease based on patient medical data using Machine Learning classification techniques.

---

## Features

* Interactive Dashboard
* Heart Disease Risk Prediction
* AI-Based Medical Risk Assessment
* Feature Importance Analysis
* Patient Information Management
* Risk Percentage Calculation
* Risk Gauge Visualization
* Personalized Health Recommendations
* PDF Report Generation
* User-Friendly Streamlit Interface

---

## Dataset

Dataset Used: Heart Disease Dataset

The dataset contains various medical attributes such as:

* Age
* Sex
* Chest Pain Type
* Resting Blood Pressure
* Cholesterol Level
* Fasting Blood Sugar
* Resting ECG
* Maximum Heart Rate Achieved
* Exercise Induced Angina
* Old Peak
* Slope
* Number of Major Vessels
* Thalassemia
* Target Variable (Heart Disease Presence)

---

## Machine Learning Algorithm

### Random Forest Classifier

Random Forest was selected because:

* High prediction accuracy
* Handles structured medical data effectively
* Reduces overfitting
* Provides feature importance analysis
* Suitable for classification problems

---

## Technology Stack

### Frontend

* Streamlit

### Backend

* Python

### Machine Learning

* Scikit-Learn
* Random Forest Classifier

### Data Analysis

* Pandas
* NumPy

### Visualization

* Plotly

### Report Generation

* ReportLab

---

## Project Structure

CodeAlpha_HeartDiseasePrediction

├── home.py

├── heart.csv

├── README.md

├── requirements.txt

│

└── pages

    ├── 1_Dashboard.py

    └── 2_Patient_Assessment.py

---

## Dashboard Module

The Dashboard provides:

* Dataset Statistics
* Model Accuracy
* Medical Feature Overview
* Age Distribution Analysis
* Heart Disease Distribution Analysis
* Feature Importance Visualization

---

## Patient Assessment Module

The Patient Assessment page allows users to:

* Enter Patient Name
* Enter Patient ID
* Provide Medical Information
* Analyze Heart Disease Risk
* View Risk Percentage
* View Risk Level
* Receive Health Recommendations
* Download PDF Report

---

## Output

The system generates:

* Heart Disease Prediction
* Risk Percentage Score
* Risk Level Classification
* Personalized Recommendations
* Downloadable PDF Medical Report

---

## Installation

Install the required libraries:

pip install pandas numpy scikit-learn streamlit plotly reportlab

---

## Run the Application

streamlit run home.py

---

## Future Enhancements

* Support for Multiple Diseases
* Integration with Real Hospital Data
* Advanced Deep Learning Models
* Cloud Deployment
* Patient History Tracking
* Doctor Recommendation System

---

## Conclusion

The Heart Disease Prediction System demonstrates the application of Machine Learning in healthcare for early disease risk assessment. The project provides an efficient and user-friendly platform for predicting heart disease risk and generating detailed medical reports, helping users make informed healthcare decisions.

---

## Developed For

CodeAlpha Machine Learning Internship

Task 4: Disease Prediction from Medical Data
