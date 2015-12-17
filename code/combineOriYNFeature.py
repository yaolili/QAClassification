#-*- coding:utf-8 -*-
# AUTHOR:   yaolili
# FILE:     combineOriYNFeature.py
# ROLE:     combine taskA feature & taskB feature into one file 
# CREATED:  2015-12-16 19:29:47
# MODIFIED: 2015-12-17 10:10:55

import os
import sys
from readYNFile import YNFeature

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print "sys.argv[1]: input original feature file"
        print "sys.argv[2]: input yn feature file"
        print "sys.argv[3]: output all feature file"
        exit()
    
    result = open(sys.argv[3], "w+")
    ynInstance = YNFeature(sys.argv[2])
    cidList = ynInstance.getCidList()
    
    
    originalMap = {}
    with open(sys.argv[1], "r")as fin:
        for line in fin:
            aList = line.strip().split("\t")
            originalMap[aList[0]] = aList[1:]

            
    for i in range(len(cidList)):
        cid = cidList[i]
        originalFeature = originalMap[cid]
        ynFeature = ynInstance.getYNFeature(cid)

        #jianmin need
        # result.write(cid)
        # result1 = open("testYNCid.txt", "a+")
        # result1.write(cid + "\n")
        # for j in range(len(originalFeature)):
            # result.write(originalFeature[j] + "\t")
        # for j in range(len(ynFeature)):
            # result.write(ynFeature[j] + "\t")
        # result.write("\n")
        
        #what I need
        result.write(cid)
        for j in range(len(originalFeature)):
            result.write("\t" + originalFeature[j])
        for j in range(len(ynFeature)):
            result.write("\t" + ynFeature[j])
        result.write("\n")
        

