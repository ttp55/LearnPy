#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'WZG'


import json


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


s = Student('Bob', 20, 99)


def student_dict(d):
    return Student(d['name'], d['age'], d['score'])


f = json.dumps(s, default=lambda obj: obj.__dict__)
print(json.loads(f, object_hook=student_dict))

obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=False)
print(s)
