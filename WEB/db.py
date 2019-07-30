# @time:  2019/7/30 14:51
# @author: WZG
# encoding: utf-8

from 数据库 import my1

sql = 'SELECT user,pass FROM users;'


def con():
    mysqlconn = my1.MySqlConn('my', 'root', 'root')
    mysqlconn.conmysql()

    userpass = mysqlconn.selmysql(sql=sql)
    mysqlconn.closemysql()

    return userpass




