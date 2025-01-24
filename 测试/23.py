# @Time : 2024/12/27 15:44
# @Author : WZG
# --coding:utf-8--
from pymouse import PyMouse
from pykeyboard import PyKeyboard
import time
m = PyMouse()
k = PyKeyboard
a = m.position()
print(a)
m.click(930, 634)
time.sleep(1)
m.click(1193, 848)
time.sleep(1)

#m.click(1328, 361,1,1)
