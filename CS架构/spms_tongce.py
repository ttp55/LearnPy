# @Time : 2020/11/27 10:22
# @Author : WZG
# --coding:utf-8--
import autoit
import time
from pymouse import PyMouse
from tkinter import messagebox
from pykeyboard import PyKeyboard


spmspath = "D:\SSSSSSSSPMS\Debug\SPMS.exe"
spmspath1 = "D:\SSSSSSSSPMS\SPMS改字段新数据库\SPMS.exe"

autoit.run(spmspath)
m = PyMouse()
k = PyKeyboard()
a = m.position()
print(a)

time.sleep(10)


def jks_login():
    autoit.send("{TAB}")
    autoit.send('jks')
    autoit.send("{DELETE 5}")
    time.sleep(1)
    autoit.send("{ENTER}")


def admin_login():
    autoit.send("{TAB}")
    autoit.send('admin')
    autoit.send("{DELETE 5}")
    time.sleep(1)
    autoit.send("{ENTER}")

    time.sleep(15)
    y3 = 158
    for i in range(4):
        m.move(41, 112)
        time.sleep(1)
        m.click(48, y3)
        time.sleep(5)
        y3 += 49
    
    m.move(171, 108)
    time.sleep(1)
    m.click(176, 152)
    time.sleep(1)
    m.click(341, 152)
    time.sleep(5)
    
    m.move(171, 108)
    time.sleep(1)
    m.click(176, 152)
    time.sleep(1)
    m.click(336, 188)
    time.sleep(5)

    m.click(171, 108)
    time.sleep(1)
    m.click(194, 203)
    time.sleep(1)
    m.click(311, 206)
    time.sleep(5)

    m.move(171, 108)
    time.sleep(1)
    m.click(194, 203)
    time.sleep(1)
    m.click(311, 253)
    time.sleep(5)
    
    m.move(171, 108)
    time.sleep(1)
    m.click(188, 255)
    time.sleep(5)

    y = 209
    for i in range(13):
        m.move(391, 107)
        time.sleep(1)
        m.click(400, y)
        time.sleep(5)
        if i == 2:
            m.click(1592, 138)
        if i == 3:
            m.click(1677, 258)
        y += 49
        
    y1 = 150
    for i in range(4):
        m.move(512, 109)
        time.sleep(1)
        m.click(525, 156)
        time.sleep(1)
        m.click(690, y1)
        time.sleep(5)
        y1 += 49
        
    y2 = 187
    for i in range(13):
        m.move(512, 109)
        time.sleep(1)
        m.click(518, y2)
        time.sleep(5)
        y2 += 49
        
    messagebox.showinfo("提示", "测试完成~")
    time.sleep(2)


# jks_login()


admin_login()

k.press_key(k.enter_key)