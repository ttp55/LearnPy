# @Time : 2019/5/16 15:23
# @Author : WZG
# --coding:utf-8--

#将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。


list1 = []
num = int(input('请输入：'))

for i in range(2, num):
    while True:
        if num % i == 0:
            list1.append(i)
            num = num / i
        else:
            break
print(list1)
