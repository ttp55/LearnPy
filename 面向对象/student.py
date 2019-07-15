#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'WZG'


class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s:%s' % (self.__name, self.__score))

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_name(self, name):
        self.__name = name

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')


bart = Student('Jim', 55)
Tom = Student('Tom', 90)
print(bart.get_name(), bart.get_score(), bart.get_grade())
print(Tom.get_name(), Tom.get_grade())
Tom.print_score()
bart.set_score(88)
#bart = Student('jjjim', 99)
print(bart.get_name(), bart.get_score(), bart.get_grade())
