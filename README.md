# Wine 🍷 Dataset Exploration and XGBoost Regression Hyperparameter Tuning with Optuna

## Classic Take on the [Wine Review Dataset from Kaggle](https://www.kaggle.com/zynicide/wine-reviews)

### Part 1 - EDA Exploration with dataprep ->> Wine101.py // Wine101_EDA.ipynb
Objective: Understand data distribution ->> Wine101.py // Wine101_EDA.ipynb

### Part 2 - Data Extraction / Feature Eng / Data Encoding  ->> Wine_Processing.py
Objective: Extract features from text fields, One Hot Encoding of Categorical Features ->> Wine_Processing.py

### Part 3 - Train XGBoost to Predict Wine Score, Parameter Hypertuning with Optuna, Feature Importance   ->> XGBoost_optuna_tuned.ipynb // XGBoost_predict.py 
Objectives:

A) Create XGBoost model to predict Wine score based on Wine Origin, Price and description features.

B) Use Optuna to tune hyperparameters, evaluate the most important hyperparamenters.

C) Based on tuned parameters evaluate model feature importance.
