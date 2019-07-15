# @Time : 2019/5/21 13:47
# @Author : WZG
# --coding:utf-8--


def wan(a):
    for i in range(2, a):
        l = []
        for j in range(1, i):
            if i % j == 0:
                l.append(j)
            else:
                continue
        if sum(l) == i:
            print(i)


wan(30000)
