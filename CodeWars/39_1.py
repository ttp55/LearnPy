# @Time : 2019/9/2 11:19
# @Author : WZG
# --coding:utf-8--


def list_squared(m, n):
    p = []
    for x in range(m, n+1):
        l = []
        i = 1
        while i <= x:
            if x % i == 0:
                l.append(i)
            i += 1
        z = sum(map(lambda y: y ** 2, l))
        if z ** (1/2) % 1 == 0:
            p.append([x, z])
    return p


print(list_squared(1, 250))
