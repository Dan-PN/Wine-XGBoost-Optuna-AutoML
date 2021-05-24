# Wine 🍷 Dataset Exploration and XGBoost Regression Hyperparameter Tuning with Optuna

## Classic Take on the [Wine Review Dataset from Kaggle](https://www.kaggle.com/zynicide/wine-reviews)

### Part 1 - EDA Exploration with dataprep
**Objective**: Understand data distribution -> [Python_file_EDA](Wine101.py)// [Notebook_EDA](Wine101_EDA.ipynb)


### Part 2 - Data Extraction / Feature Eng / Data Encoding  
**Objective**: Extract features from text fields, One Hot Encoding of Categorical Features ->> [Data_Processing](Wine_Processing.py)


### Part 3 - Train XGBoost to Predict Wine Score, Parameter Hypertuning with Optuna, Feature Importance

**Objectives**: Train model, tune with bayesian hyperparameter optimization (Optuna), Evaluate feature importance -> [Notebook](XGBoost_optuna_tuned.ipynb) // [Python_file](XGBoost_predict.py) 

- A) Create XGBoost model to predict Wine score based on Wine Origin, Price and description features.

- B) Use Optuna to tune hyperparameters, evaluate the most important hyperparamenters.

- C) Based on tuned parameters evaluate model feature importance.

### Part 4 - AutoMl with [mljar-supervised](https://github.com/mljar/mljar-supervised/)

**Objective**: Run AutoMl on same Wine dataset, compare performance ->[Notebook](https://github.com/Dan-PN/Wine-XGBoost-Optuna/blob/main/Auto%20ML/AutoML.ipynb)
- A) AutoMl as model EDA and Explained -> [Explainer](https://github.com/Dan-PN/Wine-XGBoost-Optuna/tree/main/Auto%20ML/AutoML_1#readme)
- B) AutoML as a powerful model/hyperparameter tuner ->[Model_tuner](AutoML_2/../README.md) // [Optuna_tuner](AutoML_3/../README.md)
