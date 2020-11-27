# @Time : 2019/9/4 9:01
# @Author : WZG
# --coding:utf-8--

import time
from pymouse import PyMouse
from pykeyboard import PyKeyboard

# data_b = '1、预先飞行计划管理系统功能测试（6）'
k = PyKeyboard()
m = PyMouse()
a = m.position()
print(a)

time.sleep(10000)

m.click(939, 1105)

k.type_string('hello')
