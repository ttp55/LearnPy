# @Time : 2019/9/9 9:28
# @Author : WZG
# --coding:utf-8--


def last_digit(lst):
    l = [0, 1, 4, 4, 2, 1, 1, 4, 4, 2]
    print(lst)
    if len(lst) == 0 or (len(lst) == 2 and sum(lst) == 0):
        return 1
    if sum(lst) == 0:
        return 0
    else:
        for t in range(-1, -len(lst), -1):
            x = l[lst[t-1] % 10]
            if lst[t-1] == 0:
                lst[t-1] = 4 + x
            else:
                lst[t-1] = lst[t-1] % x + x + 4
            print(lst[t])
            print(lst)
    return lst[0] % 10


#print(last_digit([12, 30, 21]))
#print(last_digit([123232, 694022, 140249]))
#print(last_digit([2, 2, 2, 0]))
print(last_digit([7, 6, 2]))
#print(last_digit([5, 0]))
#print(last_digit([7, 11, 2]))
#print(last_digit([2147483647, 2147483647, 2147483647]))

