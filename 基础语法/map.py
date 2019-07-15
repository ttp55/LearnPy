from functools import reduce
def f(x):
    return x*x
r=map(f,range(1,10))
print(list(r))
l=list(map(str,range(1,10)))
print(l)

print(sum(range(1,101)))

def ss(x,y):
    return x*10+y
print(reduce(ss,range(1,10,2)))
