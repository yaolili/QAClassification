#-*- coding:utf-8 -*-
# AUTHOR:   yaolili
# FILE:     specialInfo.py
# ROLE:     TODO (some explanation)
# CREATED:  2015-12-13 16:56:37
# MODIFIED: 2015-12-13 16:56:41

class Info:

    def __init__(self, qcInfo):
        self.labelMapInt = {}
        self.cidMapQid = {}
        self.cidMapCuserid = {}
        self.qidMapQuserid = {}
        self.categroyAnsPro = {}
        with open(qcInfo, "r")as fin:
            for line in fin:
                aList = line.strip().split("\t")
                #question line
                if len(aList) != 4:
                    qid = aList[0]
                    qcategory = aList[1]
                    quserid = aList[2]
                    self.qidMapQuserid[qid] = quserid     
                #comment line
                else:
                    cid = aList[0]
                    cuserid = aList[1]
                    cgold = aList[2]
                    self.cidMapCuserid[cid] = qid
                    self.cidMapCuserid[cid] = cuserid
                    self.labelMapInt[cid] = labelToInt(cgold)
                    
                    key = qcategory + "_" + cgold
                    if key not in categroyAnsPro:
                        self.categroyAnsPro[key] = 0
                    else:
                        self.categroyAnsPro[key] += 1
                        

    def labelMapInt(self):
        return self.labelMapInt
        
    def cidMapQid(self):
        return self.cidMapQid
    
    def cidMapCuserid(self):
        return self.cidMapCuserid
        
    def qidMapQuserid(self):
        return self.qidMapQuserid
        
    def categroyAnsPro(self):
        return self.categroyAnsPro
        
    def labelToInt(self, label):
        if(label == "Good"):
            value = 6
        elif(label == "Bad"):
            value = 5
        elif(label == "Potential"):
            value = 4
        elif(label == "Dialogue"):
            value = 3
        elif(label == "non-English"):
            value = 2
        elif(label == "Other"):
            value = 1
        else:
            value = 0
        return value

        