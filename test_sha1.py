# -*- coding: utf-8 -*-
#!/bin/python
import hashlib

h = hashlib.md5()
#h.update('http://www.apple4.cn/2009/11/how-to-take-free-online-college-courses-from-mit')
h.update('http://www.ttznl.cn//2157.html')
print h.hexdigest()
