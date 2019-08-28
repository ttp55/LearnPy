# @time:  2019/8/23 14:26
# @author: WZG
# encoding: utf-8
import sys


na = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]


def whr(names, r):
    n = 0
    while n < r:
        yield names
        names.append(names[0])
        names.append(names[0])
        names.pop(0)
        n += 1
    return names[0]


def who_is_next(names, r):
    f = whr(names, r)
    while True:
        try:
            next(f)
        except StopIteration as e:
            print(e.value)
            break


who_is_next(na, 522222)
