# @Time : 2024/12/23 13:32
# @Author : WZG
# --coding:utf-8--
import time
from selenuim_work import PyTest_main
from PIL import Image
import pytesseract
import re
import os
import time
from selenuim_work import img_ctrl
import re



for i in (0, 4):
    print(i)
'''

print(time.strftime('%Y%m%d%H%M%S', time.localtime()))

l = '{"status":-2,"ErrName":"验证码","attr":"verification code"}'


login_value = re.findall(r'-2',l)
int(login_value[0])
print(login_value[0])
print(type(login_value[0]))

'''