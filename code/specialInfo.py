#-*- coding:utf-8 -*-
# AUTHOR:   yaolili
# FILE:     specialInfo.py
# ROLE:     TODO (some explanation)
# CREATED:  2015-12-13 16:56:37
# MODIFIED: 2015-12-16 08:47:43

class trainInfo:

    def __init__(self, qcInfo):
        self.labelMapInt = {}
        self.cidMapQid = {}
        self.cidMapCuserid = {}
        self.cidMapCgold = {}
        self.qidMapQuserid = {}
        self.qidMapCategory = {}
        self.categoryAnsPro = {}
        self.userId = {}
        with open(qcInfo, "r")as fin:
            for line in fin:
                aList = line.strip().split("\t")
                #in train or dev set, question line len == 5
                #in test set, question line len == 4  
                #notice, in train or dev set, should be != rather than ==
                if len(aList) != 4:
                    qid = aList[0]
                    qcategory = aList[1]
                    quserid = aList[2]
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
                    cgold = aList[2]
                    self.cidMapQid[cid] = qid
                    self.cidMapCuserid[cid] = cuserid
                    self.cidMapCgold[cid] = cgold
                    
                    if self.__labelToInt(cgold) == 0:
                        print "Invalid cgold in Class Info __init__()!"
                        print cgold
                        exit()
                    self.labelMapInt[cid] = self.__labelToInt(cgold)
                    
                    if cuserid not in self.userId:
                        self.userId[cuserid] = 1
                    else:
                        self.userId[cuserid] += 1
                    
                    key = qcategory + "_" + cgold
                    if key not in self.categoryAnsPro:
                        self.categoryAnsPro[key] = 1
                    else:
                        self.categoryAnsPro[key] += 1
        
    
    def userIdPro(self, userId):
        if userId not in self.userId:
            print "Invalid userId in Class Info userIdPro()!"
            exit()
        allCount = 0
        for id in self.userId:
            allCount += self.userId[id]
        count = self.userId[userId]
        return float(count)/allCount
   
    
    #remain to do
    def labelToInt(self):
        #key is cid, value is an [int] 
        return self.labelMapInt

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
        
    def getCategoryAnsPro(self, categoryKey):
        aList = []
        label = ["Good", "Bad", "Potential", "Dialogue", "Not English", "Other"]
        for each in label:
            key = categoryKey + "_" + each
            aList.append(key)
        #here aList is : categoryKey_labelItem
        
        allCount = 0
        eachCount = []
        result = []
        for i in range(len(aList)):
            if aList[i] not in self.categoryAnsPro:
                #print aList[i] + ". Invalid categoryKey in Class Info categoryAnsPro()!"
                eachCount.append(0.0)
            else:
                eachCount.append(float(self.categoryAnsPro[aList[i]]))
                allCount += self.categoryAnsPro[aList[i]]   
        for i in range(len(eachCount)):
            result.append(eachCount[i]/allCount)
        return result

               
        
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

        
