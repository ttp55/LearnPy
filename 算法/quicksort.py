# @Time : 2021/6/17 10:03
# @Author : WZG
# --coding:utf-8--
import random


def quicksort(array):
    if len(array) < 2:
        return array
    else:
        cankao = array[random.randint(0, len(array))]
        left = [i for i in array if i < cankao]
        right = [i for i in array if i > cankao]
    return quicksort(left) + [cankao] + quicksort(right)


print(quicksort([10, 5, 6, 48, 62, 1]))
