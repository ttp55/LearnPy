# @Time : 2019/12/13 16:38
# @Author : WZG
# --coding:utf-8--

import time
import pymouse


m = pymouse.PyMouse()
a = m.position()
print(a)

for i in range(200):
    m.click(1168, 581)
    time.sleep(1)
    m.click(1159, 606)
    time.sleep(1)
    m.click(1080, 716)
    time.sleep(2)

