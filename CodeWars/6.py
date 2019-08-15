# @time:  2019/8/15 9:38
# @author: WZG
# encoding: utf-8


def to_camel_case(text):
    l = list(text)
    for i in l:
        if i == '_' or i == '-':
            l[l.index(i) + 1] = l[l.index(i) + 1].capitalize()
            l.remove(i)

    return ''.join(l)


print(to_camel_case("the-stealth_warrior-"))
