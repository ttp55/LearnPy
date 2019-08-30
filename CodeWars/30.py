# @time:  2019/8/26 13:58
# @author: WZG
# encoding: utf-8


def lcs(x, y):
    l = []
    i = 0
    for p in y:
        if p in x[i:]:
            l.append(p)
            i = x.index(p) + 1
    return ''.join(l)


print(lcs("132535365", "1234567893"))

