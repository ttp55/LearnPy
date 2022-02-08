# @Time : 2021/12/28 10:06
# @Author : WZG
# --coding:utf-8--
import math
n = int(input())
for i in range(2, int(math.sqrt(n))+1):
    while n % i == 0:
        print(i, end=' ')
        n = n // i
if n > 2:
    print(n)