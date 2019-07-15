def creatCounter():
    def f():
        x = 0
        while True:
            x = x + 1
            yield x

    sum = f()

    def counter():
        return next(sum)

    return counter


counterA=creatCounter()
counterB=creatCounter()
print(counterA,counterA,counterA,counterA,counterA)
print(counterB,counterB,counterB)