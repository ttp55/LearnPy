# @Time : 2022/2/7 14:14
# @Author : WZG
# --coding:utf-8--


tpre = list(map(int, input().split(',')))
#l = []
m = []
for i in range(len(tpre)):
    s = len(m)
    for j in range(1, len(tpre[i:])):
        if tpre[i:][j] > tpre[i]:
           # print(tpre.index(tpre[i:][j]), i, j)
           # l.append(tpre.index(tpre[i:][j]) - i)
            m.append(j)
            break
    if len(m) == s:
       #  l.append(0)
        m.append(0)
#print(l)
print(m)
