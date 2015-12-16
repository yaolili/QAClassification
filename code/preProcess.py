#-*- coding:utf-8 -*-
# AUTHOR:   yaolili
# FILE:     preProcess.py
# ROLE:     using nltk to preProcess train, dev and test file
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
    noStopwords = [w.lower() for w in tokens if not w.lower() in stopwords.words('english')]
    lmtzr = []
    for w in noStopwords:
        lmtzr.append(WordNetLemmatizer().lemmatize(w))
    #print lmtzr

    stem = []
    for w in lmtzr:
        stem.append(PorterStemmer().stem(w))
    #print stem
    
    return stem
    
    

def comment(question, qid, outputPath, hasUrl, prefix):
    if not question:
        print "Empty question in comment()!"
        exit()
    if isfile(outputPath):
        print "Invalid output file path! Directory expected!"
        exit()
    
    cid = []
    cuserid = []
    
    result1 = open(hasUrl, "w+")
    result2 = open(prefix, "w+")
    
    commentSet = [a for a in question.find_all('comment')]
    for each in commentSet:
        cid.append(each['cid'])
        cuserid.append(each['cuserid'])
        
        csubject = str(each.csubject.get_text())
        cbody = str(each.cbody.get_text())
        if "RE" not in csubject:
            cbody = csubject + " " + cbody
        cbody = nltkProcess(cbody)
        
        #write prefix file
        result2.write(cid + "\n")
        #write hasUrl file
        urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', cbody)
        if len(urls):  
            result1.write(each['cid'] + "\t" + "1" + "\n")
        else:
            result1.write(each['cid'] + "\t" + "0" + "\n")
        
        #one question has a file
        output = outputPath + qid
        result = open(join(output, each['cid']), "w+")
        
        #all file in one directory
        #result = open(join(outputPath, each['cid']), "w+")
        for word in cbody:
            result.write(word + " ")
        result.close()

    return cid, cuserid
         

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
    return qid, qcategory, quserid, qtype
        

def main(inputFile, outputPath, qcInfo, hasUrl, prefix): 

    result = open(qcInfo, "w+")
    with open(inputFile, "r") as fileContent:
        content = BS(fileContent.read(), "lxml")
        categorySet = {}
        questionSet = [a for a in content.find_all('question')]
        for each in questionSet:
            qid, qcategory, quserid, qtype = question(each, outputPath)
            if qcategory not in categorySet:
                categorySet[qcategory] = 1
            else:
                categorySet[qcategory] += 1
                
            cid, cuserid = comment(each, qid, outputPath, hasUrl, prefix)
            
            #write qcInfo file
            result.write(qid + "\t" + qcategory + "\t" + quserid + "\t" + qtype + "\n")
            if not cid:
                print "cid empty!"
                exit()
            for i in range(len(cid)):
                result.write(cid[i] + "\t" + cuserid[i] + "\n")
    result.close()
            

if __name__ == '__main__':
    if len(sys.argv) < 6:
        print "input train, dev or test file!"
        print "output file path!"
        print "output qcInfo file!"
        print "output hasUrl file!"
        print "output prefix file!"
        exit()
        
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])

 
