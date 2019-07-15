# @Time : 2019/5/22 9:36
# @Author : WZG
# --coding:utf-8--

day = int(input('输入一个1到11的数字：'))


def mounkey(a):
    if a == 2:
        n = 4
    else:
        n = (mounkey(a - 1) + 1) * 2
    return n


print(mounkey(day))
