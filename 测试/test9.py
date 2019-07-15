# @Time : 2019/5/16 16:14
# @Author : WZG
# --coding:utf-8--
#给定一组水果，随机选择水果，每选择一次相应的水果数量就加1，并用dict显示出来
import random


dic = {}
fruit = ['香蕉', '草莓', '苹果', '梨子', '西瓜', '芒果', '葡萄']
for i in range(100):
    f = random.choice(fruit)
    if f in dic:
        dic[f] += 1
    else:
        dic[f] = 1

print(dic)
