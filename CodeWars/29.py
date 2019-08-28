# @time:  2019/8/23 15:28
# @author: WZG
# encoding: utf-8


def permutations_(string):
    p = []
    l = list(string)
    for i in l:
        p.append(''.join(i))
    return p


print(permutations_('aabb'))
