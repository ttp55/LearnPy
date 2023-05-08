# @time:  2019/8/16 13:38
# @author: WZG
# encoding: utf-8


def high(x):
    li = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    ma = []
    xx = x.split()
    for n in xx:
        q = 0
        for m in n:
            q = q + li.index(m) + 1
        ma.append(q)
    return xx[ma.index(max(ma))]

print(high('man i need a taxi up to ubud'))
