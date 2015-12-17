#-*- coding:utf-8 -*-
# AUTHOR:   yaolili
# FILE:     yao.py
# ROLE:     TODO (some explanation)
# CREATED:  2015-12-16 21:47:09
# MODIFIED: 2015-12-16 21:47:11

import os
import sys
from baseQYN import BaseQYN

def qgoldYNToInt(qgold_yn):
    if qgold_yn == "Yes":
        return 1
    elif qgold_yn == "No":
        return 2
    elif qgold_yn == "Unsure":
        return 3
    else:
        return 0

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print "sys.argv[1]: input qidQgold_yn_train.txt"
        print "sys.argv[2]: input baseQAllFeature_train.txt"
        print "sys.argv[3]: output qgold_yn + allFeature.txt"
        exit()
    
    #instance = BaseQYN("devYNAllFeature.txt")
    instance = BaseQYN("testYNAllFeature.txt")
    
    qidDict = {}
    qidList = []
    result = open(sys.argv[3], "w+")
    with open(sys.argv[1], "r")as fin:
        for line in fin:
            qid, qgold_yn = line.strip().split("\t")
            qidList.append(qid)
            label = qgoldYNToInt(qgold_yn)
            if not label:
                print "Invalid qgold_yn!"
                exit()
            qidDict[qid] = label
            
            
    with open(sys.argv[2], "r")as fin:
        for line in fin:
            aList = line.strip().split("\t")
            qid = aList[0]
            feature = aList[1:]
            result.write(str(qidDict[qid]))
            for i in range(len(feature)):
                result.write("\t" + feature[i])
            result.write("\n")
            
    
    