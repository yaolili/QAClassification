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
    noStopwords = [w for w in tokens if not w.lower() in stopwords.words('english')]
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
    
    

def comment(question, outputPath):
    if not question:
        print "Empty question in comment()!"
        exit()
    if isfile(outputPath):
        print "Invalid output file path! Directory expected!"
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
        result = open(join(outputPath, cid), "w+")
        for word in cbody:
            result.write(word + " ")
        result.close()
    #return remain to do    
         

def question(question, outputPath):   
    if not question:
        print "Empty question in question()!"
        exit()
    if isfile(outputPath):
        print "Invalid output file path! Directory expected!"
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
    result = open(join(outputPath, qid), "w+")       
    for word in qbody:
        result.write(word + " ")
    result.close()
    print "qid: " + qid + "done!"
    #remain to do
    return qcategory
        

def main(inputFile, outputPath):   
    with open(inputFile, "r") as fileContent:
        content = BS(fileContent.read(), "lxml")
        categorySet = {}
        questionSet = [a for a in content.find_all('question')]
        for each in questionSet:
            category = question(each, outputPath)
            if category not in categorySet:
                categorySet[category] = 1
            else:
                categorySet[category] += 1
            comment(each, outputPath)
        #print categorySet
        result = open("categoryInfo", "w+")
        for category in categorySet:
            result.write(category + "\t" + str(categorySet[category]) + "\n")
        

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print "input train or test file!"
        print "output file path!"
        exit()
        
    main(sys.argv[1], sys.argv[2])

 
