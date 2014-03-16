# -*- coding: utf-8 -*-
#!/bin/python
import sys
import codecs
import json
import urllib2
#import html5lib
from bs4 import BeautifulSoup
import re

class NEBBSCrawler:
    def __init__(self, url, type):
        """
        initilize the data structure
        """
        self.params = {"type": type, "url": url}
                
    def parsing(self):
        """        
        open url, and extract the article list from them using feature str.
        the article list will be labeled as type.
        """
        articles = {}
        page = urllib2.urlopen(self.params["url"])
        soup = BeautifulSoup(unicode(page.read().decode("gbk")))
        #print soup.prettify()
        
        contents = soup.find_all("div", class_="colM")
        
        for content in contents:
            blocks = content.find_all("div", class_="content")
            for block in blocks:
                anchors = block.find_all("a")
                for anchor in anchors:
                    articles[anchor.contents[0]] = anchor.attrs["href"]
        
        return articles

class NEArticleCrawler:
    def __init__(self, url, type):
        """
        initilize the data structure
        """
        self.params = {"type": type, "url": url}
                
    def parsing(self):
        """        
        open url, and extract the article list from them using feature str.
        the article list will be labeled as type.
        """
        articles = {}
        page = urllib2.urlopen(self.params["url"])
        soup = BeautifulSoup(unicode(page.read().decode("gbk")))
        #print soup.prettify()
        
        contents = soup.find_all("div", class_="list_item clearfix")
        
        for content in contents:
            anchors = content.find_all("a", class_="")
            for anchor in anchors:
                print anchor
                articles[anchor.contents[0]] = anchor.attrs["href"]                
        return articles

class ZNLCrawler:
    def __init__(self, url, type):
        """
        initilize the data structure
        """
        self.params = {"type": type, "url": url}
                
    def parsing(self):
        articles = {}
        page = urllib2.urlopen(self.params["url"])
        soup = BeautifulSoup(unicode(page.read().decode("utf-8")))

        contents = soup.find_all("div", id="topnew")
        
        for content in contents:
            anchors = content.find_all("a", class_="")
            for anchor in anchors:
                print anchor
                articles[anchor.contents[0]] = self.params["url"] + anchor.attrs["href"]
        content2 = soup.find_all("div", id="tophot")

        for content in content2:
            anchors = content.find_all("a", class_="")
            for anchor in anchors:
                print anchor
                articles[anchor.contents[0]] = self.params["url"] + anchor.attrs["href"]
                print self.params["url"] + anchor.attrs["href"]
        return articles

class ZNLListCrawler:
    def __init__(self, url, type):
        """
        initilize the data structure
        """
        self.params = {"type": type, "url": url}
                
    def parsing(self):
        articles = {}
        page = urllib2.urlopen(self.params["url"])
        soup = BeautifulSoup(unicode(page.read().decode("utf-8")))

        contents = soup.find_all("ul", class_="newslist")
        
        for content in contents:
            anchors = content.find_all("a", class_="")
            for anchor in anchors:
                print anchor
                articles[anchor.contents[0]] = self.params["url"] + anchor.attrs["href"]        
        return articles
    
class NEListCrawler:
    def __init__(self, url, type):
        """
        initilize the data structure
        """
        self.params = {"type": type, "url": url}
                
    def parsing(self):
        articles = {}
        page = urllib2.urlopen(self.params["url"])
        soup = BeautifulSoup(unicode(page.read().decode("gbk")))

        contents = soup.find_all("div", class_="list_item clearfix")
        
        for content in contents:
            anchors = content.find_all("a", class_="")
            for anchor in anchors:
                print anchor
                articles[anchor.contents[0]] = anchor.attrs["href"]        
        return articles

class XCFCrawler:
    def __init__(self, url, type):
        """
        initilize the data structure
        """
        self.params = {"type": type, "url": url}
                
    def parsing(self):
        articles = {}
        page = urllib2.urlopen(self.params["url"])
        soup = BeautifulSoup(unicode(page.read().decode("utf-8")))

        contents = soup.find_all("div", class_="menu-list")
        
        for content in contents:
            anchors = content.find_all("a", class_="large-font")
            for anchor in anchors:
                print anchor
                articles[anchor.contents[0]] = "http://www.xiachufang.com/"+anchor.attrs["href"]
                print articles[anchor.contents[0]]
        return articles

class DXCrawler:
    def __init__(self, url, type):
        """
        initilize the data structure
        """
        self.params = {"type": type, "url": url}

    def parsing(self):
        articles = {}
        page = urllib2.urlopen(self.params["url"])
        soup = BeautifulSoup(unicode(page.read().decode("utf-8")))

        contents = soup.find_all("dl", class_="x_box12")
        
        for content in contents:
            anchors = content.find_all("a")
            for anchor in anchors:
                print anchor
                articles[anchor.contents[0]] = anchor.attrs["href"]
                print articles[anchor.contents[0]]
        return articles
    
class WumiCrawler:
    def __init__(self, url, type):
        """
        initilize the data structure
        """
        self.params = {"type": type, "url": url}
                
    def parsing(self):
        pass

class NEZCCrawler:
    def __init__(self, url, type):
        """
        initilize the data structure
        """
        self.params = {"type": type, "url": url}
                
    def parsing(self):
        articles = {}
        page = urllib2.urlopen(self.params["url"])
        soup = BeautifulSoup(unicode(page.read().decode("gbk")))

        contents = soup.find_all("div", class_="boxL")
        
        for content in contents:
            anchors = content.find_all("a")            
            for anchor in anchors:
                if len(anchor.contents) < 1: continue
                print anchor
                articles[anchor.contents[0]] = anchor.attrs["href"]
                print articles[anchor.contents[0]]
        print len(articles)
        return articles

class Apple4Crawler:
    def __init__(self, url, type):
        """
        initilize the data structure
        """
        self.params = {"type": type, "url": url}
                
    def parsing(self):
        articles = {}
        page = urllib2.urlopen(self.params["url"])
        soup = BeautifulSoup(unicode(page.read().decode("utf-8")))

        contents = soup.find_all("main", id="content")
        
        for content in contents:
            anchors = content.find_all("a", rel="bookmark")            
            for anchor in anchors:
                if len(anchor.contents) < 1: continue
                print anchor
                articles[anchor.contents[0]] = anchor.attrs["href"]
                print articles[anchor.contents[0]]
        print len(articles)
        return articles

class TTZNLCrawler:
    def __init__(self, url, type):
        """
        initilize the data structure
        """
        self.params = {"type": type, "url": url}
                
    def parsing(self):
        articles = {}
        page = urllib2.urlopen(self.params["url"])
        soup = BeautifulSoup(unicode(page.read().decode("gbk")))

        contents = soup.find_all("div", class_="picxn")
        
        for content in contents:
            anchors = content.find_all("a")            
            for anchor in anchors:
                if len(anchor.contents) < 1: continue
                print anchor
                articles[anchor.contents[0]] = "http://www.ttznl.cn/" + anchor.attrs["href"]
                print articles[anchor.contents[0]]
        print len(articles)
        return articles
    
if __name__ == "__main__":
    
    if len(sys.argv) < 2:
        print "Usage crawler.py crawler_source.json"
        
    """
    crawler = NEBBSCrawler("http://money.163.com/licai/", 2)
    crawler2 = NEArticleCrawler("http://money.163.com/special/ctgc/", 2)
    print crawler.parsing()
    crawler2.parsing()
    crawler3 = ZNLCrawler("http://www.znlba.com", 6)
    crawler3.parsing()
    crawler4 = ZNLListCrawler("http://www.znlba.com/v3", 6)
    crawler4.parsing()
    crawler5 = NEListCrawler("http://money.163.com/special/002534NV/auto_house.html", 4)
    crawler5.parsing()
    crawler6 = XCFCrawler("http://www.xiachufang.com/explore/menu/collect/", 4)
    crawler6.parsing()
    crawler7 = DXCrawler("http://infect.dxy.cn/tag/news", 4)
    crawler7.parsing()
    crawler8 = XinHuaCrawler("http://search.news.cn/mb/xinhuanet/search/?styleurl=http://www.xinhuanet.com/employment/static/style/zhichang.css&amp;nodetype=3&amp;nodeid=11629", 1)
    crawler8.parsing()
    crawler9 = Apple4Crawler("http://www.apple4.cn/category/happy-study/study-resouces/", 3)
    crawler9.parsing()
    """
    crawlers = []
    
    crawlers.append(NEBBSCrawler("http://money.163.com/licai/", 2))
    crawlers.append(NEArticleCrawler("http://money.163.com/special/ctgc/", 2))
    crawlers.append(NEArticleCrawler("http://money.163.com/special/ctgc_02/", 2))
    crawlers.append(NEArticleCrawler("http://money.163.com/special/ctgc_03/", 2))
    crawlers.append(NEArticleCrawler("http://money.163.com/special/ctgc_04/", 2))
    crawlers.append(ZNLCrawler("http://www.znlba.com", 6))
    crawlers.append(ZNLListCrawler("http://www.znlba.com/v1", 6))
    crawlers.append(ZNLListCrawler("http://www.znlba.com/v2", 6))
    crawlers.append(ZNLListCrawler("http://www.znlba.com/v3", 6))
    crawlers.append(ZNLListCrawler("http://www.znlba.com/v4", 6))
    crawlers.append(ZNLListCrawler("http://www.znlba.com/v5", 6))
    crawlers.append(ZNLListCrawler("http://www.znlba.com/v6", 6))
    crawlers.append(NEListCrawler("http://money.163.com/special/002534NV/auto_house.html", 4))
    crawlers.append(NEListCrawler("http://money.163.com/special/002534NV/auto_house_02.html", 4))
    crawlers.append(NEListCrawler("http://money.163.com/special/002534NU/house2010.html", 4))
    crawlers.append(NEListCrawler("http://money.163.com/special/002534NU/house2010_02.html", 4))
    crawlers.append(XCFCrawler("http://www.xiachufang.com/explore/menu/collect/", 4))
    crawlers.append(XCFCrawler("http://www.xiachufang.com/explore/menu/collect/?page=2", 4))
    crawlers.append(DXCrawler("http://infect.dxy.cn/tag/news", 4))
    crawlers.append(DXCrawler("http://infect.dxy.cn/tag/news/p-2", 4))    
    crawlers.append(NEZCCrawler("http://biz.163.com/special/00020UQ7/officelife.html", 1))
    crawlers.append(NEZCCrawler("http://biz.163.com/special/00020UQ7/officelife_02.html", 1))
    crawlers.append(NEZCCrawler("http://biz.163.com/special/00020UQ7/officelife_03.html", 1))
    crawlers.append(NEZCCrawler("http://biz.163.com/special/00020UQ7/officelife_04.html", 1))
    crawlers.append(NEZCCrawler("http://biz.163.com/special/00020UQ7/officelife_05.html", 1))
    crawlers.append(NEZCCrawler("http://biz.163.com/special/00020UQ7/officelife_06.html", 1))
    crawlers.append(NEZCCrawler("http://biz.163.com/special/00020UQ7/officelife_07.html", 1))
    crawlers.append(NEZCCrawler("http://biz.163.com/special/00020UQ7/officelife_08.html", 1))
    crawlers.append(NEZCCrawler("http://biz.163.com/special/00020UQ7/officelife_09.html", 1))
    crawlers.append(Apple4Crawler("http://www.apple4.cn/category/happy-study", 3))
    crawlers.append(Apple4Crawler("http://www.apple4.cn/category/happy-study/page/2/", 3))
    crawlers.append(Apple4Crawler("http://www.apple4.cn/category/happy-study/page/3/", 3))
    crawlers.append(Apple4Crawler("http://www.apple4.cn/category/happy-study/page/4/", 3))
    crawlers.append(Apple4Crawler("http://www.apple4.cn/category/happy-study/page/5/", 3))
    crawlers.append(Apple4Crawler("http://www.apple4.cn/category/happy-study/page/6/", 3))
    crawlers.append(Apple4Crawler("http://www.apple4.cn/category/happy-study/page/7/", 3))
    crawlers.append(Apple4Crawler("http://www.apple4.cn/category/happy-study/page/8/", 3))
    crawlers.append(Apple4Crawler("http://www.apple4.cn/category/happy-study/page/9/", 3))
    crawlers.append(Apple4Crawler("http://www.apple4.cn/category/happy-study/page/10/", 3))    
    crawlers.append(TTZNLCrawler("http://www.ttznl.cn/zhengnenliangxinwen/", 6))
    crawlers.append(TTZNLCrawler("http://www.ttznl.cn/zhengnenliangxinwen/list_1_2.html", 6))
    #crawlers[0].parsing()
    #crawlers[1].parsing()
    
    categorys = {}
    for crawler in crawlers:
        articles = crawler.parsing()
        key = crawler.params["type"]
        if key not in categorys.keys():
            categorys[key] = []
        for con, url in articles.items():
            categorys[key].append(url)

    file = codecs.open(sys.argv[1], "w", encoding="utf-8")
    file.write(json.dumps(categorys))
    file.close()
    
