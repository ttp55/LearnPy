# @Time : 2021/4/16 9:22
# @Author : WZG
# --coding:utf-8--


class Stack(object):
    def __init__(self, limit):
        self.stack = []
        self.limit = limit

    def push(self, data):
        if len(self.stack) >= self.limit:
            print('StackOverflowError')
        else:
            self.stack.append(data)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            raise IndexError('pop from an empty stack')

    def peek(self):
        if self.stack:
            return self.stack[-1]

    def is_empty(self):
        return not bool(self.stack)

    def size(self):
        return len(self.stack)


<<<<<<< Updated upstream
s = Stack(10)
=======
s = Stack(0)
>>>>>>> Stashed changes
s.push(1)
s.push(2)
print(s.peek())
print(s.size())
<<<<<<< Updated upstream
print(s.stack)
=======
>>>>>>> Stashed changes
