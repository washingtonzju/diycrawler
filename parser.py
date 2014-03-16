# -*- coding: utf-8 -*-
#!/bin/python
import sys
import json
import urllib2
import codecs
from bs4 import BeautifulSoup
import re

class NEBBSParser:
    """
    page parser that extracting title and contents
    """
    def __init__(self):
        pass
        
    def parsing(self, url):
        content = u""
        page = urllib2.urlopen(url)
        soup = BeautifulSoup(unicode(page.read().decode("gbk")))

        title_soup = soup.find_all("h2", class_="tie-con-hd-title js-tietitle")[0]
        title = title_soup.contents[0]
        print title
        content = content + title + u"\n"
        
        content_soup = soup.find_all("div", class_="tie-content")
        para = unicode(content_soup[0])
        para = re.sub(u"<[^>]+>", u"", para, 10000)
        content = content + para
        print para.encode("utf-8")
        return content

class DXParser:
    """
    page parser that extracting title and contents
    """
    def __init__(self):
        pass
        
    def parsing(self, url):
        content = u""
        page = urllib2.urlopen(url)
        soup = BeautifulSoup(unicode(page.read().decode("utf-8")))

        title_soup = soup.find_all("h1", class_="title")[0]
        title = title_soup.contents[0]
        print title
        content = content + title + u"\n"
        
        content_soup = soup.find_all("div", id="content")
        para = unicode(content_soup[0])
        para = re.sub(u"<[^>]+>", u"", para, 10000)
        content = content + para
        print para.encode("utf-8")
        return content

class NEmParser:
    """
    page parser that extracting title and contents
    """
    def __init__(self):
        pass
        
    def parsing(self, url):
        content = u""
        page = urllib2.urlopen(url)
        soup = BeautifulSoup(unicode(page.read().decode("gbk")))
        title_soup = soup.find_all("h1", id="h1title")[0]
        title = unicode(title_soup.contents[0])
        content = content + title + u"\n"
        
        paras = soup.find_all("p", style="TEXT-INDENT: 2em")
        for para in paras:
            para_con = unicode(para)
            para_con = re.sub(u"<[^>]+>", u"", para_con, 10000)
            content = content + para_con + u"\n"
        print content
        return content

class Apple4Parser:
    """
    page parser that extracting title and contents
    TODO 
    """
    def __init__(self):
        pass
        
    def parsing(self, url):
        contents = u""
        return content
    
if __name__ == "__main__":
    # a map from url pattern to parser
    parser_picker = {}
    
    if len(sys.argv) < 2:
        print "Usage parser.py config_file.json, list_file.json"
    """
    parser = NEBBSParser()
    parser.parsing("http://bbs.money.163.com/bbs/licai/374989242.html")

    parser2 = DXParser()
    parser2.parsing("http://infect.dxy.cn/article/69521")
    """
    parser3 = NEmParser()
    parser3.parsing("http://money.163.com/09/0610/09/5BEHK3Q3002524TU.html")
    
    
