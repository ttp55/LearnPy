# @Time : 2024/12/27 15:44
# @Author : WZG
# --coding:utf-8--
from pymouse import PyMouse
from pykeyboard import PyKeyboard
m = PyMouse
k = PyKeyboard
a = m.position(1)
print(a)
m.move(1328, 361)

m.click(1328, 361,1,1)
