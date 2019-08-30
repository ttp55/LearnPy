# @Time : 2019/8/30 9:06
# @Author : WZG
# --coding:utf-8--


class PaginationHelper:

    def __init__(self, collection, items_per_page):
        self.list_l1 = list(collection)
        self.list_l2 = [self.list_l1[x : x + items_per_page] for x in range(0, len(self.list_l1), items_per_page)]

    def item_count(self):
        return len(self.list_l1)

    def page_count(self):
        return len(self.list_l2)

    def page_item_count(self, page_index):
        try:
            return len(self.list_l2[page_index])
        except:
            return -1

    def page_index(self, item_index):
        try:
            r = map(lambda i: item_index + 1 in i, self.list_l2)
            return list(r).index(True)
        except:
            return -1


coll = range(1, 25)
helper = PaginationHelper(coll, 10)
#print(helper.item_count())
print(helper.page_index(0))
#print(helper.page_item_count(2))
#print(helper.page_count())
