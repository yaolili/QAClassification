# -*- coding: utf-8 -*-
from sklearn import tree
import numpy as np
import io,sys
from sklearn import metrics
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier

#引入评价指标

from sklearn.metrics import  accuracy_score  #计算ACC
from sklearn.cross_validation import train_test_split

def calculate_result(actual,pred):  
    m_precision = metrics.precision_score(actual,pred);  
    m_recall = metrics.recall_score(actual,pred);  
    #print 'predict info:'  
    print 'precision:{0:.3f}'.format(m_precision)  
    print 'recall:{0:0.3f}'.format(m_recall);  
    print 'f1-score:{0:.3f}'.format(metrics.f1_score(actual,pred));  


f = open("formatResult_3.txt")

f.readline()  # skip the header

data = np.loadtxt(f)

X = data[:, 1:]  # select columns 1 through end

y = data[:, 0]   # select column 0, the stock price

clf = RandomForestClassifier(n_estimators=10)

print("===performance on TEST===")

# Split the data into a training set and a test set; 分为训练集 检验集

X_train, X_dev, y_train, y_dev = train_test_split(X, y, random_state=0)

clf.fit(X_train,y_train)

y_pred =clf.predict(X_dev)

calculate_result(y_dev,y_pred)

