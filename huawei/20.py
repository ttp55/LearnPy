# @Time : 2022/2/8 10:48
# @Author : WZG
# --coding:utf-8--

a = list(map(int, input().split(',')))

s, p = [], 0

while p < len(a):
    if not s or s[-1] < 0 or a[p] > 0:
        s.append(a[p])
    elif s[-1] <= -a[p]:
        if s.pop() < -a[p]:
            continue
    p += 1
print(s)
