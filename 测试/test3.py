# @Time : 2019/5/16 10:32
# @Author : WZG
# --coding:utf-8--

L1 = [1, 2, 3, 5, 76, 'dfds']
L2 = L1[:]
print(L2)
L3 = L1.copy()
print(L3)
L4 = []
for i in L1:
    L4.append(i)

print(L4)
