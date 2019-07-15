from functools import reduce

def pord(l):
    return reduce(lambda x,y:x*y,l)

print(pord(list(range(3,10,2))))
