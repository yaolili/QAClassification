#-*- coding:utf-8 -*-
# AUTHOR:   yaolili
# FILE:     dealResult.py
# ROLE:     TODO (some explanation)
# CREATED:  2015-12-14 19:58:53
# MODIFIED: 2015-12-14 19:58:55

import os
import sys
import linecache

def labelToString(label):
    if label == "6":
        string = "Good"
    elif label == "5":
        string = "Bad"
    elif label == "4":
        string = "Potential"
    elif label == "3":
        string = "Dialogue"
    elif label == "2":
        string = "Not English"
    else:
        string = "Other"
    return string
    

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print "sys.argv[1]: prefix order file"
        print "sys.argv[2]: label order file"
        print "sys.argv[3]: output file"
        exit()
        
    result = open(sys.argv[3], "w+")
    with open(sys.argv[1], "r")as fin:
        for lineNum, line in enumerate(fin):
            label = linecache.getline(sys.argv[2], lineNum + 1)
            line = line.strip().split("\n")[0]
            label = label.strip().split("\n")[0]
            # print line
            # print label
            # exit()
            result.write(line + "\t" + labelToString(label) + "\n")
            
    result.close()       