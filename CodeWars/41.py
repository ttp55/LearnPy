# @Time : 2019/9/5 13:37
# @Author : WZG
# --coding:utf-8--
import itertools


def next_smaller(n):
    l = list(itertools.permutations(str(n)))
    p = []
    q = []
    for i in l:
        p.append(list(i))
    print(p)
    for j in p:
        m = int(''.join(x for x in j))
        q.append(m)
    q = sorted(q)
    return q[q.index(n) - 1]


print(next_smaller(2017))
