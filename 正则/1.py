# @Time : 2020/8/13 14:37
# @Author : WZG
# --coding:utf-8--
import re

st = 'q j g wh owmh DF ar, dd ff 1212HFO2#$%&(.'
print(re.search(r'[A-Z]+', st))

print(re.match(r'[a-z]+', st))

print(re.search(r'\w', st))
print(re.search(r'^q', st))
print(re.search(r'\d+', st))
print(re.search(r'[0-9]+', st))
print(re.search(r'.*', st))
print(re.search(r'\D*', st))
print(re.search(r'\D+', st))
print(re.match(r'/[A-Z]/+', st))


print(re.findall(r'[A-Z]+', st))
