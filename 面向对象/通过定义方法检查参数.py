#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'WZG'


class Student(object):

    def __init__(self, score):
        self.__score = score

    def get_score(self):
        return self.__score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError("score must be integer!")
        if value < 0 or value > 100:
            raise ValueError("score must between 0 ~ 100!")
        else:
            self.__score = value


s = Student()
s.set_score(90)
print(s.get_score())
s.set_score(33333)
print(s.get_score())
