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
'''
# 打开钉钉
m.click(110, 239)
m.click(110, 239)
time.sleep(10)

# 点击工作
m.click(434, 549)
time.sleep(5)

# 点击日志
m.click(833, 249)
time.sleep(2)

# 点击写日志
m.click(1538, 188)
time.sleep(1)
# 点击滚动条
m.click(1741, 507)
time.sleep(1)
# 点击系统测试输入框
m.click(782, 576)
time.sleep(0.5)
k.type_string(data_b)
# 点击滚动条
m.click(1734, 794)
time.sleep(1)
'''

time.sleep(10000)
# 点击加群
#m.click(493, 1008)
#time.sleep(3)
# 点击要选的群
# m.click(1076, 471)
#m.click(1063, 423)
# 点击确定
#m.click(703, 806)
#time.sleep(3)
# 点击提交
m.click(939, 1105)

# k.type_string('hello')
