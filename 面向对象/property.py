#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'WZG'


class Student(object):

    #def __init__(self, score):
    #    self.__score = score

    #@property
    def score(self):
        return self.__score

    #@score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError("score must be integer!")
        if value < 0 or value > 100:
            raise ValueError("score must between 0 ~ 100!")
        else:
            self.__score = value


s = Student()
s.score = 90
print(s.score)
