# @time:  2019/8/23 14:43
# @author: WZG
# encoding: utf-8

na = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]


def who_is_next(names, r):
    while r > 5:
        r = (r - 4) / 2
    return names[r-1]


print(who_is_next(na, 7230702951))
