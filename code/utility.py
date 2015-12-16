#-*- coding:utf-8 -*-
# AUTHOR:   yaolili
# FILE:     utility.py
# ROLE:     calculate cosine similarity
# CREATED:  2015-12-12 13:17:46
# MODIFIED: 2015-12-12 13:17:54

import os
import sys
import numpy as np
from scipy import linalg, mat, dot
from sklearn.metrics import pairwise_distances
from scipy.spatial.distance import cosine

class Utility:
    
    '''
    def numpyArray(self, list1, list2):
        aList = []
        aList.append(list(list1))
        aList.append(list(list2))
        return np.array(aList)
        
    def cosine(self, array):
        distance = 1 - pairwise_distances(array, metric="cosine")
        return distance
    '''
          
    def cosine(self, list1, list2):
        a = mat(list1)
        b = mat(list2)
        c = dot(a,b.T)/linalg.norm(a)/linalg.norm(b)
        return c[0,0]
        
        


