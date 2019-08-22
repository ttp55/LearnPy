# @time:  2019/8/21 16:02
# @author: WZG
# encoding: utf-8
from functools import reduce


def find_even_index(arr):
    print(arr)
    if len(arr) == 1:
        return 0
    if reduce(lambda x, y: x + y, arr[1:]) == 0:
        return 0
    elif reduce(lambda x, y: x + y, arr[:-1]) == 0:
        return len(arr) - 1
    for i in range(1, len(arr) - 1):
        if reduce(lambda x, y: x + y, arr[0:i]) == reduce(lambda x, y: x + y, arr[i + 1:]):
            return i

    return -1


print(find_even_index([10,-80,10,10,15,35,20]))
