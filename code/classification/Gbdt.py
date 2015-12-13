
# -*- coding: utf-8 -*-
from sklearn import tree
import numpy as np
import io,sys
from sklearn import metrics
from sklearn import svm
from sklearn.ensemble import GradientBoostingClassifier

from sklearn.metrics import  accuracy_score  
from sklearn.cross_validation import train_test_split

def calculate_result(actual,pred):  
    m_precision = metrics.precision_score(actual,pred);  
    m_recall = metrics.recall_score(actual,pred);  
    print 'precision:{0:.3f}'.format(m_precision)  
    print 'recall:{0:0.3f}'.format(m_recall);  
    print 'f1-score:{0:.3f}'.format(metrics.f1_score(actual,pred));  


f = open("formatResult7D.txt")

f.readline()  # skip the header

data = np.loadtxt(f)

X = data[:, 1:]  # select columns 1 through end

y = data[:, 0]   # select column 0, the stock price

X_train, X_dev, y_train, y_dev = train_test_split(X, y, random_state=0)

gbdt = GradientBoostingClassifier()
gbdt.fit(X_train, y_train) 

gbdt_predict_labels = gbdt.predict(X_dev)

calculate_result(y_dev,gbdt_predict_labels)







