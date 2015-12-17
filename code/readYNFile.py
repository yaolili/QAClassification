#-*- coding:utf-8 -*-
# AUTHOR:   yaolili
# FILE:     readYNFile.py
# ROLE:     TODO (some explanation)
# CREATED:  2015-12-16 19:17:31
# MODIFIED: 2015-12-17 10:15:16

class YNFeature:
    def __init__(self, ynFile):
        self.cidDict = {}
        self.cidList = []
        #use for checking existing in cidList
        self.cidMap = {}
        with open(ynFile, "r")as fin:
            for lineNum, line in enumerate(fin):
                aList = line.strip().split("\t")
                cid = aList[0]
                vector = aList[1:]
                self.cidDict[cid] = vector
                if cid not in self.cidMap:
                    self.cidMap[cid] = 0
                    self.cidList.append(cid)
    
        
    def getCidList(self):
        return self.cidList
                
                
                
