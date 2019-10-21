# @Time : 2019/9/9 14:00
# @Author : WZG
# --coding:utf-8--


def last_digit(lst):
    l = [0, 1, 4, 4, 2, 1, 1, 4, 4, 2]
    print(reversed(lst))
    for x in reversed(lst):
        print(x)
    if len(lst) == 0 or (len(lst) % 2 == 0 and sum(lst) == 0):
        return 1
    if sum(lst) == 0:
        return 0

    for t in range(-1, -len(lst), -1):
        p = lst[t - 1] % 10
        if lst[t - 1] == 1 or lst[t] == 1:
            pass
        elif lst[t] == 0:
            lst[t - 1] = 1
        elif lst[0] == lst[1] == 0:
            return 1
        elif lst[0] % 10 == 0:
            return 0
        elif p == 0 and lst[t-1] != 0 and lst[t] > 1:
            lst[t-1] = 4
        elif p == 0:
            lst[t] = 1
        elif l[p] == 1:

            lst[t - 1] = lst[t-1] ** (lst[t] % 10)

        else:
            lst[t - 1] = lst[t-1] ** ((lst[t] % l[p]) + l[p])
        print(t)
        print(p)
        print(lst)
    return lst[0] % 10


#print(last_digit([2, 2, 101, 2]))
#print(last_digit([2, 0, 1]))
print(last_digit([7, 6, 2]))
