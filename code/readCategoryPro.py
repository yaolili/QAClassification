#-*- coding:utf-8 -*-
# AUTHOR:   yaolili
# FILE:     readCategoryPro.py
# ROLE:     TODO (some explanation)
# CREATED:  2015-12-15 22:52:18
# MODIFIED: 2015-12-15 22:52:19

import sys
import os

class CategoryPro:
    def __init__(self, categoryProFile):
        self.result = {}
        with open(categoryProFile, "r")as fin:
            for line in fin:
                aList = line.strip().split("\t")
                self.result[aList[0]] = aList[1:]
    
    def getCategoryPro(self, category):
        if category not in self.result:
            print "Invalid category in Class CategoryPro __init__()!"
            exit()
        return self.result[category]