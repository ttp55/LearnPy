# @Time : 2019/10/29 9:45
# @Author : WZG
# --coding:utf-8--
from sympy import *


def sympy_derivative():
    # 定义表达式的变量名称
    a, x = symbols('a x')
    Y = x**2 + pi*((a-4*x)/2*pi)**2
    #Y = 2*a/p + (8/p-2) * x
    return diff(Y, x)

y = symbols('y')
f = y ** 2
print(diff(f, y))
print(sympy_derivative())
