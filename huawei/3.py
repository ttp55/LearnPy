# @Time : 2021/4/25 14:48
# @Author : WZG
# --coding:utf-8--
while True:
    try:
        a = input()
        l = a.split()
        l = list(map(int, l))
        print(sum(l))
    except:
        break