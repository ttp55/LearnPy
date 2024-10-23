# @Time : 2024/10/23 15:38
# @Author : WZG
# --coding:utf-8--
import random

l = []
a = []

while len(l)<100:
    l.append([1,1,1,1,0,0,0])

for i in l:
    random.shuffle(i)
    a.append(i)
print(a)