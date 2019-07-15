#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'WZG'
'''
try:
    f = open('C:/Users/Administrator/Desktop/py.txt', 'r')
    print(f.read(100))
finally:
    if f:

with open('C:/Users/Administrator/Desktop/py.txt', 'r') as r:
##    print(r.readline(), r.readline())
    for line in r.readlines():
        print(line.strip())
'''
#with open('C:/Users/Administrator/Desktop/21.png', 'rb') as q:
#  print(q.read())


with open('C:/Users/Administrator/Desktop/py.txt', 'a') as w:
    w.write('Hello Python!')

