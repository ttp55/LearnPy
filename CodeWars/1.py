# @time:  2019/8/13 10:30
# @author: WZG
# encoding: utf-8


def nb_year(p0, percent, aug, p,):
    i = 0
    while True:
        p0 = p0 + p0 * percent + aug
        i += 1
        if p0 >= p:
            return i


print(nb_year(1500000, 0.25, 1000, 2000000))
