#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'WZG'

from enum import Enum


Mouth = Enum('Mouth', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Mouth.__members__.items():
    print(name, '=>', member, ',', member.value)

