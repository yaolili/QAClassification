#-*- coding:utf-8 -*-
# AUTHOR:   yaolili
# FILE:     readTFIDF.py
# ROLE:     TODO (some explanation)
# CREATED:  2015-12-13 20:13:03
# MODIFIED: 2015-12-13 20:13:05

class Tfidf:
    def __init__(self, inputFile):
        self.result = {}
        with open(inputFile, "r")as fin:
            for line in fin:
                cid, score = line.strip().split("\t")
                self.result[cid] = score
    
    def getTfidfScore(self, cid):
        if cid not in self.result:
            print "Invalid cid in Class Tfidf getTfidfScore()!"
            exit()
        return self.result[cid]