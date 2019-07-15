#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'WZG'

from enum import Enum, unique


@unique
class Gender(Enum):
    male = 0
    female = 1


class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


bart = Student('Bart', Gender.male)
print(bart.gender == Gender.male)
lart = Student('Lart', Gender.male)
print(lart.gender == Gender.male)
print(bart.gender.value, lart.gender.value)
