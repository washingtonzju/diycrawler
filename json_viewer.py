# -*- coding: utf-8 -*-
#!/bin/python
import sys
import codecs
import json

file = open(sys.argv[1], "r")
categorys = json.load(file)
file.close()

cnt = 0
for key, val in categorys.items():
    print key, ": ", len(val)
    cnt = cnt + len(val)

print cnt
