# @Time : 2019/5/14 10:56
# @Author : WZG
# --coding:utf-8--


class student(object):
    count = 0
    name = 'Mic'

    def __init__(self, name):
        self.name = name
        student.count += 1


s = student('Tom')
print(s.count, s.name)
s.name = 'Rose'
print(s.count, s.name)
print(student.name)
del s.name
print(s.name)
t = student('wang')
print(t.count, t.name)
print(s.count, s.name)
