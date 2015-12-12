#-*- coding:utf-8 -*-
# AUTHOR:   yaolili
# FILE:     readW2V.py
# ROLE:     TODO (some explanation)
# CREATED:  2015-12-12 14:23:23
# MODIFIED: 2015-12-12 14:23:31

import sys
import os
import numpy as np
from utility import Utility

class W2V:
    def __init__(self, inputFile):
        self.vector = {}
        with open(inputFile) as fin:
            for lineNum, line in enumerate(fin):
                aList = line.strip().split(" ")
                if len(aList) < 200:
                    #print lineNum
                    continue
                value = []
                for i in range(1, len(aList)):
                    value.append(float(aList[i]))
                self.vector[aList[0]] = value
    
    #def getVector(self):
        #return self.vector
        
    def __tmpNumpyArray(self, vectorKey):
        if vectorKey in self.vector:
            tmpList = self.vector[vectorKey]
            array = np.array(tmpList)
            return array
        else:
            print vectorKey + ": Invalid vectorKey in Class W2V tmpNumpyArray()!"
            exit()
    
    def sentenceVector(self, sentence):
        aList = sentence.strip().split(" ")
        if not aList:
            print "sentence split error in Class W2V sentenceVector()!"
            exit()

        arr1 = self.__tmpNumpyArray(aList[0])
        
        for i in range(1, len(aList) - 1):
            arr2 = self.__tmpNumpyArray(aList[i])
            arr1 = arr1 + arr2
        return (arr1/len(aList)).tolist()    
        #print arr1/len(aList)

