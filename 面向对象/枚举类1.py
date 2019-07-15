#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'WZG'

from enum import Enum, unique


@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


day1 = Weekday.Fri
print(day1)
print(Weekday.Thu)
print(Weekday.Mon.value)
print(Weekday['Sat'])
print(day1 == Weekday.Fri)
print(Weekday(3))

for name, member in Weekday.__members__.items():
    print(name, '=>', member)
