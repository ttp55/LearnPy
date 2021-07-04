# @Time : 2021/6/10 15:50
# @Author : WZG
# --coding:utf-8--

my_list = [1, 3, 5, 7, 9]


def binary_search(list, item):
    low = 0
    high = len(my_list)-1

    while low <= high:
        mid = int((low + high) / 2)
        guess = list[mid]

        if guess == item:
            return mid, guess
        if guess < item:
            low = mid + 1
        else:
            high = mid - 1
    return None

# 简单查找线性时间为 O(n) 二分法查找线性时间为 O(log n)


print(binary_search(my_list, 3))
print(binary_search(my_list, -1))
