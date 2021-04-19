# @Time : 2021/4/19 9:29
# @Author : WZG
# --coding:utf-8--

from 数据结构 import date_stack

s = date_stack.Stack(10)


def zhuanhuan(n):
    while n > 0:
        s.push(int(n%2))
        n = (n-(n%2))/2
    print(s.stack)


zhuanhuan(138)
