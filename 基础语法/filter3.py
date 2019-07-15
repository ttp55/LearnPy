def hui(u):
    return u == int(str(u)[::-1])
#[::-1] 含义：输出倒序字符串，[::-2] 含义：倒序输出跨越一个字符  [:-1] 含义：输出字符串从第一个字符到倒数第二个

L = range(0, 100000, 1)


def p():
    it = list(filter(hui, L))#用filter取回数
    print(it)


p()
