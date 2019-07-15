def odditer():#定义一个奇数序列
    n=1
    while True:
        n=n+2
        yield n


def notdiv(n):#如果x对n取余大于0，就被filter留下
    return lambda x:x%n>0


def primes():
    yield 2
    it=odditer()
    while True:
        n=next(it)
        yield n
        it=filter(notdiv(n),it)


L = []
for q in primes():
    if q<1000:
        L.append(q)
    else:
        break
print(L)
