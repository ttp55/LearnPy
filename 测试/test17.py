# @Time : 2019/5/21 14:49
# @Author : WZG
# --coding:utf-8--


def jinzita(a):
    for x in range(1, a + 1):
        print(' ' * (a - x) + '*' * (2 * x - 1))


jinzita(60)
