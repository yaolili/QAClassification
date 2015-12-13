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
    #return lmtzr
    
    stem = []
    for w in lmtzr:
        stem.append(PorterStemmer().stem(w))
    #print stem
    return stem 
    
    

def comment(question, qid, outputPath):
    if not question:
        print "Empty question in comment()!"
        exit()
        
    commentSet = [a for a in question.find_all('comment')]
    for each in commentSet:
        cid = each['cid']
        cuserid = each['cuserid']
        csubject = str(each.csubject.get_text())
        cbody = str(each.cbody.get_text())
        if "RE" not in csubject:
            cbody = csubject + " " + cbody
        cbody = nltkProcess(cbody)
        #print cbody
        # result1 = open(outputPath, "a+")
        # for word in cbody:
            # result1.write(word + " ")
        # result1.write("\n")
        # result1.close()
        result2 = open("idOrderDev.txt", "a+")
        result2.write(cid + "\t" + qid + "\n")
        result2.close()
    #return remain to do    
         

def question(question, outputPath):   
    if not question:
        print "Empty question in question()!"
        exit()

    qid = question['qid']
    quserid = question['quserid']
    qcategory = question['qcategory']
        
    #deal with qsubject & qbody
    qsubject = str(question.qsubject.get_text()) 
    qbody = str(question.qbody.get_text())
    if qsubject not in qbody:
        qbody = qsubject + " " + qbody
    
    qbody = nltkProcess(qbody)
    result2 = open("idOrderDev.txt", "a+")
    result2.write(qid + "\t" + qid + "\n")
    result2.close()
    # result1 = open(outputPath, "a+")   
    # for word in qbody:
        # result1.write(word + " ")
    # result1.write("\n")
    # result1.close()
    print "qid: " + qid + "done!"
    #remain to do
    return qid, qcategory
        

def main(inputFile, outputPath):   
    with open(inputFile, "r") as fileContent:
        content = BS(fileContent.read(), "lxml")
        categorySet = {}
        questionSet = [a for a in content.find_all('question')]
        for each in questionSet:
            qid, qcategory = question(each, outputPath)
            comment(each, qid, outputPath)
        

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print "input train or test file!"
        print "output file!"
        exit()
        
    main(sys.argv[1], sys.argv[2])

 
