# @time:  2019/8/28 10:48
# @author: WZG
# encoding: utf-8
import math


def isPP(n):
    for i in range(2, n):
        j = n ** (1/i)
        m = math.modf(j)
        if m[0] < 0.0000000001 or m[0] > 0.999999999999:
            return [round(j), i]
    return None


print(isPP(125))
print(math.log(125, 5))