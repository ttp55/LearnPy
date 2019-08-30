# @Time : 2019/8/30 9:06
# @Author : WZG
# --coding:utf-8--
import math


class PaginationHelper:

    def __init__(self, collection, items_per_page):
        self.i = 0
        self.list_l = []
        self.list_l1 = list(collection)
        self.list_l2 = list(collection)
        while self.i < math.ceil(len(self.list_l2)/items_per_page):
            self.list_l.append(list(self.list_l1[:items_per_page]))
            self.list_l1 = self.list_l1[items_per_page:]
            self.i += 1

    def item_count(self):
        return len(self.list_l2)

    def page_count(self):
        return len(self.list_l)

    def page_item_count(self, page_index):
        try:
            return len(self.list_l[page_index])
        except:
            return -1

    def page_index(self, item_index):
        try:
            r = map(lambda i: item_index in i, self.list_l)
            return list(r).index(True)
        except:
            return -1


coll = range(1, 25)
helper = PaginationHelper(coll, 10)
print(helper.item_count())
print(helper.page_index(5))
print(helper.page_item_count(2))
print(helper.page_count())
