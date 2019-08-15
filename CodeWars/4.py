# @time:  2019/8/14 10:18
# @author: WZG
# encoding: utf-8


def accum(s):
    # your code

    return '-'.join(i.upper() + i.lower() * x for x, i in enumerate(s))

