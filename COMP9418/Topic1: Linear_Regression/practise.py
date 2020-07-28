import pandas as pd
import sklearn.model_selection
import sklearn.linear_model
import sklearn.metrics
import numpy
import scipy.stats

# Step 1: obtain the dataset data structure from the csv file
dataset = pd.read_csv('Daily_Weather_Observations.csv')

# Step 2: Select the linear features and target value
## 2.1 the target value
y = dataset['Temp_at_3pm'].values.reshape(-1, 1)

## 2.2 the multi-dimensional features
###2.2.1 find all the features that can be linear-related with the target value
selected_features = []
ori_features = list(dataset.keys())
ori_features.remove('Temp_at_3pm')

for feature in ori_features:
    if not isinstance(dataset[feature][0], (int, float)):
        continue
    a = dataset[feature].values.reshape(-1, 1)
    b = y
    correlation, _ = scipy.stats.pearsonr(a, b)
    print(correlation)
    if correlation > 0:
        selected_features.append(feature)

### 2.2.2 generate the feautre matrix
X = dataset[selected_features].values

# Step 3: split the dataset into training set and test set
X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.2, random_state=0)

# Step 4: construct the model object and train
model = sklearn.linear_model.LinearRegression()
model.fit(X_train, y_train)

# obtain and store the coefficient vector and intercept
coefficients = model.coef_
intercept = model.intercept_

# Step 5: test
y_pred = model.predict(X_test)

# obtain the MSE
mse = sklearn.metrics.mean_squared_error(y_test, y_pred)
