# @time:  2019/8/29 15:31
# @author: WZG
# encoding: utf-8


def first_non_repeating_letter(string):
    l = list(string)
    try:
        return string[min(l.index(i) for i in l if l.count(i) == 1)]
    except:
        return ''


print(first_non_repeating_letter('sTreSS'))
