# @time:  2019/8/23 14:04
# @author: WZG
# encoding: utf-8

n = 0
na = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]


def who_is_next(names, r):
    global n
    print(names)
    while n < r:
        names.append(names[0])
        names.append(names[0])
        names.pop(0)
        who_is_next(names, n)
        n += 1
    return names[0]


print(who_is_next(na, 52))
