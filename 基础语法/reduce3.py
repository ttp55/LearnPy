from functools import reduce
q='123.456'
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def ddd(t):
    l=len(t)
    ind=t.index('.')+1
    n=10**(l-ind)
    return n
def str(g):
    return DIGITS[g]
def str2float(s):
    y=ddd(q)
    j=q.replace('.','')
    return reduce(lambda x,y:x*10+y,map(str,j))/y
print(str2float(q))

