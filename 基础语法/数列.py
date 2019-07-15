def fib(max):
    a , b , n = 0 , 1 , 0
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done!'
#for f in fib(10):#取不到return的返回值，下面while可以取，需要try
#   print(f)

f=fib(10)
while True:
    try:
        x=next(f)
        print(x)
    except StopIteration as e:
        print(e.value)
        break