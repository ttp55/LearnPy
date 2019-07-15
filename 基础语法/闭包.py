def count():
    fs=[]
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs

f1,f2,f3=count()
print(f1())
print(f2())
print(f3())
# 返回闭包时牢记一点：返回函数不要引用任何循环变量，或后续会发生变化的变量
