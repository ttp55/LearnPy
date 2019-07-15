def sumS(*a):
    def sum():
        x=0
        for n in a:
            x=x+n
        return x
    return sum

print(sumS(1,2,3,5,6,7,7,8,8))
f=sumS(1,35,5,6,7,8,6798,8)
f1=sumS(3,432,42,42,42,52,4332)
print(f())
print(f1())
print(f)#每次调用sumS都会返回一个新的函数
print(f1)



