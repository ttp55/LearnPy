# @Time : 2019/11/20 15:54
# @Author : WZG
# --coding:utf-8--

p = list(range(1, 31))
i = 8
while len(p) > 15:
    p.pop(i)
    i = i + 9
    if i > len(p)+1:
        i = i - len(p)+1
    print(p)


