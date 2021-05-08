# @Time : 2020/9/18 9:44
# @Author : WZG
# --coding:utf-8--
import easygui
import re
from 数据库 import my1

mysql_C = my1.MySqlConn('my', 'root', 'root')
#取口味
Taste = mysql_C.selmysql('select Taste from sweetice')
Taste = re.findall(r'[\u4e00-\u9fa5]+', str(Taste))
#取尺寸
size = mysql_C.selmysql('select size_ from size')
size = re.findall(r'\d+', str(size))
favor = easygui.buttonbox('请选择口味：',
                          choices=Taste)
like = easygui.buttonbox(favor+'多大尺寸', choices=size)

easygui.msgbox('您选择'+' '+like+'号的'+favor+'冰激凌')
print('您选择'+' '+like+'号的'+favor+'冰激凌')
a = str(like)
money = mysql_C.selmysql("select money from size where size_=%s" %a)
money = re.findall(r'\d+', str(money))
easygui.msgbox('您此次消费'+money[0]+'元')
print('您此次消费'+money[0]+'元')
