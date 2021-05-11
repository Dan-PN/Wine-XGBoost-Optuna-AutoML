import collections
import numpy as np
import pandas as pd
import xgboost
from sklearn.model_selection import RepeatedKFold, cross_val_score
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# %%
# ----------------------
# define objective
wines = pd.read_csv("wines_encoded.csv", encoding='utf-8')
data_X = wines.drop(columns='points', inplace=False).values
data_Y = wines["points"].values
all_features = wines.drop(columns='points', inplace=False).columns
num_features = len(all_features)

X_train, X_test, y_train, y_test = train_test_split(
    data_X, data_Y, test_size=0.20, random_state=42)

# Select Features
model = xgboost.XGBRegressor(verbosity=2)
# fit
model.fit(X_train, y_train)
print("Model Fitted")

# Calculate Accuracy

# %%
# Select top 100 Most Important Features
sorted_idx = model.feature_importances_.argsort()
selected_features = all_features[sorted_idx][num_features-100:num_features]

data_X_selected = wines[selected_features].values

# Refit Model with Selected Features
model = xgboost.XGBRegressor(verbosity=2)
# fit
model.fit(data_X_selected, data_Y)
print("Model Fitted")

# Calculate Accuracy   -> Demostrate Accuracy Reductions

#plt.barh(all_features[sorted_idx][num_features-25:num_features], model.feature_importances_[sorted_idx][num_features-25:num_features])


# %%
xgboost.plot_importance(model)
# %%
# cross val based on train/test
cv = RepeatedKFold(n_splits=10, n_repeats=3, random_state=42)

# evaluate
scores = cross_val_score(
    model, data_X, data_Y, scoring='neg_mean_absolute_error', cv=cv, n_jobs=-6, verbose=2)

print("MAE: {a}".format(a=abs(scores)))


# %%
np.array(all_features)
# %%
all_features_name = wines.columns
all_features_name

# %%
sorted_idx
# %%
model.feature_importances_[sorted_idx]

# %%
np.array(all_features)[sorted_idx]
# %%
len(all_features)


# %%
model.feature_importances_[sorted_idx][230:244]


# %%
all_features[sorted_idx][230:244]
# %%
