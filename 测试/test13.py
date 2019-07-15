# @Time : 2019/5/21 10:03
# @Author : WZG
# --coding:utf-8--


def ye(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print('闰年！')
    else:
        print('平年！')


ye(4000)
