# @time:  2019/8/22 15:11
# @author: WZG
# encoding: utf-8


def rot13(s):
    d = {chr(i+c): chr((i + 13) % 26 + c) for i in range(26) for c in (65, 97)}
    return ''.join([d.get(c, c) for c in s])


print(rot13('sfafaSDFfjS'))
