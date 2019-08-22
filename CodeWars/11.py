# @time:  2019/8/16 14:31
# @author: WZG
# encoding: utf-8

# 同10


def high(x):

    return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))


print(high('man i need a taxi up to ubud'))
