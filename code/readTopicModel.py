#-*- coding:utf-8 -*-
# AUTHOR:   yaolili
# FILE:     readTopicModel.py
# ROLE:     read topicModelFile and you can get the specific qid's or cid's topic model distributed probability
# CREATED:  2015-12-12 15:53:44
# MODIFIED: 2015-12-12 15:53:47


#the format of tfidfFile is something like this:
#topicModelId + \t + fileName + specific dimensions float numbers
#eg: 1 + \t + file:/home/yaolili/QAClassification/preProcessResult/Q2582_C15 + 200 dimensions float numbers


class TopicModel:
    def __init__(self, topicModelFile, dimension):
        self.probability = {}
        with open(topicModelFile, "r")as fin:
            for lineNum, line in enumerate(fin):
                aList = line.strip().split("\t")
                if not aList:
                    print "Line split error in Class TopicModel __init__()!"
                    exit()
                if len(aList) != (int(dimension) + 2):
                    print len(aList)
                    print str(lineNum) + ": " + line + " \nLine error in Class TopicModel __init__()!"
                    exit()

                value = []
                for i in range(2, len(aList)):
                    value.append(float(aList[i]))                   

                fileName = aList[1].strip().split("/")
                file = fileName[len(fileName) - 1]
                self.probability[file] = value 
    
    
    def getProbability(self, file):
        if file in self.probability:
            return self.probability[file]
        else:
            print "Invalid file in Class TopicModel getProbability()!"
            exit()
            
            