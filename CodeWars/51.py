# @Time : 2019/10/25 9:28
# @Author : WZG
# --coding:utf-8--
from types import MethodType


class Thing (object):
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex
    def name(self):
        return self.name()
    is_a = is_a(True)

class is_a(Thing):
    pass


jane = Thing('Jane')
print(jane.name)

