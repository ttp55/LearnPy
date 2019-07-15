# @Time : 2019/5/16 14:17
# @Author : WZG
# --coding:utf-8--


def count(mounth):
    a = [1, 1, 2]
    if mounth <= 3:
        return a[0: mounth]
    else:
        a = a.pop(a[count(mounth-2)] + a[count(mounth-4)])
        return a


print(count(11))
