# @time:  2019/8/28 10:41
# @author: WZG
# encoding: utf-8


def isPP(n):
    for i in range(1, n):
        for j in range(1, n):
            if pow(i, j) == n:
                return [i, j]
    return None


print(isPP(1024))
