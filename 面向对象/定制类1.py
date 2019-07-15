# @Time : 2019/5/14 14:48
# @Author : WZG
# --coding:utf-8--


class Fib(object):
    def __init__(self):
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.b + self.a
        if self.a > 10000:
            raise StopIteration()
        else:
            return self.a


for n in Fib():
    print(n)
