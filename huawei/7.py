# @Time : 2021/4/26 13:55
# @Author : WZG
# --coding:utf-8--

while True:
    try:
        n = int(input())
        l = []
        while n:
            m = input()
            l.append(m)
            n -= 1
        for i in l:
            s = set(i)
            q = list(i)
            p = []
            for j in s:
                p.append(q.count(j))
            p.sort(reverse=True)
            d = 26
            t = 0
            for x in p:
                t = t + (x * d)
                d -= 1
            print(t)
    except:
        break
