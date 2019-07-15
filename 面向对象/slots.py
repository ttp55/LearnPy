#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'WZG'


import types


class Student(object):
    __slots__ = ('name', 'age')

#slots 对其子类不起作用，除非其子类也定义了slots，这样子类的限制就变成了父类的限制加上本身的限制


s = Student()
s.name = 'Tom'
print(s.name)
s.age = 25
print(s.age)
#报错，因为__slots__限制了增加的属性
s.score = 88
print(s.score)
