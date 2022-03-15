# @Time : 2022/3/14 15:27
# @Author : WZG
# --coding:utf-8--

cache = set()
def func(selects, lasts):
    if selects in cache:
        return None
    if not lasts:
        return selects
    for i in range(len(lasts)):
        if not selects:
            ret = func(lasts[i], lasts[:i] + lasts[i + 1:])
            if ret:
                return ret
        else:
            if abs(ord(selects[-1]) - ord(lasts[i])) != 1:
                ret = func(selects + lasts[i], lasts[:i] + lasts[i + 1:])
                if ret:
                    return ret
    cache.add(selects)
    return None


print(func("", "abbbbbbbbcddddddddddddddddddddd"))

