# @time:  2019/8/13 10:47
# @author: WZG
# encoding: utf-8


def high_and_low(numbers):
    return "".join(x(numbers.split(), key=int) for x in (max, min))


print(high_and_low([1, 34, 5]))

