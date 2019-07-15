# @Time : 2019/5/15 15:19
# @Author : WZG
# --coding:utf-8--

for i in range(1, 5):
    for j in range(1, 5):
        if j == i:
            continue
        for n in range(1, 5):
            if n == i or j == n:
                continue
            print(i, j, n)
