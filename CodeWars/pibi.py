# @Time : 2019/9/4 9:01
# @Author : WZG
# --coding:utf-8--

import time
from pymouse import PyMouse
#from pykeyboard import PyKeyboard

#k = PyKeyboard()
m = PyMouse()
a = m.position()
print(a)
time.sleep(74000)
m.click(1052, 329)
m.click(1052, 329)
while True:

    time.sleep(86401)
    m.click(1052, 329)
    m.click(1052, 329)

# k.type_string('hello')
