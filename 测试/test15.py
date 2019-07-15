# @Time : 2019/5/21 10:47
# @Author : WZG
# --coding:utf-8--
#与7相关的数：如果一个正整数，它能被7整除或者它的十进制表示法中某个位数上的数字为7，则称之为与7相关的数。（10分）
#题目内容：
#现在我们给定一个正整数n（n<1000），求所有小于等于n的与7无关的正整数的平方和。


def sev(a):
    b = list(range(1, a + 1))
    for i in range(1, a + 1):
        if (i % 7 == 0) or ('7' in str(i)):
            b.remove(i)
    c = map(lambda x: x ** 2, b)
    print(b)
    print(sum(list(c)))


sev(50)
