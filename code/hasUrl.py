#-*- coding:utf-8 -*-
# AUTHOR:   yaolili
# FILE:     hasUrl.py
# ROLE:     read hasUrlFile and you can determine whether the specific cid content has url or not
# CREATED:  2015-12-15 21:39:47
# MODIFIED: 2015-12-15 21:39:48


#the format of hasUrlFile is something like this:
#cid + \t + 1(or 0) + \n

class Url:
    def __init__(self, hasUrlFile):
        self.result = {}
        with open(hasUrlFile, "r")as fin:
            for line in fin:
                cid, hasUrl = line.strip().split("\t")
                self.result[cid] = hasUrl
    
    def isExistUrl(self, cid):
        if cid not in self.result:
            print "Invalid cid in Class Url isExistUrl()!"
            exit()
        return self.result[cid]
