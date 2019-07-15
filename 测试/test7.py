# @Time : 2019/5/16 15:08
# @Author : WZG
# --coding:utf-8--


for i in range(100, 1000):
    a = list(map(int, str(i)))
    if i == a[0]**3 + a[1]**3 + a[2]**3:
        print(i)
