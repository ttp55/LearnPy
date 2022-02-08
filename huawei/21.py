# @Time : 2022/2/8 13:58
# @Author : WZG
# --coding:utf-8--

l = [1,2,3,4,5,5]
print(l[3:]+l[:3])


s = input()

while '{}' in s or '()' in s or '[]' in s:
    s = s.replace('{}', '')
    s = s.replace('[]', '')
    s = s.replace('()', '')
print(not s)
