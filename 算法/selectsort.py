# @Time : 2021/6/16 9:51
# @Author : WZG
# --coding:utf-8--


def findsmall(arr):
    small = arr[0]
    smallindex = 0
    for i in range(1, len(arr)):
        if arr[i] < small:
            small = arr[i]
            smallindex = i
    return smallindex


def selecttionsort(arr):
    newArr = []
    for i in range(len(arr)):
        small = findsmall(arr)
        newArr.append(arr.pop(small))
    return newArr


print(selecttionsort([5, 3, 6, 2, 10]))
