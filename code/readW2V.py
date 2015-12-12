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
                    print lineNum
                    continue
                value = []
                for i in range(1, len(aList)):
                    value.append(int(aList[i]))
                self.vector[aList[0]] = value
    
    #def getVector(self):
        #return self.vector
    
    def sentenceVector(self, sentence):
        aList = sentence.strip().split(" ")
        if not aList:
            print "sentence split error in Class W2V sentenceVector()!"
            exit()
        for word in aList:
            if word not in self.vector:
                print word
            
        

