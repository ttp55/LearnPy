# @Time : 2021/5/20 15:03
# @Author : WZG
# --coding:utf-8--
l = []
m = 0
p = 0
while True:
    try:
        n = int(input())
        if n < 0:
            l.append(n)
        else:
            m += n
            p += 1
    except:
        break

print(len(l))
print(round(m/p, 1) if m > 0 else 0.0)

