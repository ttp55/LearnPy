# @Time : 2021/4/25 9:58
# @Author : WZG
# --coding:utf-8--

while True:
    try:
        b = int(input())
        l = []
        for i in range(b):
            a = int(input())
            if a not in l:
                l.append(a)
        l.sort()
        for x in l:
            print(x)
    except:
        break
