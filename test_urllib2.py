# -*- coding: utf-8 -*-
#!/bin/python
import sys
import codecs
import json
import urllib2
#import html5lib
from bs4 import BeautifulSoup
import re

page = urllib2.urlopen("https://www.facebook.com")
print unicode(page.read().decode("gbk"))
