# @Time : 2022/3/14 14:20
# @Author : WZG
# --coding:utf-8--
import math

stt = sorted(list(map(ord, input())))
cen = math.ceil(len(stt) / 2)
s1 = stt[:cen]
s2 = stt[cen:]
j, n = 0, 0
fin = []
print(stt)
while len(fin) < len(stt):
    fin.append(s1[n])
    if len(s2) > n:
        fin.append(s2[n])
        n += 1
print(fin)
print(list(map(chr, fin)))
