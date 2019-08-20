# @time:  2019/8/20 14:07
# @author: WZG
# encoding: utf-8


def triangles(k):
    p = [1]
    n = 0
    l = []
    while n <= k:
        p = [1] + [p[i] + p[i+1] for i in range(len(p)-1)] + [1]
        l = p + l
        n += 1
    return l[::-1]


print(triangles(5))
