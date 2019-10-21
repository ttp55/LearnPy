# @Time : 2019/9/11 15:19
# @Author : WZG
# --coding:utf-8--
import random


def touzi(numm):
    i = 1
    x = numm * 6
    l = []
    s = set()
    for j in range(6, x):
        s.add(j)
    s.add(sum(l))
    print(s)


touzi(10)
