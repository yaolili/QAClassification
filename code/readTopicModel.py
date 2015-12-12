#-*- coding:utf-8 -*-
# AUTHOR:   yaolili
# FILE:     readTopicModel.py
# ROLE:     TODO (some explanation)
# CREATED:  2015-12-12 15:53:44
# MODIFIED: 2015-12-12 15:53:47

class TopicModel:
    def __init__(self, inputFile, dimension):
        self.probability = {}
        with open(inputFile, "r")as fin:
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