#-*- coding:utf-8 -*-
# AUTHOR:   yaolili
# FILE:     hasUrl.py
# ROLE:     TODO (some explanation)
# CREATED:  2015-12-15 21:39:47
# MODIFIED: 2015-12-15 21:39:48

import sys
import os

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
