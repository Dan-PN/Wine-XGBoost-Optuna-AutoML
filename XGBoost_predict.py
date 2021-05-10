import pandas as pd
import numpy as np
import xgboost
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RepeatedKFold

# Prep data
wines = pd.read_csv("winemag-data-130k-v2.csv")
wines.columns
wines.drop(columns='Unnamed: 0', inplace=True)
wines.dropna(axis='index', subset=['price'], inplace=True)
wines.drop_duplicates(inplace=True)

# define objective
# drop description,taster_twitter_handle also
# Extract year from title
# Extract other details
data_X = wines.drop(columns='points', inplace=False).values
data_Y = wines["points"].values

# model
model = xgboost.XGBRegressor()

# fit
model.fit(data_X, data_Y)

# cross val based on train/test
cv = RepeatedKFold(n_splits=10, n_repeats=3, random_state=42)

# evaluate
scores = cross_val_score(
    model, X, y, scoring='neg_mean_absolute_error', cv=cv, n_jobs=-1)

print("MAE: {a}".format(a=abs(scores)))


# %%
wines.drop(columns='points', inplace=False)
# %%
