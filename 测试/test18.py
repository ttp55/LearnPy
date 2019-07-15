# @Time : 2019/5/22 9:06
# @Author : WZG
# --coding:utf-8--


def list_rewrite():
    a = input('输入一个数字：')
    l = list(map(int, a))
    for i in range(len(l)):
        if l[i] % 2 == 0:
            l[i] = int(l[i] / 2)
        else:
            l[i] = l[i] ** 2
    print(l)


list_rewrite()
