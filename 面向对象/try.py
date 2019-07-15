#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'WZG'


try:
    print('try...')
    r = 10 / int('a')
    print('result:', r)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
except ValueError as e:
    print('ValueError:', e)
finally:
    print('finally...')
print('END')
