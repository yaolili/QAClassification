#-*- coding:utf-8 -*-
# AUTHOR:   yaolili
# FILE:     baseQYN.py
# ROLE:     TODO (some explanation)
# CREATED:  2015-12-16 21:19:37
# MODIFIED: 2015-12-17 10:21:01

import copy

#cid, all feature

class BaseQYN:
    def __init__(self, ynAllFeatureFile):
        self.cidDict = {}
        self.qidDict = {}
        self.qidList = []
        tmp = ""
        tmpList = []
        num = 0
        with open(ynAllFeatureFile, "r") as fin:
        
            for line in fin:
                aList = line.strip().split("\t")
                cid = aList[0]
                featureList = aList[1:]
                qid = cid.strip().split("_")[0]
                if not tmp:
                    num += 1
                    tmp = qid
                    tmpList = copy.deepcopy(featureList)
                    self.qidList.append(qid)
                else:
                    if tmp != qid:
                        for i in range(len(tmpList)):
                            tmpList[i] = float(tmpList[i]) / num
                        self.qidDict[tmp] = tmpList
                        # print self.qidDict
                        # exit()
                        num = 1
                        tmp = qid
                        tmpList = copy.deepcopy(featureList)
                        self.qidList.append(qid)
                    else:
                        for i in range(len(tmpList)):
                            tmpList[i] = float(tmpList[i]) + float(featureList[i])
            
            #dont't forget the final qid
            for i in range(len(tmpList)):
                tmpList[i] = float(tmpList[i]) / num
            self.qidDict[tmp] = tmpList
            
            #here can be "prefixTrainYN.txt", "prefixDevYN.txt" for result1
            #and "baseQAllFeature_train.txt", "baseQAllFeature_dev.txt" are also ok with log
            result1 = open("prefixTestYN.txt", "w+")
            log = open("baseQAllFeature_test.txt", "w+")
            for i in range(len(self.qidList)):
                qid = self.qidList[i]
                result1.write(qid + "\n")
                log.write("1.0")
                for j in range(len(self.qidDict[qid])):
                    log.write("\t" + str(self.qidDict[qid][j]))
                log.write("\n")
            
            '''
            #test usage!
            log = open("log.txt", "w+")
            for i in range(len(self.qidList)):
                qid = self.qidList[i]
                log.write(qid + "\t" + str(self.qidDict[qid]) + "\n")     
            '''
            
    def getQidFeature(self, qid):
        if qid not in self.qidList:
            print "Invalid qid in Class BaseQYN getQidFeature()!"
            exit()
        return self.qidDict[qid]
        
               
                
