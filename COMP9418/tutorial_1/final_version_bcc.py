from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# load the dataset
data = load_breast_cancer()

# organise the data
label_names = data['target_names']
labels = data['target']
feature_names = data['feature_names']
features = data['data']

# split the data into training and testing
train, test, training_labels, testing_labels = train_test_split(features, labels,
test_size=0.33, random_state=42)

# construct the model
gnb = GaussianNB()
model = gnb.fit(train, training_labels)

# make prediction
pred = model.predict(test)

# evaluate the accuracy
acc = accuracy_score(testing_labels, pred)

print(acc)
