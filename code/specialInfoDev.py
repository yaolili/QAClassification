#-*- coding:utf-8 -*-
# AUTHOR:   yaolili
# FILE:     specialInfo.py
# ROLE:     used for dev & test set
# CREATED:  2015-12-13 16:56:37
# MODIFIED: 2015-12-13 16:56:41

class Info:

    def __init__(self, qcInfo):
        #self.labelMapInt = {}
        self.cidMapQid = {}
        self.cidMapCuserid = {}
        self.cidMapCgold = {}
        self.qidMapQuserid = {}
        self.qidMapCategory = {}
        #self.categoryAnsPro = {}
        self.userId = {}
        with open(qcInfo, "r")as fin:
            for line in fin:
                aList = line.strip().split("\t")
                #in train, question line len == 5
                #in dev or test set, question line len == 4  
                if len(aList) == 4:
                    qid = aList[0]
                    qcategory = aList[1]
                    quserid = aList[2]
                    qtype = aList[3]
                    self.qidMapQuserid[qid] = quserid  
                    self.qidMapCategory[qid] = qcategory
                    
                    if quserid not in self.userId:
                        self.userId[quserid] = 1
                    else:
                        self.userId[quserid] += 1
                #in train or dev set, comment line len == 4
                #in test set, comment line len == 3
                else:
                    cid = aList[0]
                    cuserid = aList[1]

                    self.cidMapQid[cid] = qid
                    self.cidMapCuserid[cid] = cuserid
                    
                    if cuserid not in self.userId:
                        self.userId[cuserid] = 1
                    else:
                        self.userId[cuserid] += 1
                    
                   
        
    
    def userIdPro(self, userId):
        if userId not in self.userId:
            print "Invalid userId in Class Info userIdPro()!"
            exit()
        allCount = 0
        for id in self.userId:
            allCount += self.userId[id]
        count = self.userId[userId]
        return float(count)/allCount
   

    def cidToCuserid(self, cid):
        if cid not in self.cidMapCuserid:
            print "Invalid cid in Class Info cidToCuserid()!"
            exit()
        return self.cidMapCuserid[cid]
    
    def cidToCgold(self, cid):
        if cid not in self.cidMapCgold:
            print "Invalid cid in Class Info cidMapCgold()!"
            exit()
        return self.cidMapCgold[cid]
        
    
    def qidToCategory(self, qid):
        if qid not in self.qidMapCategory:
            print "Invalid qid in Class Info qidMapCategory()!"
            exit()
        return self.qidMapCategory[qid]
    
    def cidToQuserid(self, cid):
        if cid not in self.cidMapQid:
            print "Invalid cid in Class Info cidToQuserid()!"
            print self.cidMapQid
            exit()
        return self.qidMapQuserid[self.cidMapQid[cid]]
        
    
    def cidToQid(self, cid):
        if cid not in self.cidMapQid:
            print "Invalid cid in Class Info cidMapQid()!"
            exit()
        return self.cidMapQid[cid]
    
    def cidToCuserid(self, cid):
        if cid not in self.cidMapCuserid:
            print "Invalid cid in Class Info cidMapCuserid()!"
            exit()
        return self.cidMapCuserid[cid]
        
    def qidToQuserid(self, qid):
        if qid not in self.qidMapQuserid:
            print "Invalid qid in Class Info qidMapQuserid()!"
            exit()
        return self.qidMapQuserid[qid]
        

               
        
    def __labelToInt(self, label):
        if(label == "Good"):
            value = 6
        elif(label == "Bad"):
            value = 5
        elif(label == "Potential"):
            value = 4
        elif(label == "Dialogue"):
            value = 3
        elif(label == "Not English"):
            value = 2
        elif(label == "Other"):
            value = 1
        else:
            value = 0
        return value

        