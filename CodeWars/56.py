# @Time : 2019/11/21 16:13
# @Author : WZG
# --coding:utf-8--

p = list(range(1, 31))
while len(p) > 15:
    p = p[9:] + p[0:8]
    print(p)
