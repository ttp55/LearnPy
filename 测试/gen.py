# @Time : 2019/5/7 14:52
# @Author : WZG
# --coding:utf-8--


def fib(max):
    n, a, b, = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


def odd():
    yield 1
    yield 2
    yield 3
    yield 4


f = fib(10)
print(f)
for i in fib(10):
    print(i)


for x in odd():
    print(x)
