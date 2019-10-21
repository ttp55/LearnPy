# @Time : 2019/9/4 9:01
# # @Author : WZG
# --coding:utf-8--

import time
from pymouse import PyMouse
from pykeyboard import PyKeyboard


k = PyKeyboard()
m = PyMouse()
a = m.position()
print(a)

m.click(699, 367)
k.type_string('1、预先飞行计划管理系统功能测试（6）')
