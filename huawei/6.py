# @Time : 2021/4/26 10:47
# @Author : WZG
# --coding:utf-8--
while True:
    try:
        num = int(input())
        mode = int(input())
        ls = []
        while num:  # 以 (名字，成绩) 的格式存入列表
            entry = input().split(' ')
            ls.append((entry[0], int(entry[1])))
            num -= 1
        ls.sort(key=lambda x: x[1], reverse= False if mode else True)  # 根据成绩排序
        for e in ls:
            print(e[0], e[1])  # print 函数中“,”是加个空格，“+”是直接连接
    except:
        break

