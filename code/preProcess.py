#-*- coding:utf-8 -*-
# AUTHOR:   yaolili
# FILE:     preProcess.py
# ROLE:     TODO (some explanation)
# CREATED:  2015-12-11 21:04:11
# MODIFIED: 2015-12-11 21:04:20

import sys
import os
import nltk
from os.path import isfile, join
from nltk import stem
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer
from bs4 import BeautifulSoup as BS
from getUrlTitle import UrlTitle

def nltkProcess(sentence):
    if not sentence:
        print "Empty sentence in nltkProcess()!"
        exit()
        
    tokenizer = RegexpTokenizer(r'\w+') 
    tokens = tokenizer.tokenize(sentence) 
    #tokens = nltk.word_tokenize(sentence)
    noStopwords = [w.lower() for w in tokens if not w.lower() in stopwords.words('english')]
    lmtzr = []
    for w in noStopwords:
        lmtzr.append(WordNetLemmatizer().lemmatize(w))
    #print lmtzr
    
    '''
    stem = []
    for w in lmtzr:
        stem.append(PorterStemmer().stem(w))
    print stem
    #return stem
    '''
    return lmtzr
    
    

def comment(question, qid, outputPath):
    if not question:
        print "Empty question in comment()!"
        exit()
    if isfile(outputPath):
        print "Invalid output file path! Directory expected!"
        exit()
    
    cid = []
    cuserid = []
    cgold = []
    cgold_yn = []
    
    commentSet = [a for a in question.find_all('comment')]
    for each in commentSet:
        cid.append(each['cid'])
        cuserid.append(each['cuserid'])
        cgold.append(each['cgold'])
        cgold_yn.append(each['cgold_yn'])
        
        csubject = str(each.csubject.get_text())
        cbody = str(each.cbody.get_text())
        if "RE" not in csubject:
            cbody = csubject + " " + cbody
        cbody = nltkProcess(cbody)
        #one question has a file
        output = outputPath + qid
        result = open(join(output, each['cid']), "w+")
        #all file in one directory
        #result = open(join(outputPath, each['cid']), "w+")
        for word in cbody:
            result.write(word + " ")
        result.close()
    
    return cid, cuserid, cgold, cgold_yn
         

def question(question, outputPath):   
    if not question:
        print "Empty question in question()!"
        exit()
    if isfile(outputPath):
        print "Invalid output file path! Directory expected!"
        exit()
       
    qid = question['qid']   
    qcategory = question['qcategory']
    quserid = question['quserid']
    qtype = question['qtype']
    qgold_yn = question['qgold_yn']
    
    os.system("mkdir " + outputPath + qid)  
    output = join(outputPath, qid)
    
    #deal with qsubject & qbody
    qsubject = str(question.qsubject.get_text()) 
    qbody = str(question.qbody.get_text())
    if qsubject not in qbody:
        qbody = qsubject + " " + qbody    
    qbody = nltkProcess(qbody)
    
    #each question has a file
    result = open(join(output, qid), "w+")  
    #all file in one directory
    #result = open(join(outputPath, qid), "w+")
    for word in qbody:
        result.write(word + " ")
    result.close()
    print "qid: " + qid + "done!"
    return qid, qcategory, quserid, qtype, qgold_yn
        

def main(inputFile, outputPath):   
    with open(inputFile, "r") as fileContent:
        content = BS(fileContent.read(), "lxml")
        categorySet = {}
        questionSet = [a for a in content.find_all('question')]
        for each in questionSet:
            qid, qcategory, quserid, qtype, qgold_yn = question(each, outputPath)
            if qcategory not in categorySet:
                categorySet[qcategory] = 1
            else:
                categorySet[qcategory] += 1
                
            cid, cuserid, cgold, cgold_yn = comment(each, qid, outputPath)
            
            #question & comment info
            # result = open("qcInfo.dev", "a+")
            # result.write(qid + "\t" + qcategory + "\t" + quserid + "\t" + qtype + "\t" + qgold_yn + "\n")
            # if not cid:
                # print "cid empty!"
                # exit()
            # for i in range(len(cid)):
                # result.write(cid[i] + "\t" + cuserid[i] + "\t" + cgold[i] + "\n")
            # result.close()
            
        # print "qcInfo.dev done!"
        # result = open("categoryInfo.dev", "w+")
        # for category in categorySet:
            # result.write(category + "\t" + str(categorySet[category]) + "\n")
        # print "categoryInfo.dev done!"

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print "input train or test file!"
        print "output file path!"
        exit()
        
    main(sys.argv[1], sys.argv[2])

 
