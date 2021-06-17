# @Time : 2021/6/16 14:55
# @Author : WZG
# --coding:utf-8--
# 有一块地要分成小方块，不能有剩余，找出能分成的最大方块，以下是递归算法。 后来发现，这个问题的解决与找两个数的最大公因数一样


def DC(x, y):
    if x < y:
        x, y = y, x
    if x % y == 0:
        return y
    else:
        return DC(x-y*(x//y), y)


print(DC(1680, 640))

