# @Time : 2022/2/16 14:12
# @Author : WZG
# --coding:utf-8--

#字符串处理输入：s = "3[a2[c]]"输出："accaccacc"

s = input()

stack = []
num = 0
res = ''
for c in s:
    if c.isdigit():
        num = num * 10 + int(c)
    elif c == '[':
        stack.append((res, num))
        res = ''
        num = 0
    elif c == ']':
        top = stack.pop()
        res = top[0] + top[1] * res
    else:
        res += c
print(res)

