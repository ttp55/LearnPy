# @Time : 2021/4/26 9:46
# @Author : WZG
# --coding:utf-8--


while True:
    try:
        n = int(input())
        a = int(input())
        dic = {}
        for i in range(n):
            d = input()
            d = d.split()
            dic[d[0]] = d[1]
        if a == 0:
            f = dict(sorted(dic.items(), key=lambda item: item[1], reverse=True))
        else:
            f = dict(sorted(dic.items(), key=lambda item: item[1], reverse=False))

        for v, k in f.items():
            print(v, k)
    except:
        break

