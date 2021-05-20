# @Time : 2021/5/20 15:21
# @Author : WZG
# --coding:utf-8--
import re
l = input()
l = re.split('\W+', l)[::-1]
print(''.join(x+' ' for x in l))