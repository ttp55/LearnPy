# @Time : 2020/6/3 14:25
# @Author : WZG
# --coding:utf-8--

from itertools import permutations


def permutations_(string):
    p = []
    l = list(set(list(permutations(string))))
    for i in l:
        p.append(''.join(i))
    return p


print(permutations_('aabb'))
