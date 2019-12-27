#-------------------------------------------------------------------------------
# Name:        Tutorial 1: Breast Cancer Classifier (NB)

# Purpose:     getting familiar with Naive Bayes Classifier
#              getting familiar with Sklearn

# Author:      Michael
#
# Created:     27/12/2019
# Copyright:   (c) Michael 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
"""
Breast Cancer Wisconsin Diagnostic Database practice
"""

from sklearn.datasets import load_breast_cancer

"""
this variable works as Dictionary
    key: string
    value: strings, lists and arrays

attributes: data['feature_names']
labels: data['target_names']

"""
data = load_breast_cancer()

# initialise all the parameters:

label_names = data['target_names']
labels = data['target']
feature_names = data['feature_names']
features = data['data']

# test these initilisation
print(label_names)
print(labels[0])
print(feature_names[0])
print(features[0])

# Organising data into sets
# in order to evaluate the quality of our model
# before building the model, it is better to split the data into 2 parts
# (training set and test set)

from sklearn.model_selection import train_test_split

train, test, train_labels, test_labels = train_test_split(features, labels, test_size=0.33, random_state=42)

# Building and Evaluating the model

from sklearn.naive_bayes import GaussianNB
