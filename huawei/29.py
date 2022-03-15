# @Time : 2022/3/15 14:25
# @Author : WZG
# --coding:utf-8--
num = int(input())
num = bin(num).replace('0b', '')
s = ''.join(str(abs(int(i)-1)) for i in num)

print(int(s, 2))