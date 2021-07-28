# @Time : 2021/7/15 14:01
# @Author : WZG
# --coding:utf-8--
import time
from pymouse import PyMouse
from pykeyboard import PyKeyboard

m = PyMouse()
k = PyKeyboard()
a = m.position()

print(a)


time.sleep(1)

m.click(463, 1175)
time.sleep(1)
m.click(680, 1044)
time.sleep(1)
m.click(256, 258)
time.sleep(1)
m.click(233, 359)
time.sleep(1)
m.click(456, 915)
time.sleep(1)
k.press_key(k.enter_key)
k.release_key(k.enter_key)
time.sleep(1)
k.press_key(k.enter_key)
k.release_key(k.enter_key)
time.sleep(1)
m.click(1202, 951)
time.sleep(2)
k.press_key(k.enter_key)
k.release_key(k.enter_key)


time.sleep(1)
m.click(1993, 95)
time.sleep(1)
m.click(2173, 421)
time.sleep(1)
m.click(2214, 468)
k.press_key(k.delete_key)
k.press_key(k.numpad_keys[1])
k.release_key(k.numpad_keys[1])
time.sleep(1)
m.click(2249, 421)
time.sleep(1)
m.click(2062, 96)
time.sleep(1)

m.click(23, 178)
time.sleep(20)
m.click(29, 294)
time.sleep(1)
m.click(77, 799)
time.sleep(1)
m.click(392, 795)
time.sleep(1)
k.press_key(k.enter_key)
k.release_key(k.enter_key)
time.sleep(1)
k.press_key(k.enter_key)
k.release_key(k.enter_key)