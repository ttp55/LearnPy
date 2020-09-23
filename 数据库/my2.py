# @Time : 2019/5/23 10:33
# @Author : WZG
# --coding:utf-8--

import pymysql
import re
'''
conn = pymysql.connect(user='root', password='root', database='my')
cursor = conn.cursor()

cursor.execute('create table user1 (id varchar(20) primary key , name varchar (20))')
cursor.execute('insert into user1 (id, name) value (%s, %s)', ['1', 'Tom'])

conn.commit()
cursor.close()
'''


class MySqlCommand(object):
    def __init__(self, db, table):
        self.host = 'localhost'
        self.port = 3306
        self.user = 'root'
        self.password = 'root'
        self.db = db
        self.table = table
        try:
            self.conn = pymysql.connect(host=self.host, port=self.port, user=self.user,
                                        password=self.password, db=self.db)

            self.cursor = self.conn.cursor()
        except StopIteration:
            print('connect mysql error')

#创建表
    def createmysql(self, sql):
        try:
            self.cursor.execute(sql)
        except StopIteration:
            print('createtable failed')

#数据库查询
    def selmysql(self, sql):
        try:
            self.cursor.execute(sql)
            row = self.cursor.fetchall()
            print(list(row))
        except StopIteration:
            print(sql + ' execute failed')

#插入数据
    def insertmysql(self, sql):
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except StopIteration:
            print('insert error')

#删除、更新数据
    def del_updatemysql(self, sql):
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except StopIteration:
            self.conn.rollback()

#关闭数据库连接
    def closemysql(self):
        self.conn.close()
        self.cursor.close()


mysqlcommand = MySqlCommand('my', 'sweetice')
mysqlcommand.selmysql('select Taste from sweetice')

