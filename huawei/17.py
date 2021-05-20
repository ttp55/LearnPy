# @Time : 2021/5/20 16:20
# @Author : WZG
# --coding:utf-8--
import re
print(''.join(x+' ' for x in re.split('\W+', input())[::-1]))