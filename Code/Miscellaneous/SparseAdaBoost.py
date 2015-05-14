"""Plot the performance of a AdaBoost classifer with two data formats.

Charts the trainning time of a AdaBoost classifier on 20newsgroups data
represented in both sparse and dense format as the number of features
used in the data grows.
"""
from scipy import sparse
import time
import random
from sklearn.datasets import fetch_20newsgroups
from sklearn.ensemble import AdaBoostClassifier
from sklearn.svm import SVC
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

categories = ['alt.atheism', 'talk.religion.misc', 'comp.graphics',
              'sci.space']
remove = ('headers', 'footers', 'quotes')

X = [[0], [1], [2], [3]]
y = [0, 0, 1, 1]

data_train = fetch_20newsgroups(subset='train', categories=categories,
                                shuffle=True, random_state=42, remove=remove)

data_test = fetch_20newsgroups(subset='test', categories=categories,
                               shuffle=True, random_state=42, remove=remove)

# Get label data
Y_train, Y_test = data_train.target, data_test.target

# Get sparse test and train data
vectorizer = None
if False:
    vectorizer = HashingVectorizer(stop_words='english', non_negative=True,
                                   n_features=2**16)
    X_train = vectorizer.transform(data_train.data)
else:
    vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5,
                                 stop_words='english')
    X_train = vectorizer.fit_transform(data_train.data)
X_test = vectorizer.transform(data_test.data)

# slice the data
Y_train = Y_train[0:1000]
X_train = X_train[0:1000, 0:200]
X_test = X_test[:, 0:200]

ada = AdaBoostClassifier(n_estimators=5000, base_estimator=SVC(probability=True),
                         learning_rate=0.01)

# Begin Timing
start = time.clock()
# Train on sparse data
ada.fit(X_train, Y_train)
elapsed_sparse_train = time.clock() - start
print(" Sparse Training time: ", elapsed_sparse_train)

# Begin Timing
start = time.clock()
# Predict on sparse data
ada.predict(X_test[:1000])
elapsed_sparse_predict = time.clock() - start
print(" Sparse Prediciton time: ", elapsed_sparse_predict)

# Densify Data
X_train = X_train.toarray()
X_test = X_test.toarray()

# Begin Timing
start = time.clock()
# Train on dense data
ada.fit(X_train, Y_train)
elapsed_dense_train = time.clock() - start
print(" Dense Training time: ", elapsed_dense_train)

# Begin Timing
start = time.clock()
# Predict on dense data
ada.predict(X_test[:1000])
elapsed_dense_predict = time.clock() - start
print(" Dense Prediciton time: ", elapsed_dense_predict)