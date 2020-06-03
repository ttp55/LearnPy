# @Time : 2019/12/3 9:43
# @Author : WZG
# --coding:utf-8--
# 拆分报文
import time
from pymouse import PyMouse
from pykeyboard import PyKeyboard

k = PyKeyboard()
m = PyMouse()
a = m.position()
print(a)
x = 322
for i in range(1, 1000):
    m.click(2030, x)
    x += 25
    if x >= 591:
        x = 322
    if 11 % i == 0:
        for y in range(11):
            m.click(2544, 595)
    time.sleep(2)
    m.click(2022, 638)
    time.sleep(1)
    m.click(2876, 679)
    time.sleep(2)
    m.click(2899, 670)
    time.sleep(1)
    m.click(3214, 972)
    time.sleep(1)
