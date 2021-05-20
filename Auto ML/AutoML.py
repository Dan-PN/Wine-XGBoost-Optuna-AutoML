import pandas as pd
from sklearn.model_selection import train_test_split
from supervised.automl import AutoML

wines = pd.read_csv("wines_encoded.csv", encoding='utf-8')
data_X = wines.drop(columns='points', inplace=False)
data_Y = wines["points"]
all_features = wines.drop(columns='points', inplace=False).columns
num_features = len(all_features)


X_train, X_test, y_train, y_test = train_test_split(data_X, data_Y,
                                                    test_size=0.25, random_state=42)

# train models with AutoML
automl = AutoML(mode="Explain")
automl.fit(X_train, y_train)
