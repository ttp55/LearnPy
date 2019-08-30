# @Time : 2019/8/30 9:06
# @Author : WZG
# --coding:utf-8--


class PaginationHelper:

    def __init__(self, collection, items_per_page):
        self.list_l = []
        for i in collection:


        for collection[: items_per_page] in collection:
            self.list_l += collection[:items_per_page]
        self.it = items_per_page
        self.co = collection

    def item_count(self):
        return self.co.count()

    def page_count(self):
        return self.list_l.count()

    def page_item_count(self, page_index):
        try:
            return self.list_l[page_index].count()
        except:
            return -1

    def page_index(self, item_index):
        try:
            return self.list_l.index(self.co[item_index])
        except:
            return -1


coll = range(25)
helper = PaginationHelper(coll, 4)
print(helper.item_count())
