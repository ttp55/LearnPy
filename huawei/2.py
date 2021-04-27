# @Time : 2021/4/25 14:04
# @Author : WZG
# --coding:utf-8--
import math

while True:
    try:
        a = input()
        b = math.ceil(len(a) / 8)
        for i in range(b):
            c = a[i*8:8*i+8]
            if len(c)<8:
                c = c + '0'*(8-len(c))
            print(c)

    except:
        break

