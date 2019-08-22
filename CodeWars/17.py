# @time:  2019/8/21 15:39
# @author: WZG
# encoding: utf-8


def two_sum(numbers, target):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                print(i, j)
                return [i, j]


print(two_sum([2, 2, 3], 4))
