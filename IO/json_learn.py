#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'WZG'


import json


d = dict(name='bob', age=20, score=88)
print(d)
j = json.dumps(d)

f = open('D:\json.txt', 'w')
json.dump(d, f)
f.close()

o = open('D:\json.txt', 'r')
print(json.load(o))
o.close()
print(json.loads(j))
print(j)

