# @time:  2019/8/20 10:51
# @author: WZG
# encoding: utf-8


def delete_nth(s, m):
    # code here
    o = s[::-1]
    for x in o:
        if o.count(x) > m:
            for i in range(o.count(x) - m):
                o.remove(x)
    return o[::-1]


print(delete_nth([20, 37, 20, 21], 1))
