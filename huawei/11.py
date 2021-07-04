# @Time : 2021/4/29 20:35
# @Author : WZG
# --coding:utf-8--

l = input().split(',')
l = list(map(int, l))
n = 0
for x in l:
    print(l)
    i = l.index(x)
    if x == 0:
        del x
        continue
    if sum(l[i:i+2]) == 3:
        n += 1
        del l[i:i+2]
        continue
    elif sum(l[i:i+1]) == 2:
        n += 1
        del l[i:i+1]
        continue
    elif l[i] == 1:
        n += 1
        del l[i]
        continue


print(n)



# 1,1,0,0,0,1,1,1,0,1