# @Time : 2021/4/25 15:22
# @Author : WZG
# --coding:utf-8--
while True:
    try:
        a = input()
        l = []
        for i in range(1, len(a)+1):
            l.append(a[-i])

        print(''.join(l))
    except:
        break