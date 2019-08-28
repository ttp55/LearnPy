# @Time : 2019/8/23 8:42
# @Author : WZG
# --coding:utf-8--


def count_smileys(arr):
    x = 0
    for i in arr:
        if (';' and 'D' in i) or (':' and 'D' in i) or (';' and ')' in i) or (':' and ')' in i):
            l = list(i)
            if (l[0] == ';') or (l[0] == ':'):
                x += 1
            else:
                return None
    return x


print(count_smileys([')', ':(', 'D', ':O', ':;']))
