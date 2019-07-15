# @Time : 2019/5/13 9:22
# @Author : WZG
# --coding:utf-8--


def count(*args):
    def cou():
        x = 0
        for i in args:
            x = x + i
        return x
    return cou


f = count(1, 8, 6, 5)
print(f)
print(f())
