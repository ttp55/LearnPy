#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'WZG'


class Student(object):
    def __init__(self):
        self.name = 'Tom'

    def attr(self):
         return 99


s = Student()
print(s.name)
#print(s.score)
print(hasattr(s, 'name'))
print(hasattr(s, 'age'))
#print(getattr(s, 'age'))
setattr(s, 'age', 19)
print(getattr(s, 'age'))
