# jjj

# %%
import pandas as pd
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from supervised.automl import AutoML
import xgboost as xgb

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

# Select 300 best features
sorted_idx = model.feature_importances_.argsort()
selected_features = all_features[sorted_idx][num_features-300:num_features]
data_X_selected = wines[selected_features]
selected_features_names = list(selected_features)


data_Y_selected = wines["points"]
X_train, X_test, y_train, y_test = train_test_split(data_X_selected, data_Y_selected,
                                                    test_size=0.25, random_state=42)

# train models with AutoML
automl = AutoML(mode="Explain")
automl.fit(X_train, y_train)

predictions = automl.predict(X_test)
print("Test MSE:", mean_squared_error(y_test, predictions))
