class firstClass:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        if(self.a<20):
            x=self.a
            self.a+=1
            return x
        else:
            raise StopIteration

myClass=firstClass()#实例化类
iterCLass=iter(myClass)#创建迭代器对象
#for x in iterCLass:
print(next(iterCLass))
print(next(iterCLass))
print(myClass)
print(iterCLass)
print(next(myClass))
print(next(myClass))
while True:
    try:
        print(next(iterCLass))
    except StopIteration as e:
        print(e.value)
        break
print(dir())