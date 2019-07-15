#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'WZG'

import pickle


d = dict(name='bob', age=20, score=88)
p = pickle.dumps(d)
print(p)
f = open('D:\dump.txt', 'wb')
pickle.dump(p, f)
f.close()
o = open('D:\dump.txt', 'rb')
print(pickle.load(o))
o.close()

