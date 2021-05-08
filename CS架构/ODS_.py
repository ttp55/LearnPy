# @Time : 2020/10/13 14:20
# @Author : WZG
# --coding:utf-8--
import autoit
import time

ODS_path = "D:\ODS\Debug\ODS.exe"

autoit.run(ODS_path)
time.sleep(3)

autoit.send("admin")
time.sleep(1)

autoit.send("{ENTER}")
time.sleep(5)