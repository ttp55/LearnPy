#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'WZG'


class Student(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2019 - self._birth


s = Student()
s.birth = 1997
print(s.birth)
print(s.age)
#s.age = 10
