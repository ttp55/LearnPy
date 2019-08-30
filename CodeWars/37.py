# @time:  2019/8/30 11:11
# @author: WZG
# encoding: utf-8

s = [3, 1, 2, 3, 2, 1, 3, 2, 2, 3, 1, 1, 1]
s1 = [s[x: x + 3] for x in range[0, 12, 3]]
print(s1)