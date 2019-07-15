# @Time : 2019/5/16 10:39
# @Author : WZG
# --coding:utf-8--
#题目：古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子， 小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死， 问每个月的兔子对数为多少？


def count(mounth):
    a = [1, 1, 2]
    i = 3

    if mounth <= 3:
        return a[0: mounth]
    while i < mounth:
        a.append(a[i-1] + a[i-3])
        i += 1
    return a


print(count(11))








