# @Time : 2024/12/23 13:32
# @Author : WZG
# --coding:utf-8--
import time
import re
print(time.strftime('%Y%m%d%H%M%S', time.localtime()))

l = '{"status":-2,"ErrName":"验证码","attr":"verification code"}'


login_value = re.findall(r'-2',l)
int(login_value[0])
print(login_value[0])
print(type(login_value[0]))