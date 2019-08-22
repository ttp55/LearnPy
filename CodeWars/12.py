# @time:  2019/8/16 14:48
# @author: WZG
# encoding: utf-8


def oddOrEven(arr):
    return 'even' if sum(arr) % 2 == 0 else 'odd'


print(oddOrEven([0, 1, 2]))
