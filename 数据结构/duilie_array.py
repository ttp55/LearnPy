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


def josefhes(P_list, m):
    q = Queue()
    for people in P_list:
        q.enqueue(people)

    while q.size() > 1:
        for i in range(m-1):
            q.enqueue(q.dequeue())
            print(q.entries)
        q.dequeue()
    return q.dequeue()


P_list = [1, 2, 3, 4]
print(josefhes(P_list, 3))

