#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'WZG'


def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    try:
        bar('0')
    except ZeroDivisionError as e:
        print('Error:', e)
    finally:
        print('finally...')

main()
