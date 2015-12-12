#-*- coding:utf-8 -*-
# AUTHOR:   yaolili
# FILE:     runW2V.py
# ROLE:     TODO (some explanation)
# CREATED:  2015-12-12 12:55:07
# MODIFIED: 2015-12-12 12:55:18

import os
import sys
from os import listdir
from os.path import isfile, join

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print "sys.argv[1]: input file path!"
        print "sys.argv[2]: output file path!"
        exit()
        
    files = [f for f in listdir(sys.argv[1]) if isfile(join(sys.argv[1], f))]
    for file in files:
        readPath = sys.argv[1] + file
        writePath = sys.argv[2] + file
        #print readPath
        #print writePath
        os.system("./word2vec -train " + readPath + " -output " + writePath " -cbow 0 -size 200 -window 5 -negative 0 -hs 1 -sample 1e-3 -threads 12 -binary 0")

