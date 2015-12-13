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
    
    def __init__(self, inputFile, dimension):
        self.vector = {}
        self.dimension = int(dimension)
        with open(inputFile) as fin:
            for lineNum, line in enumerate(fin):
                aList = line.strip().split(" ")
                if len(aList) < self.dimension:
                    #print lineNum
                    continue
                value = []
                for i in range(1, len(aList)):
                    value.append(float(aList[i]))
                self.vector[aList[0]] = value
                #print "len(value): " + str(len(value))
    
        
    def __tmpNumpyArray(self, vectorKey):
        if vectorKey in self.vector:
            tmpList = self.vector[vectorKey]
            array = np.array(tmpList)
            return array
        else:
            #log = open("emptyVectorKey.txt", "a+")
            #log.write(vectorKey + "\n")
            #Whole sentence may be empty if you return an empty array for a word
            #Thus it's invalid for division for cosine similarity
            #array = np.zeros(self.dimension)
            array = np.ones(self.dimension)
            array = array / 1000000000000
            return array
    
    def sentenceVector(self, sentence):
        aList = sentence.strip().split(" ")
        if not aList:
            print "sentence split error in Class W2V sentenceVector()!"
            exit()

        arr1 = self.__tmpNumpyArray(aList[0])
        #log = open("array.txt", "a+")
        #log.write(str(arr1.tolist()) + "\n")
        for i in range(1, len(aList)):
            arr2 = self.__tmpNumpyArray(aList[i])
            #log.write(str(arr2.tolist()) + "\n")
            arr1 = arr1 + arr2
        return (arr1/len(aList)).tolist()    
        #print arr1/len(aList)

