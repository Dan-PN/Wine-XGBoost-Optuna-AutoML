import pandas as pd
import numpy as np
import xgboost
import collections
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RepeatedKFold

# %%
# ----------------------
# define objective
# drop description,taster_twitter_handle also
# Extract year from title
# Extract other details
wines = pd.read_csv("wines_encoded.csv", encoding='utf-8')

data_X = wines.drop(columns='points', inplace=False).values
data_Y = wines["points"].values

# model
model = xgboost.XGBRegressor(verbosity=2)

# fit
model.fit(data_X, data_Y)
print("Model Fitted")

# cross val based on train/test
cv = RepeatedKFold(n_splits=10, n_repeats=3, random_state=42)

# evaluate
scores = cross_val_score(
    model, data_X, data_Y, scoring='neg_mean_absolute_error', cv=cv, n_jobs=-2, verbose=2)

print("MAE: {a}".format(a=abs(scores)))


# %%
#wines.drop(columns='points', inplace=False)

# %%
