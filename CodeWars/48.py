# @Time : 2019/9/18 13:51
# @Author : WZG
# --coding:utf-8--

list1 = ['a1', 'b', 'a', 'a', 'b', 'c']


def do_string(l):
    l1 = set(l)
    for x in l1:
        if l.count(x) > 1:
            for i in range(1, l.count(x) + 1):
                l[l.index(x)] = x + str(i)
    return l


print(do_string(list1))
