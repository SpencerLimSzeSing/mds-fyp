# **MDS FYP**
### Meteorological Variable-Based Daily Rainfall Prediction Using Stacking Ensemble Learning and ANN
## Project Background
Weather has a huge influence on agriculture, disaster management, transportation, and everyday decisions — but rainfall is getting harder to predict as climate patterns shift. Traditional forecasting methods often fall short when it comes to capturing the complex relationships between different weather variables. When rainfall predictions are off, it creates real problems — poor resource planning, agricultural setbacks, and inadequate preparation for extreme weather. A data-driven approach, powered by machine learning & deep learning, can help close that gap.

## 🎯 Project Goal & Objectives
To build a machine learning model that predicts daily rainfall categories based on meteorological data.

Objectives:

- Analyze and preprocess historical weather data to uncover the key factors driving rainfall
- Develop and compare several machine learning models for rainfall classification
- Combine multiple base models using a stacking ensemble approach, with an Artificial Neural Network (ANN) as the meta-learner
- Evaluate performance using accuracy, precision, recall, F1-score, and ROC-AUC
- Deploy the final model through an interactive Streamlit app for real-time rainfall prediction


## ⚙️ Project Structure / Method
**🛠️ Tools, Techniques & Platforms Used**

- **Programming Language:** Python
- **Libraries:** Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn, Folium, TensorFlow/Keras, XGBoost, Imbalanced-learn (SMOTE), Scikeras
- **Models:** Stacking Ensemble (Random Forest, XGBoost, SVC, KNN), ANN (SimpleRNN, Sequential), Logistic Regression (Meta-model)
- **Evaluation Metrics:** Accuracy, Precision, Recall, F1-score, R² Score, MSE, RMSE, MAE

### 1. Dataset
The datasets are sourced from the **Malaysian Meteorological Department (MetMalaysia)**, focusing on regional stations (e.g., Alor Setar, Bayan Lepas, Chuping).

The attributes in the dataset are:
- **Date:** Observation timestamp.
- **Precipitation:** Target variable (Daily rainfall in mm).
- **Temperature (Max/Min):** Daily temperature readings.
- **Relative Humidity:** Average daily humidity percentage.
- **Wind Speed:** Mean daily wind speed.
- **Solar Radiation:** Daily solar exposure.

### 2. Preprocessing
The following preprocessing steps were applied:
- **Missing Value Handling:** Imputation of null values in meteorological records.
- **Feature Scaling:** `StandardScaler` was used to normalize numerical features for ANN and KNN.
- **Encoding:** `LabelEncoder` and `OneHotEncoder` for categorical location data.
- **Class Balancing:** Applied **SMOTE** (Synthetic Minority Over-sampling Technique) to handle the imbalance between "Rain" and "No Rain" days.

### 3. Data Exploration
- Time-series decomposition using `seasonal_decompose` to identify trends.
- Correlation heatmaps using `Seaborn` to find relationships between humidity, temperature, and rainfall.
- Geospatial mapping of stations using `Folium`.

### 4. Modelling
The dataset was split into training and testing sets (80:20). The following models were evaluated:
- **Base Learners:** Random Forest, XGBoost, Support Vector Classifier (SVC), and K-Nearest Neighbors (KNN).
- **Meta-Learner:** Logistic Regression (used to combine base learner predictions).
- **Deep Learning:** Artificial Neural Networks (ANN).

**Evaluation**

| Model Type | Model Name | Accuracy | Key Strength / Performance |
|------|-------------|-------------|------|
| Base Learner 1 | Random Forest (RF) | 82.0% | Best base learner; high recall (0.98) for "Very Heavy Rain" |
| Base Learner 2 | XGBoost (XGB)      | 81.0% | Strong performance in capturing non-linear data patterns. |
| Base Learner 3 | K-Nearest Neighbors (KNN) | 73.0%, | Moderate performance; struggled with "Moderate Rain" category.|
| Meta Learner   | Meta-ANN (Stacking) | 84.0% | Highest overall accuracy; best balance across all rain categories. |
| Benchmark      | Standalone ANN      | 81.0% | Competitive, but had lower recall for the "No Rain" majority class. |


## 📊 Findings
- The **Stacking Ensemble** model significantly outperformed individual base learners by reducing variance and bias.
- **Humidity and Solar Radiation** were identified as the strongest predictors for daily rainfall occurrence.
- The **ANN (RNN)** model showed high capability in capturing temporal dependencies in the meteorological time-series data.

## 🚀 Deployment

The model has been deployed as a web application for real-time rainfall prediction. You can find the deployment source code and configuration in the dedicated repository:

🔗 **Deployment Repository:** [mds-fyp-deploy](https://github.com/SpencerLimSzeSing/mds-fyp-deploy)

🔗 **Streamlit :** [app](https://mds2024.streamlit.app/)

### Key Deployment Features:
- **Platform:** Streamlit / Flask (adjust based on your actual tool).
- **Model Integration:** Uses the pre-trained **Stacking Ensemble (Meta-ANN)** weight files (`.joblib` / `.h5`).
- **Interactive UI:** Users can input meteorological variables (Humidity, Temp, etc.) to receive an instant rainfall intensity classification.


