#-*- coding:utf-8 -*-
# AUTHOR:   yaolili
# FILE:     run.py
# ROLE:     TODO (some explanation)
# CREATED:  2015-12-12 11:27:16
# MODIFIED: 2015-12-12 11:33:14

import os
import sys
from os import listdir
from os.path import isfile, isdir, join
import numpy as np
from bagOfWords import BOW
from utility import Utility
from readW2V import W2V
from readTopicModel import TopicModel
from specialInfo import Info    
   
def writeResult(commentVectors, labelMapInt, outputFile):
    result = open(outputFile, "w+")
    for key in commentVectors:
        result.write(str(labelMapInt[key]) + " ")
        for i in range(len(commentVectors[key])):
            result.write(str(commentVectors[key][i]) + " ")
        result.write("\n")
    result.close()

def main(originalFile, w2vFile, w2vDimension, topicModelFile, topicModelDimension):

    bowDict = {}
    w2vDict = {}
    tmDict = {}
    resultDict = {}
    
    utility = Utility()
    w2v = W2V(w2vFile, w2vDimension)
    tm = TopicModel(topicModelFile, topicModelDimension)
    
    files = [f for f in listdir(originalFile) if isdir(join(originalFile, f))]
    #print files
    for directory in files:
        path = originalFile + directory
        fileList = [f for f in listdir(path) if isfile(join(path, f))]
        #print fileList
        #question file
        with open(path + "/" + directory, "r") as fin:
            s1 = fin.read()
            vec1 = w2v.sentenceVector(s1)
            t1 = tm.getProbability(directory)
        #comment file
        for each in fileList:
            if each == directory:
                continue
            completePath = path + "/" + each
            #print completePath           
            with open(completePath, "r") as fin:
                s2 = fin.read()
                #some questions & comments are empty after preProcessing
                if not s1 or not s2:
                    bowDict[each] = 0
                    w2vDict[each] = 0
                    tmDict[each] = 0
                    continue

                bow = BOW(s1, s2)   
                v1, v2 = bow.getVector()
                score = utility.cosine(v1, v2)
                bowDict[each] = score
                               
                vec2 = w2v.sentenceVector(s2)
                score = utility.cosine(vec1, vec2)               
                w2vDict[each] = score
                w2vResult = open("w2vResult.txt", "a+")
                w2vResult.write(each + "\t" + str(score) + "\n")
                
                t2 = tm.getProbability(each)
                score = utility.cosine(t1, t2)
                tmDict[each] = score
                '''
                print bowDict
                print w2vDict
                print tmDict
                '''
    print "bowDict, w2vDict, tmDict done!"        
    for key in bowDict:
        aList = []
        aList.append(bowDict[key])
        aList.append(w2vDict[key])
        aList.append(tmDict[key])
        resultDict[key] = aList
    print "resultDict done!"
    return resultDict   
    

if __name__ == '__main__':
    if len(sys.argv) < 8:
        print "sys.argv[1]: original file path!"
        print "sys.argv[2}: w2v file"
        print "sys.argv[3]: w2v dimension"
        print "sys.argv[4]: topic model file"
        print "sys.argv[5]: topic model dimension"
        print "sys.argv[6]: qcInfo"
        print "sys.argv[7]: format result file"
        exit()
    
    
    commentVectors = main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
    spInfo = Info(sys.argv[6])
    writeResult(commentVectors, spInfo.labelMapInt(), sys.argv[7])

    

    
    
    

