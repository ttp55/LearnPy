# @Time : 2019/8/22 8:43
# @Author : WZG
# --coding:utf-8--
l1= [1, 4, 8, 7, 3, 15]
l2= [1, -2, 3, 0, -6, 1]
l3= [20, -13, 40]
l4= [1, 2, 3, 4, 1, 0]
l5= [10, 5, 2, 3, 7, 5]
l6= [4, -2, 3, 3, 4]
l7= [0, 2, 0]
l8= [5, 9, 13, -3]


def sum_pairs(ints, s):
    l = []
    v = []
    m = []
    for i in range(len(ints)):
        for j in range(i + 1, len(ints)):
            if ints[i] + ints[j] == s:
                l.append([i, j])
    for x in l:
        v.append(x[1] - x[0])
    if l:
        m = l[v.index(min(v))]
        return [ints[m[0]], ints[m[1]]]
         # return [ints[i], ints[j]]
    return None


print(sum_pairs(l5, 10))
