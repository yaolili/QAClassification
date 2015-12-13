import numpy as np
from sklearn import svm

f = open("testdata.txt")

f.readline()  # skip the header

data = np.loadtxt(f)

X = data[:, 1:]  # select columns 1 through end

y = data[:, 0]   # select column 0, the stock price

clf = svm.SVC()

clf.fit(X, y)

X_new=[[1,3,4]]

ynew=clf.predict(X_new)
print ynew
