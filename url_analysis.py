# -*- coding: utf-8 -*-
#!/bin/python
import sys
import json
import codecs
from bs4 import BeautifulSoup
import re

file = open(sys.argv[1], "r")
categorys = json.load(file)
file.close()

urls = []

for key, val in categorys.items():
    urls = urls + val

urls = sorted(urls)

for url in urls:
    print url

