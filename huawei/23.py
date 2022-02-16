# @Time : 2022/2/16 14:31
# @Author : WZG
# --coding:utf-8--

# 函数独占时间

class Solution:
    def exclusiveTime(n, logs):
        stack = []
        gotime = [0]*n
        pre = 0
        for i in logs:
            lis = i.split(':')
            if lis[1] == 'start':
                if stack:
                    gotime[stack[-1]] += int(lis[2]) - pre
                stack.append(int(lis[0]))
                pre = int(lis[2])
            else:
                gotime[stack.pop()] += (int(lis[2]) - pre + 1)
                pre = int(lis[2]) + 1

        print(gotime)









Solution.exclusiveTime(n = 2, logs = ["0:start:0","1:start:2","1:end:5","0:end:6"])