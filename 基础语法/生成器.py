import sys


def ssq(n):
    a,b,c = 0,1,0
    while c<n:
        yield a
        a,b = b,a+b
        c+=1
        print("%d,%d"%(a,b))
    return
f=ssq(10)

while True:
    try:
        print(next(f),end=",")
    except StopIteration as e:
        print(e.value)
        sys.exit()
        break
