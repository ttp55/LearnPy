# @Time : 2019/5/7 10:21
# @Author : WZG
# --coding:utf-8--


L = [x * x for x in range(10)]
print(L)

g = (x * x for x in range(1, 10))

for n in g:
    print(n)

