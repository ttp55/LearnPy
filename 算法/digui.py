# @Time : 2021/6/16 13:54
# @Author : WZG
# --coding:utf-8--


def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x-1)


print(fact(5))
