# @Time : 2022/2/17 14:55
# @Author : WZG
# --coding:utf-8--

import random
lll = 0 # 总次数
num = 1 # 扔到1时的次数
sta = [] # 保证随机的数是没扔到过的
i = 0
while i <= 10000:
    x = random.randint(1, 10) #随机1-10
    if x not in sta:
        i += 1
        sta.append(x)
        if x == 1: # 扔到1 一轮结束
            lll += num
            num = 1
            sta = []

        else: # 不是1 就接着扔
            num += 1
    else:
        i -= 1
print(lll/10000)

