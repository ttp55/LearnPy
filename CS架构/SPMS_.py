# @Time : 2020/10/13 15:18
# @Author : WZG
# --coding:utf-8--
import autoit
import time
spmspath = "D:\SSSSSSSSPMS\Debug\SPMS.exe"
spmspath1 = "D:\SSSSSSSSPMS\SPMS改字段新数据库\SPMS.exe"

autoit.run(spmspath)

time.sleep(3)


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


# jks_login()
admin_login()


