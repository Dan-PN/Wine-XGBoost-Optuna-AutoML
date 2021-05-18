# %%#
import plotly
import collections
import numpy as np
import pandas as pd
import xgboost as xgb
from sklearn.model_selection import RepeatedKFold, cross_val_score
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import optuna

# Load Data
wines = pd.read_csv("wines_encoded.csv", encoding='utf-8')
data_X = wines.drop(columns='points', inplace=False).values
data_Y = wines["points"].values
all_features = wines.drop(columns='points', inplace=False).columns
num_features = len(all_features)


# Select  Top Features
model = xgb.XGBRegressor(verbosity=1)
model.fit(data_X, data_Y)
print("Model Fitted")

# Select 100 best features
sorted_idx = model.feature_importances_.argsort()
selected_features = all_features[sorted_idx][num_features-300:num_features]
data_X_selected = wines[selected_features].values
selected_features_names = list(selected_features)

# %%
# Data Prep for XGBoost
X_train_2, X_test_2, y_train_2, y_test_2 = train_test_split(
    data_X_selected, data_Y, test_size=0.25, random_state=42)

# Encode Dmatrix
dtrain = xgb.DMatrix(X_train_2, label=y_train_2,
                     feature_names=selected_features_names)
dtest = xgb.DMatrix(X_test_2, label=y_test_2,
                    feature_names=selected_features_names)


# Set Optimize objective for Optuna and tune hyperparameters
def objective(trial, dtrain, dtest):

    param = {'booster': 'gbtree',
             "verbosity": 1,   # verbose=0   "silent": 0,
             'nthread': 6,
             'objective': 'reg:squarederror',
             'eval_metric': 'rmse',  # rmse   #mae
             'learning_rate': trial.suggest_loguniform('learning_rate', 0.0005, 1),
             'gamma': trial.suggest_loguniform("gamma", 1e-8, 0.5),
             'max_depth': trial.suggest_int('max_depth', 2, 20),
             "lambda": trial.suggest_loguniform("lambda", 1e-8, 3.0),
             "alpha": trial.suggest_loguniform("alpha", 1e-8, 1.0),
             'colsample_bytree': trial.suggest_discrete_uniform('colsample_bytree', 0.5, 1, 0.05)
             }
    # Pruning Callback to stop training
    pruning_callback = optuna.integration.XGBoostPruningCallback(
        trial, 'validation-rmse')

    eval_r = {}
    bst = xgb.train(param, dtrain, evals=[(dtest, "validation")], callbacks=[
                    pruning_callback], evals_result=eval_r)

    return eval_r["validation"][param["eval_metric"]][-1]


study = optuna.create_study(direction="minimize")
study.optimize(lambda trial: objective(trial, dtrain, dtest), n_trials=50)

print("Number of finished trials: {}".format(len(study.trials)))
print("Best trial:")
trial_best = study.best_trial
print("  Value: {}".format(trial_best.value))
print("  Params: ")
for key, value in trial_best.params.items():
    print("    {}: {}".format(key, value))

best_param = trial_best.params

# %%
# Viz of Hyperparameter Search

optuna.visualization.plot_param_importances(study)
# %%
# Viz of Hyperparameter Search
optuna.visualization.plot_optimization_history(study)


# %%
# Train Model with Tuned Parameters
param_basic = {'booster': 'gbtree',
               "verbosity": 1,
               'nthread': 6,
               'objective': 'reg:squarederror',
               "eval_metric": ['rmse', 'mae']
               }

opt_param = {**param_basic, **best_param}


eval_record = {}
f_model = xgb.train(opt_param, dtrain, evals=[
    (dtest, "validation")], evals_result=eval_record)  # num_boost_round=15, early_stopping_rounds=5


# %%
xgb.plot_importance(f_model, importance_type="weight", max_num_features=20)
# %%
xgb.plot_importance(f_model, importance_type="gain", max_num_features=20)
# %%
xgb.plot_importance(f_model, importance_type="cover", max_num_features=20)
