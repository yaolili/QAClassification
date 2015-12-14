#-*- coding:utf-8 -*-
# AUTHOR:   yaolili
# FILE:     getUrlTitle.py
# ROLE:     TODO (some explanation)
# CREATED:  2015-12-14 12:01:40
# MODIFIED: 2015-12-14 12:01:42

import urllib2
from bs4 import BeautifulSoup as BS

class UrlTitle:
    def __init__(self, url):    
        req = urllib2.Request(url)
        try:
            raw = urllib2.urlopen(req)
            self.content = BS(raw, "lxml")           
        except URLError as e:
            print e.reason 
            exit()
    
    def getTitle(self):
        return self.content.title.string