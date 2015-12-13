# -*- coding: utf-8 -*-
 #使用SVM  分类器
import numpy as np
import io,sys
from sklearn import metrics

from sklearn import svm


#将数据集分为训练集、检验集

from sklearn.cross_validation import train_test_split

from sklearn import cross_validation

#引入评价指标

from sklearn.metrics import confusion_matrix    #计算混淆矩阵
from sklearn.metrics import  accuracy_score  #计算ACC

def calculate_result(actual,pred):  
    m_precision = metrics.precision_score(actual,pred);  
    m_recall = metrics.recall_score(actual,pred);  
    #print 'predict info:'  
    print 'precision:{0:.3f}'.format(m_precision)  
    print 'recall:{0:0.3f}'.format(m_recall);  
    print 'f1-score:{0:.3f}'.format(metrics.f1_score(actual,pred));  


#引入数据


fr_n = open("formatResult_2.txt")

fr_n.readline()  # skip the header

data = np.loadtxt(fr_n)

X = data[:, 1:]  # select columns 1 through end

y = data[:, 0]   # select column 0, the stock price

f = open("predict.txt")

f.readline()  # skip the header

pre = np.loadtxt(f)

X_test = pre[:, 1:]  # select columns 1 through end

y_test = pre[:, 0]   # select column 0, the stock price


# Run classifier  

#print("===cross validation===")

#clf = svm.SVC(kernel='rbf')

#scores=cross_validation.cross_val_score(clf,X,y,cv=3,scoring="accuracy")

#print(scores,scores.mean())


print("===performance on TEST===")

# Split the data into a training set and a test set; 分为训练集 检验集

X_train, X_dev, y_train, y_dev = train_test_split(X, y, random_state=0)

clf= svm.SVC(kernel='rbf')

clf.fit(X_train,y_train)

y_pred =clf.predict(X_dev)

calculate_result(y_dev,y_pred)

#y_testResult=clf.predict(X_test)

#print "结果长度："
#print len(y_testResult)
#print y_testResult

fout=open("Result.txt","w")
for each in y_pred:
	fout.write(str(each)+"\n")



