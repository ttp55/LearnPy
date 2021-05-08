# @Time : 2021/4/19 15:07
# @Author : WZG
# --coding:utf-8--


class sort_1():
    def __init__(self):
        self.l = [32,4,2,52,632,7634,324,76,63,4,6453,23,532,724,762,4898]

    def buuble_sort(self):
        for i in range(len(self.l)):
            for j in range(len(self.l)-1-i):
                if self.l[j] > self.l[j+1]:
                    self.l[j], self.l[j+1] = self.l[j+1], self.l[j]

        return self.l


S = sort_1()
print(S.buuble_sort())



