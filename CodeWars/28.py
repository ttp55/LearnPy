# @time:  2019/8/23 15:05
# @author: WZG
# encoding: utf-8

from itertools import permutations


def permutations_(string):
    p = []
    l = list(set(list(permutations(string))))
    for i in l:
        p.append(''.join(i))
    return p


print(permutations_('a'))
