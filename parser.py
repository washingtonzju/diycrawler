# -*- coding: utf-8 -*-
#!/bin/python
import os
import sys
import json
import urllib2
import codecs
import hashlib
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

        title_soup = soup.find_all("h2", class_="tie-con-hd-title")[0]
        title = title_soup.contents[0]
        #print title
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
        #print title
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
        
        paras = soup.find_all("p")
        for para in paras:
            para_con = unicode(para)
            para_con = re.sub(u"<[^>]+>", u"", para_con, 10000)
            content = content + para_con + u"\n"
        print content.encode("utf-8")
        return content

class Apple4Parser:
    """
    page parser that extracting title and contents
    TODO 
    """
    def __init__(self):
        pass
        
    def parsing(self, url):
        content = u""
        page = urllib2.urlopen(url)
        soup = BeautifulSoup(unicode(page.read().decode("utf-8")))
        #print soup
        title_soup = soup.find_all("h1", class_="entry-title")[0]
        title = unicode(title_soup.contents[0])
        content = content + title + u"\n"
        paras = soup.find_all("div", class_="entry-content", itemprop="articleBody")
        for para in paras:
            para_con = unicode(para)
            para_con =  re.sub(r"<script.+\n.+\n</script>", u"", para_con, 100, re.MULTILINE)
            para_con = re.sub(u"<[^>]+>", u"", para_con, 10000)
            #print para_con.encode("utf-8")
            
            content = content + para_con + u"\n"

        print content.encode("utf-8")
        return content
        
class TTZNLParser:
    """
    page parser that extracting title and contents
    TODO 
    """
    def __init__(self):
        pass
        
    def parsing(self, url):
        content = u""
        page = urllib2.urlopen(url)
        soup = BeautifulSoup(unicode(page.read().decode("gbk")))
        #print soup
        title_soup = soup.find_all("div", class_="artz")[0].find_all("h2")[0]
        title = unicode(title_soup.contents[0])
        content = content + title + u"\n"
        paras = soup.find_all("div", class_="arpic")
        for para in paras:
            para_con = unicode(para)
            #para_con =  re.sub(r"<script.+\n.+\n</script>", u"", para_con, 100, re.MULTILINE)
            para_con = re.sub(u"<[^>]+>", u"", para_con, 10000)
            #print para_con.encode("utf-8")
            
            content = content + para_con + u"\n"

        print content.encode("utf-8")
        return content

class XCFParser:
    """
    page parser that extracting title and contents
    TODO 
    """
    def __init__(self):
        pass
        
    def parsing(self, url):
        content = u""
        page = urllib2.urlopen(url)
        soup = BeautifulSoup(unicode(page.read().decode("utf-8")))
        #print soup
        title_soup = soup.find_all("h1", class_="page-title align-center")[0]
        title = unicode(title_soup.contents[0])
        content = content + title + u"\n"
        paras = soup.find_all("div", class_="desc")
        for para in paras:
            para_con = unicode(para)
            #para_con =  re.sub(r"<script.+\n.+\n</script>", u"", para_con, 100, re.MULTILINE)
            para_con = re.sub(u"<[^>]+>", u"", para_con, 10000)
            #print para_con.encode("utf-8")
            
            content = content + para_con + u"\n"

        paras2 = soup.find_all("ul", class_="plain")
        for para in paras2:
            para_con = unicode(para)
            #para_con =  re.sub(r"<script.+\n.+\n</script>", u"", para_con, 100, re.MULTILINE)
            para_con = re.sub(u"<[^>]+>", u"", para_con, 10000)
            #print para_con.encode("utf-8")
            
            content = content + para_con + u"\n"
        print content.encode("utf-8")
        return content

class ZNLParser:
    """
    page parser that extracting title and contents
    TODO 
    """
    def __init__(self):
        pass
        
    def parsing(self, url):
        content = u""
        page = urllib2.urlopen(url)
        soup = BeautifulSoup(unicode(page.read().decode("utf-8")))
        #print soup
        title_soup = soup.find_all("div", class_="title")[0].find_all("h1")[0]
        title = unicode(title_soup.contents[0])
        content = content + title + u"\n"
        paras = soup.find_all("div", id="sdcms_content")
        for para in paras:
            para_con = unicode(para)
            #para_con =  re.sub(r"<script.+\n.+\n</script>", u"", para_con, 100, re.MULTILINE)
            para_con = re.sub(u"<[^>]+>", u"", para_con, 10000)
            #print para_con.encode("utf-8")
            
            content = content + para_con + u"\n"
        print content.encode("utf-8")
        return content
        
if __name__ == "__main__":

    if len(sys.argv) < 2:
        print "Usage parser.py categorys.json"
        
    # a map from url pattern to parser
    parser_picker = {
        r"http://bbs\.money\.163\.com/bbs/licai/.+": NEBBSParser(),
        r"http://infect\.dxy\.cn/article/.+": DXParser(),
        r"http://money\.163\.com/[0-9]+/[0-9]+/[0-9]+/.+": NEmParser(),
        r"http://www\.apple4\.cn/[0-9]+/[0-9]+/.+": Apple4Parser(),
        r"http://www\.ttznl\.cn/.+": TTZNLParser(),
        r"http://www\.xiachufang\.com//recipe_list/[0-9]+":XCFParser(),
        r"http://www\.znlba\.com/v[0-9]+/.+": ZNLParser()        
    }

    file = codecs.open(sys.argv[1], "r", encoding="utf-8")
    urls = json.load(file)
    file.close()

    #lst = [1]
    #print lst[2]
    exists = {}
    error_urls = []
    for key, val in urls.items():
        dir_name = str(key)
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)
        for url in val:
            parser = None
            for patt, ps in parser_picker.items():
                if re.match(patt, url)!=None:
                    parser = ps
                    break
            if parser == None: continue
            #print url, parser.__name__
            
            try:
                content = parser.parsing(url)
                h = hashlib.md5()
                h.update(url)
                file_name = h.hexdigest()
                if file_name in exists.keys():
                    continue
                exists[file_name] = True
                out_file = codecs.open(dir_name+"/"+file_name, "w", encoding="gb18030")
                out_file.write(content)
                out_file.close()
                
            except urllib2.HTTPError, err:
                error_urls.append(url)
                continue
            except urllib2.URLError, err:
                error_urls.append(url)
                continue
            except UnicodeEncodeError, err:
                error_urls.append(url)
                continue
            except IndexError, err:
                error_urls.append(url)
                continue
        
    for e_url in error_urls:
        print e_url
        
