# %%
import pandas as pd
import numpy as np
import xgboost

from dataprep.eda import plot
from dataprep.eda import plot_correlation
from dataprep.eda import plot_missing


import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="whitegrid", color_codes=True)
sns.set(font_scale=1)

# %%  RUN EDA
wines = pd.read_csv("winemag-data-130k-v2.csv")
# %%  #Overall Distribution
plot(wines)
# %%  # Price Dist -> Clean
plot(wines, "price")

# %%
plot(wines, "points")

# %%
plot(wines, "price", "points")

# %%
plot_correlation(wines, "price", "points")
# %%
plot_missing(wines)
# %%
plot_missing(wines, "price", "points")  # <-cool

# %%
