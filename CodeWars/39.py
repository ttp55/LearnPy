# @Time : 2019/9/4 9:01
# @Author : WZG
# --coding:utf-8--

from pymouse import PyMouse
from pykeyboard import PyKeyboard
import time

k = PyKeyboard()
m = PyMouse()
a = m.position()
print(a)
time.sleep(5)
k.press_key(k.enter_key)
