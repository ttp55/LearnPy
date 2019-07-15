a = 20
b = 20
print(id(a))
print(id(b))

if ( a is b ):
    print("a b 有相同标识")
else:
    print("a b 没有相同标识")
if (id(a) == id(b)):
    print("a b 有相同标识")
else:
    print("a b 没有相同标识")
a = 30
print(id(a))
if ( a is b ):
    print("a b 有相同标识")
else:
    print("a b 没有相同标识")
if ( a is not b):
    print("a b 没有相同标识")
else:
    print("a b 有相同标识")