import pandas
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import numpy

# step 1: Create the dataset from reading csv file
dataset = pandas.read_csv('Daily_Weather_Observations.csv')

# Step 2: create the training data with labels
selected_features = {'Year':[], 'Month':[], 'Day':[]}
labels = dataset['Wind_dir_at_3pm'].values

# Step 3: Encode the values of the features and the labels
## 3.1 encode the feature values
for feature in selected_features.keys():
    values = list(dataset[feature].values)
    feature_encoder = preprocessing.LabelEncoder()
    encoded_values = list(feature_encoder.fit_transform(values))
    selected_features[feature] = encoded_values
encoded_features = list(zip(selected_features['Year'], selected_features['Month'], selected_features['Day']))

## 3.2 encode the label values
label_encoder = preprocessing.LabelEncoder()
labels_encoded = list(label_encoder.fit_transform(labels))

# Step 4: split the selected dataset into training and test data
X_train, X_test, y_train, y_test = train_test_split(encoded_features, labels_encoded, test_size=0.1, random_state=0)

# Step 5: Create the KNN model and train the training data
model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train, y_train)

# Step 6: Predict the labels for test data
y_pred = model.predict(X_test)


    
    

