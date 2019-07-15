def createCounter():
    n=[0]
    def counter():
        n[0]=n[0]+1
        return n[0]
    return counter
counterA=createCounter()
counterB=createCounter()
print(counterA(),counterA(),counterA(),counterA(),counterA())
print(counterB(),counterB(),counterB())
print(counterA())
