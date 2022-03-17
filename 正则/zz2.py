# @Time : 2020/12/9 11:15
# @Author : WZG
# --coding:utf-8--

import re

str1 = 'the little cat cat cat is in the hat hat hat hat, we like it.'

# print(re.sub(r'(\w+)(\s\1)+', r'\1', str1))
# print(re.findall(r'(\w+)(\s\1)+', str1))

st = 'as1,2,3,4,5,6,7,8,9,cd1,2,3,cd'
m = max(re.findall(r'\d+', st))
print(re.search(r'(\d,){%s,}' %m, st).group()) # 正则中引用变量