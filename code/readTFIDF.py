#-*- coding:utf-8 -*-
# AUTHOR:   yaolili
# FILE:     readTFIDF.py
# ROLE:     read tfidfFile and you can get the specific cid's tfidf score
# CREATED:  2015-12-13 20:13:03
# MODIFIED: 2015-12-13 20:13:05

#the format of tfidfFile is something like this:
#cid + \t + score + \n

class Tfidf:
    def __init__(self, tfidfFile):
        self.result = {}
        with open(tfidfFile, "r")as fin:
            for line in fin:
                cid, score = line.strip().split("\t")
                self.result[cid] = score
    
    def getTfidfScore(self, cid):
        if cid not in self.result:
            print "Invalid cid in Class Tfidf getTfidfScore()!"
            exit()
        return self.result[cid]