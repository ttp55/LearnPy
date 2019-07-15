#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'WZG'


class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1


s = Student('Tom')

print(s.count)

ll = Student('lisa')

print(ll.count)
