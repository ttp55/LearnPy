# @Time : 2019/8/23 8:42
# @Author : WZG
# --coding:utf-8--


def count_smileys(arr):
    x = 0
    for i in arr:
        if ';' and 'D' in i:
            x += 1
        elif ':' and 'D' in i:
            x += 1
        elif ';' and ')' in i:
            x += 1
        elif ':' and ')' in i:
            x += 1
    return x


print(count_smileys([':)',':(',':D',':O',':;']))
