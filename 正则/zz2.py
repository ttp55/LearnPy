# @Time : 2020/12/9 11:15
# @Author : WZG
# --coding:utf-8--

import re

str1 = 'the little cat cat cat is in the hat hat hat hat, we like it.'

print(re.sub(r'(\w+)(\s\1)+', r'\1', str1))
print(re.findall(r'(\w+)(\s\1)+', str1))
