# @time:  2019/8/13 15:14
# @author: WZG
# encoding: utf-8


def find_short(s):
    print(s.split())
    return min(len(i) for i in list(s.split()))


print(find_short("bitcoin take over the world maybe who knows perhaps"))
