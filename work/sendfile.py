# @Time : 2023/4/13 14:08
# @Author : WZG
# --coding:utf-8--
import autoit
import time
import os
import pyautogui
import pyperclip
from pymouse import PyMouse
from pykeyboard import PyKeyboard

pathxml = 'D:/xmlxml/Fs20230410'

pathxmllist = os.listdir(pathxml)

#print(pathxmllist)

for i in pathxmllist[50:150]:

    with open('D:/xmlxml/Fs20230410/' + i, 'r', encoding='utf-8') as f:
        fxml = f.read()
    #print(fxml)

    pyperclip.copy(fxml)

    m = PyMouse()
    k = PyKeyboard()
    a = m.position()


#send to
    m.move(1328, 594)
    time.sleep(1)
    m.click(1328, 594)
    time.sleep(1)

#message
    m.move(511, 787)
    time.sleep(1)
    m.click(511, 787)
    time.sleep(1)

    pyautogui.hotkey('ctrl', 'a')

    pyautogui.hotkey('ctrl', 'v')

#send
    m.move(448, 634)
    time.sleep(1)
    m.click(448, 634)
    time.sleep(1)

    print(i)
