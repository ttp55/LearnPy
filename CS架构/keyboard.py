# @Time : 2021/7/15 16:06
# @Author : WZG
# --coding:utf-8--
from pykeyboard import PyKeyboard
import time
from pymouse import PyMouse

m = PyMouse()
k = PyKeyboard()
a = m.position()
print(a)

m.click(1993, 95)
time.sleep(2)
m.click(2173, 421)
time.sleep(2)
m.click(2214, 468)
k.press_key(k.delete_key)
k.press_key(k.numpad_keys[1])
k.release_key(k.numpad_keys[1])