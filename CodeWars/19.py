# @time:  2019/8/22 10:04
# @author: WZG
# encoding: utf-8
l1= [1, 4, 8, 7, 3, 15]
l2= [1, -2, 3, 0, -6, 1]
l3= [20, -13, 40]
l4= [1, 2, 3, 4, 1, 0]
l5= [5, 2, 5, 3, 10, 7]
l6= [4, -2, 3, 3, 4]
l7= [0, 2, 0]
l8= [5, 9, 13, -3]


def sum_pairs(lis, s):
    cache = []
    for i in lis:
        other = s - i
        if other in cache:
            return [other, i]
        cache.append(i)
    return None


print(sum_pairs(l5, 10))

