# @time:  2019/8/14 14:18
# @author: WZG
# encoding: utf-8


def array_diff(a, b):
    for i in b:
        if a.count(i) > 0:
            a.remove(i)
    return a


array_diff([1,2], [1])
