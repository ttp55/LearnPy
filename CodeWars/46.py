# @Time : 2019/9/10 10:40
# @Author : WZG
# --coding:utf-8--


def last_digit(lst):
    n = 1
    for x in lst[::-1]:
        print(n)
        n = x ** (n if n < 4 else n % 4 + 4)
        print(x)
    return n % 10


print(last_digit([754, 6454, 4542]))
