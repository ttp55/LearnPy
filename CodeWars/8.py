# @time:  2019/8/15 14:17
# @author: WZG
# encoding: utf-8


def valid_parentheses(string):
    # your code here
    l = []
    for i in list(string):
        if i in '()':
            l.append(i)
    for x in l:
        m = l[1:]
        for y in m:
            if ord(x) - ord(y) == -1:
                l.remove(x)
                l.remove(y)
                continue

    if len(l) == 0:
        return True
    else:
        return False


print(valid_parentheses("())("))

