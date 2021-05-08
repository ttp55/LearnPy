# @Time : 2020/10/13 15:18
# @Author : WZG
# --coding:utf-8--
import autoit
import time

spmspath = "D:\SSSSSSSSPMS\Debug\SPMS.exe"
spmspath1 = "D:\SSSSSSSSPMS\SPMS改字段新数据库\SPMS.exe"

<<<<<<< Updated upstream

def jks_login():
    autoit.run(spmspath)

    time.sleep(3)
=======
autoit.run(spmspath)

time.sleep(3)


def jks_login():
>>>>>>> Stashed changes
    autoit.send("{TAB}")    
    autoit.send('jks')
    autoit.send("{DELETE 5}")
    time.sleep(1)
    autoit.send("{ENTER}")


def admin_login():
<<<<<<< Updated upstream
    autoit.run(spmspath)

    time.sleep(3)

=======
>>>>>>> Stashed changes
    autoit.send("{TAB}")
    autoit.send('admin')
    autoit.send("{DELETE 5}")
    time.sleep(1)
    autoit.send("{ENTER}")


<<<<<<< Updated upstream
jks_login()
admin_login()

=======
# jks_login()
admin_login()


>>>>>>> Stashed changes
