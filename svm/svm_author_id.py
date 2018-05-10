#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
import numpy as np

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()
# features_train = features_train[:int(len(features_train)/100)] 
# labels_train = labels_train[:int(len(labels_train)/100)] 

from sklearn import svm
clf = svm.SVC(C=10000.0, kernel='rbf')

t0 = time()
clf.fit(features_train, labels_train)
print('training time: ', round(time() - t0, 3), 's')

t1 = time()
pred  = clf.predict(features_test)
print('predicting time: ', round(time() - t1, 3), 's')

from sklearn.metrics import accuracy_score
acc = accuracy_score(pred, labels_test)

print(acc)
y = np.array(pred)
print(np.count_nonzero(y == 1))

#########################################################
### your code goes here ###

#########################################################

