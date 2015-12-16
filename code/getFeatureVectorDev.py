#-*- coding:utf-8 -*-
# AUTHOR:   yaolili
# FILE:     getFeatureVector.py
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
from specialInfoDev import Info    
from readTFIDF import Tfidf
from hasUrl import Url
from readCategoryPro import CategoryPro
 
def sort(keyOrderList):
    result = []
    order = []
    tmp = keyOrderList[0].strip().split("C")[0]
    for i in range(len(keyOrderList)):
        prefix, num = keyOrderList[i].strip().split("C")
        if prefix == tmp:
            order.append(int(num))
        else:
            order = sorted(order)
            for j in range(len(order)):
                string = tmp + "C" + str(order[j])
                result.append(string)
            order = []
            tmp = prefix
            order.append(int(num))
    order = sorted(order)   
    for j in range(len(order)):
        string = tmp + "C" + str(order[j])
        result.append(string)
    return result

 
def writeResult(commentVectors, outputFile, prefixFile, type):
    if not (type == "1" or type == "0"):
        print "Invalid type in writeResult()!"
        exit()
        
    labelDict = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}      #int label, count number
    goodDict = {}                                   #cid, label
    result = open(outputFile, "w+")
    file = open(prefixFile, "w+")
    aList = sorted(commentVectors.iterkeys())
    aList = sort(aList)
    for i in range(len(aList)):
        key = aList[i]
        '''
        #test usage!
        if labelMapInt[key] not in labelDict:
            labelDict[labelMapInt[key]] = 1
        else:
            labelDict[labelMapInt[key]] += 1
        ''' 
        #write prefixFile       
        file.write(key + "\n")       
        #write feature vector file      
        result.write("1.0" + " ")  
        for i in range(len(commentVectors[key])):
            result.write(str(commentVectors[key][i]) + " ")
        result.write("\n")
        
        #negative sampling in training
        #label 4 or 5 double write the ones whose w2v score plus topic model score > 1.0
        # if type == "0":
            # if float(commentVectors[key][1]) + float(commentVectors[key][2]) > 1.0 and (label == 4):
                # result.write(str(label) + " ")  
                # for i in range(len(commentVectors[key])):
                    # result.write(str(commentVectors[key][i]) + " ")
                # result.write("\n")
                
                # result.write(str(label) + " ")  
                # for i in range(len(commentVectors[key])):
                    # result.write(str(commentVectors[key][i]) + " ")
                # result.write("\n")
                

        '''
        #test usage!
        if float(commentVectors[key][1]) + float(commentVectors[key][2]) > 1.0:
            goodDict[key] = label
            labelDict[label] += 1
        '''
    result.close()
    '''
    #test usage!
    result = open("labelCount.txt", "w+")
    for key in labelDict:
        result.write(str(key) + "\t" + str(labelDict[key]) + "\n")
    result.close()
    
    #test usage
    result = open("goodCount.txt", "w+")
    for key in goodDict:
        result.write(str(key) + "\t" + str(goodDict[key]) + "\n")
    result.close()
    '''
    
def main(originalFile, w2vFile, w2vDimension, topicModelFile, topicModelDimension, infoInstance, tfidfInstance, hasUrlInstance, ansProInstance):

    bowDict = {}
    w2vDict = {}
    tmDict = {}
    
    cuserComQuser = {}  #cid, 0 or 1, compared with quserid
    ansProDict = {}     #cid, category_cgold probability
    tfidfDict = {}      #cid, tfidfScore
    urlDict = {}
    
    resultDict = {}
    
    utility = Utility()
    w2v = W2V(w2vFile, w2vDimension)
    tm = TopicModel(topicModelFile, topicModelDimension)
    
    files = [f for f in listdir(originalFile) if isdir(join(originalFile, f))]
    for directory in files:
        path = originalFile + directory
        fileList = [f for f in listdir(path) if isfile(join(path, f))]
        #question file
        with open(path + "/" + directory, "r") as fin:
            s1 = fin.read()
            vec1 = w2v.sentenceVector(s1)
            t1 = tm.getProbability(directory)
            
        #comment file
        for each in fileList:
            if each == directory:
                continue
            
            qid = directory
            cid = each
            cuserid = infoInstance.cidToCuserid(cid)           
            quserid = infoInstance.cidToQuserid(cid)
            qcategory = infoInstance.qidToCategory(qid) 
            
            
            if cuserid == quserid:
                cuserComQuser[cid] = 1.0
            else:
                cuserComQuser[cid] = 0.0           
      
            ansProDict[cid] = ansProInstance.getCategoryPro(qcategory)
            tfidfDict[cid] = tfidfInstance.getTfidfScore(cid)
            urlDict[cid] = hasUrlInstance.isExistUrl(cid) 
              
            completePath = path + "/" + each          
            with open(completePath, "r") as fin:
                s2 = fin.read()
                #some questions & comments are empty after preProcessing
                if not s1 or not s2:
                    bowDict[each] = 0.000000000001
                    w2vDict[each] = 0.000000000001
                    tmDict[each] = 0.000000000001
                    continue

                bow = BOW(s1, s2)   
                v1, v2 = bow.getVector()
                score = utility.cosine(v1, v2)
                bowDict[each] = score
                               
                vec2 = w2v.sentenceVector(s2)
                score = utility.cosine(vec1, vec2)               
                w2vDict[each] = score
                
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
        aList.append(cuserComQuser[key])
        for i in range(len(ansProDict[key])):    
            aList.append(ansProDict[key][i])
        aList.append(tfidfDict[key])
        aList.append(urlDict[key])
        resultDict[key] = aList
    print "resultDict done!"
    return resultDict   
    

if __name__ == '__main__':
    if len(sys.argv) < 13:
        print "sys.argv[1]: original file path!"
        print "sys.argv[2}: w2v file"
        print "sys.argv[3]: w2v dimension"
        print "sys.argv[4]: topic model file"
        print "sys.argv[5]: topic model dimension"
        print "sys.argv[6]: qcInfo"
        print "sys.argv[7]: format result file"
        print "sys.argv[8]: tfidf file"
        print "sys.argv[9]: prefix order file"
        print "sys.argv[10]: 0 for train,  1 for dev"
        print "sys.argv[11]: hasUrl file"
        print "sys.argv[12]: categoryAnsProTrain file"
        exit()
    
    spInfo = Info(sys.argv[6])
    ansProInstance = CategoryPro(sys.argv[12])
    tfidfInstance = Tfidf(sys.argv[8])
    hasUrlInstance = Url(sys.argv[11])
    commentVectors = main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], spInfo, tfidfInstance, hasUrlInstance, ansProInstance)
    writeResult(commentVectors, sys.argv[7], sys.argv[9], sys.argv[10])

    

    
    
    

