#-*- coding:utf-8 -*-
# AUTHOR:   yaolili
# FILE:     preProcess.py
# ROLE:     TODO (some explanation)
# CREATED:  2015-12-11 21:04:11
# MODIFIED: 2015-12-11 21:04:20

import sys
import os
import re
import nltk
from os.path import isfile, join
from nltk import stem
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer

from bs4 import BeautifulSoup as BS

def nltkProcess(sentence):
    if not sentence:
        print "Empty sentence in nltkProcess()!"
        exit()
        
    tokenizer = RegexpTokenizer(r'\w+') 
    tokens = tokenizer.tokenize(sentence) 
    #print tokens
    #tokens = nltk.word_tokenize(sentence)
    noStopwords = [w.lower() for w in tokens if not w.lower() in stopwords.words('english')]
    lmtzr = []
    for w in noStopwords:
        lmtzr.append(WordNetLemmatizer().lemmatize(w))
    #print lmtzr
    return lmtzr
    
    # stem = []
    # for w in lmtzr:
        # stem.append(PorterStemmer().stem(w))
    # #print stem
    # return stem 
    
    

def comment(question, qid, outputPath):
    if not question:
        print "Empty question in comment()!"
        exit()
        
    commentSet = [a for a in question.find_all('comment')]
    cid = []
    cuserid = []
    for each in commentSet:
        cid.append(each['cid'])
        cuserid.append(each['cuserid'])

        csubject = str(each.csubject.get_text())
        cbody = str(each.cbody.get_text())
        
        if "RE" not in csubject:
            cbody = csubject + " " + cbody
        
        #has url or not 
        # urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', cbody)
        # result2 = open("hasUrlTest.txt", "a+")
        # if len(urls):  
            # result2.write(cid + "\t" + "1" + "\n")
        # else:
            # result2.write(cid + "\t" + "0" + "\n")
        
        cbody = nltkProcess(cbody) 

        # result3 = open("../order/prefixTest.txt", "a+")
        # result3.write(cid + "\n")
        # result1 = open(outputPath, "a+")
        # if cgold == "Potential":
            # result1.write(cid + ",\t" + cuserid + ",\t")
            # for word in cbody:
                # result1.write(word + " ")
            # result1.write("\n")
    #result1.close()
    return cid, cuserid  
         

def question(question, outputPath):   
    if not question:
        print "Empty question in question()!"
        exit()

    qid = question['qid']
    quserid = question['quserid']
    qcategory = question['qcategory']
    qtype = question['qtype']
    
    #deal with qsubject & qbody
    qsubject = str(question.qsubject.get_text()) 
    qbody = str(question.qbody.get_text())
    if qsubject not in qbody:
        qbody = qsubject + " " + qbody
    
    qbody = nltkProcess(qbody)

    # result1 = open(outputPath, "a+") 
    # result1.write(qid + ",\t" + quserid + ",\t" + qcategory + ",\t")
    # for word in qbody:
        # result1.write(word + " ")
    # result1.write("\n")
    # result1.close()
    print "qid: " + qid + "done!"
    #remain to do
    return qid, qcategory, quserid, qtype
        

def main(inputFile, outputPath):  
    result = open("qcInfo.test", "w+")
    with open(inputFile, "r") as fileContent:
        content = BS(fileContent.read(), "lxml")
        categorySet = {}
        questionSet = [a for a in content.find_all('question')]
        for each in questionSet:
            qid, qcategory, quserid, qtype = question(each, outputPath)
            cid, cuserid = comment(each, qid, outputPath)
            
            
            result.write(qid + "\t" + qcategory + "\t" + quserid + "\t" + qtype + "\n")
            if not cid:
                print "cid empty!"
                exit()
            for i in range(len(cid)):
                result.write(cid[i] + "\t" + cuserid[i] + "\n")
            
        

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print "input train or test file!"
        print "output file!"
        exit()
        
    main(sys.argv[1], sys.argv[2])

 
