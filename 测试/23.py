# @Time : 2024/12/27 15:44
# @Author : WZG
# --coding:utf-8--
from pymouse import PyMouse
from pykeyboard import PyKeyboard
import time
mouth = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
now = time.strftime("%d%m%Y", time.localtime())

m = int(now[2:4])-1
d = now[0:2]
y = now[6:]
date_now = d + mouth[m] + y
print(date_now)


'''
m = PyMouse()
k = PyKeyboard
a = m.position()
print(a)
m.click(930, 634)
time.sleep(1)
m.click(1193, 848)
time.sleep(1)

#m.click(1328, 361,1,1)
'''