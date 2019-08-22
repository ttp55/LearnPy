# @time:  2019/8/15 16:19
# @author: WZG
# encoding: utf-8


def isValid(s):
    stack = []
    start = ['(', '{', '[']
    MAP = {')': '(', '}': '{', ']': '['}
    for v in s:
        if v in start:
            stack.append(v)
        else:
            if stack == []:
                return False
            if MAP[v] == stack[-1]:
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True
    else:
        return False



print(isValid("()()"))
