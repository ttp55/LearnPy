# @Time : 2019/5/16 14:43
# @Author : WZG
# --coding:utf-8--


def jisuan(a):
    if a % 2 == 0:
        s = a / 2
        print(s)
    if a % 2 == 1:
        s = a * 3 + 1
        print(s)
    if s == 1:
        print(s)
    else:
        jisuan(s)


jisuan(1000)
