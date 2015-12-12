#-*- coding:utf-8 -*-
# AUTHOR:   yaolili
# FILE:     run.py
# ROLE:     TODO (some explanation)
# CREATED:  2015-12-12 11:27:16
# MODIFIED: 2015-12-12 11:33:14

import os
import sys
import numpy as np
from bagOfWords import BOW
from utility import Utility

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print "sys.argv[1]: s1"
        print "sys.argv[2}: s2"
        exit()

    with open(sys.argv[1], "r") as fin:
        s1 = fin.read()
    with open(sys.argv[2], "r") as fin:
        s2 = fin.read()
        
    bow = BOW(s1, s2)
    utility = Utility()
    v1, v2 = bow.getVector()
    array = utility.numpyArray(v1, v2)
    score = utility.cosine(array)
    print score
    
    

