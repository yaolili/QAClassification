# -*- coding: utf-8 -*-

import numpy as np
import os,sys
from sklearn import tree
from sklearn import svm
from sklearn import metrics
from sklearn.preprocessing import Imputer
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.cross_validation import train_test_split
from sklearn.metrics import  accuracy_score  
from sklearn.metrics import confusion_matrix    
from sklearn.neighbors import KNeighborsClassifier


class Classification():
    def __init__(self, classifier, trainFile, devFile):
        f = open(trainFile)
        data = np.loadtxt(f)
        X_train = data[:, 1:]  # select columns 1 through end
        y_train = data[:, 0] 
        f.close()
            
        f = open(devFile)
        pre = np.loadtxt(f)
        X_test = pre[:, 1:]
        
        X_test = Imputer().fit_transform(X_test)
        
        #test usage!
        if np.isnan(X_test).any():
            print "nan in X_test!"
            exit()
            
        self.y_test = pre[:, 0] 
        f.close()
        
        if classifier == 'tree':
            clf = tree.DecisionTreeClassifier()
        elif classifier == 'knn':
            clf = KNeighborsClassifier()
        elif classifier == 'svm':
            clf = svm.SVC(kernel='rbf')
        elif classifier == 'gbdt':
            clf = GradientBoostingClassifier()
        elif classifier == 'essemble':
            clf = RandomForestClassifier(n_estimators=10)
        else:
            print "Invalid classifier in Class Classification __init__()!"
            exit()
        
        clf.fit(X_train, y_train) 
        self.y_pred = clf.predict(X_test)
        #self.calculate_result(self.y_test, self.y_pred)
        #print( "ACC:  %f " %accuracy_score(y_test,y_pred))

        
    def getPreResult(self, outputFile):
        fout = open(outputFile,"w+")
        for each in self.y_pred:
            eachint = int(each)
            fout.write(str(eachint)+"\n")
        fout.close()        
   
    def calculate_result(self):  
        m_precision = metrics.precision_score(self.y_test, self.y_pred)
        m_recall = metrics.recall_score(self.y_test, self.y_pred) 
        print 'precision:{0:.3f}'.format(m_precision)  
        print 'recall:{0:0.3f}'.format(m_recall) 
        print 'f1-score:{0:.3f}'.format(metrics.f1_score(self.y_test, self.y_pred))    
    

    




