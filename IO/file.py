#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'WZG'

import os
'''
print(os.name, os.environ.get('PATH'))
print(os.environ.get('x', 'default'))
#显示当前绝对路径
print(os.path.abspath('.'))
#添加或合并一个路径
os.path.join('D:/', 'testdir')
#创建一个路径
os.mkdir('D:/testdir')
#删除一人路径
os.rmdir('D:/testdir')
#拆分一个路径
print(os.path.split('C:/Users/Administrator/Desktop/py.txt'))
#重命名一个文件
#os.rename('C:/Users/Administrator/Desktop/py.txt', 'C:/Users/Administrator/Desktop/python.txt')
#删除一个文件
#os.remove('test.py')
#列出当前目录下的所有目录
b = [x for x in os.listdir('D:/learn py/') if os.path.isdir('D:/learn py/'+x)]
print(b)
#列出所有.py的文件
f = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']
print(f)
'''
'''


root = input('please input root:')
keyword = input('please input keyword:')


def getfile(path,key):
    if (key in os.path.split(path)[1]):
        print("result: "+path)


def iter(road):
    for x in os.listdir(road):
        if os.path.isfile(os.path.join(road,x)):
            getfile(os.path.join(road,x),keyword)
        else:
            iter(os.path.join(road,x)+'/')
iter(root)
'''
r = 'C:\Users\lenovo\PycharmProjects\LearnPy'
k = 'z'
#递归查找一个目录下的文件，并返回文件名包含特定字符串的文件路径
#x是文件名，通过join拼接成路径


def find_str(root):
    for x in os.listdir(root):
        if os.path.isdir(os.path.join(root, x)):
            find_str(os.path.join(root, x))
        else:
            if k in os.path.split(os.path.join(root, x))[1]:
                print(os.path.join(root, x))


try:
    find_str(r)
except Exception as e:
    print('error: %s' % e)
