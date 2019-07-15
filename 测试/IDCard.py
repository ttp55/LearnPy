# @Time : 2019/5/17 8:58
# @Author : WZG
# --coding:utf-8--
import re


class Idcard(object):
    def __init__(self, _card_num):
        self._cardNum = _card_num

    def id_card(self):
        m = 0
        l1 = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
        l3 = [1, 0, 'X', 9, 8, 7, 6, 5, 4, 3, 2]
        if re.match(r'(^\d{18}$)|(^\d{17}(\d|X|x))$', self._cardNum):
            first_l = list(self._cardNum)
            lll = first_l[17]
            if lll.isdigit():
                llll = int(lll)
            else:
                llll = 'X'

            first_l.pop()
            second_l = list(map(int, first_l))
            l2 = list(map(lambda x, y: x * y, second_l, l1))

            for i in l2:
                m += i
            n = m % 11

            def su(o):
                b = ''
                for q in o:
                    b = b + str(q)
                return int(b)
            if llll == l3[n]:
                if second_l[16] % 2 == 0:
                    print('您的生日为：%s-%s-%s，您的姓别：女' % (su(second_l[6:10]), su(second_l[10:12]), su(second_l[12:14])))
                else:
                    print('您的生日为：%s-%s-%s，您的姓别：男' % (su(second_l[6:10]), su(second_l[10:12]), su(second_l[12:14])))
            else:
                print("2请输入正确的身份证号!")
                aaa()
        else:
            print("1请输入正确的身份证号!")
            aaa()


def aaa():
    a = input('请输入身份证号：')
    id = Idcard(a)
    id.id_card()


aaa()

