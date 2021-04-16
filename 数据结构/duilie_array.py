# @Time : 2021/4/16 10:00
# @Author : WZG
# --coding:utf-8--


class Queue(object):
    def __init__(self):
        self.entries = []

    def enqueue(self, item):
        self.entries.insert(0, item)

    def dequeue(self):
        return self.entries.pop()

    def isEmpty(self):
        return self.entries == []

    def size(self):
        return len(self.entries)


q = Queue()
q.enqueue(1)
q.enqueue(2)
print(q.size())
print(q.dequeue())
print(q.dequeue())