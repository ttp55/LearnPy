# @Time : 2019/11/12 10:04
# @Author : WZG
# --coding:utf-8--

'''
获取一个文件夹下所有文件绝对路径
import os
f = os.listdir('C:/Users/h/Desktop')
for fx in f:
    print(os.path.realpath(fx))
'''

'''
x = [1, 2, 3]
y = [4, 5, 6]
z = [7, 8, 9]
xyz = list(zip(x, y, z))
unxyz = zip(*xyz)
print(xyz)
print(list(unxyz))
'''

'''
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


f = fib(6)
try:
    while True:
        print(next(f))
except:
    print('stop')
'''
'''
dic = {'name':'tom', 'age':'15'}
del dic['name']
print(dic)
dic.update({'Name':'rose'})
print(dic)
'''
'''
def demo(args_f, *args_v):
    print(args_f)
    for x in args_v:
        print(x)
demo('a', 'b', 'c', 'd')

def demo1(**kwargs):
    for k, v in kwargs.items():
        print(k, v)

demo1(name='tom')
'''