# @Time : 2019/5/24 10:23
# @Author : WZG
# --coding:utf-8--
import mysql.connector
import re


class MySqlConn(object):
    def __init__(self, db, user, password):
        self.host = 'localhost'
        self.db = db
        self.user = user
        self.password = password
        self.port = 3306

    def conmysql(self):
        try:
            self.conn = mysql.connector.connect(user=self.user, password=self.password, database=self.db)
            self.cursor = self.conn.cursor()
        except Exception as e:
            print(e)

    def createmyslq(self, sql):
        try:
            self.cursor.execute(sql)
        except Exception as e:
            print(e)

    def selmysql(self, sql):
        try:
            self.cursor.execute(sql)
            row = self.cursor.fetchall()
            print(row)
        except Exception as e:
            print(e)

    def insertmysql(self, sql):
        try:
            self.cursor.execute(sql)
        except Exception as e:
            print(e)
        else:
            self.conn.commit()

    def del_updatesql(self, sql):
        try:
            self.cursor.execute(sql)
        except Exception as e:
            self.conn.rollback()
            print(e)
        else:
            self.conn.commit()

    def qumyslq(self, sql):
        try:
            self.cursor.execute(sql)
        except Exception as e:
            print(e)

    def closemysql(self):
        self.conn.close()
        self.cursor.close()


def readsql():
    with open('E:/sql/sql.txt', 'r') as f:
        sql_list = f.read().split(';')[:-1]  # sql文件最后一行加上;
        sql_list = [x.replace('\n', '') if '\n' in x else x for x in sql_list]  # 将每段sql里的换行符改成空格
    for sql_item in sql_list:
        if re.match(r'[C|c\_][0-9a-zA-Z\_]*', sql_item):
            mysqlconn.createmyslq(sql_item)
        elif re.match(r'[D|d|U|u\_][0-9a-zA-Z\_]*', sql_item):
            mysqlconn.del_updatesql(sql_item)
        elif re.match(r'[S|s\_][0-9a-zA-Z\_]*', sql_item):
            mysqlconn.selmysql(sql_item)
        elif re.match(r'[I|i\_][0-9a-zA-Z\_]*', sql_item):
            mysqlconn.insertmysql(sql_item)
        else:
            mysqlconn.qumyslq(sql_item)


mysqlconn = MySqlConn('my', 'root', 'root')
mysqlconn.conmysql()
#mysqlconn.selmysql("SELECT * FROM user1")
readsql()
#mysqlconn.insertmysql("insert into user1 value (3, 'wanghong')")
#mysqlconn.selmysql("SELECT * FROM user1")
#mysqlconn.del_updatesql("DELETE FROM user1 WHERE id = 3")
#mysqlconn.selmysql("SELECT * FROM user1")
#mysqlconn.selmysql('SHOW TABLES')
mysqlconn.closemysql()


