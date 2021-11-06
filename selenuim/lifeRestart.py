# @Time : 2021/9/18 11:10
# @Author : WZG
# --coding:utf-8--
from selenuim import PyTest_main

url_url = 'http://liferestart.syaro.io/view/?continueFlag=cc4aedc355f9e8a0af4ca55dbf4dfea4'


def LifeRe():
    d.element(fangfa='id', dingwei='restart').click()
    d.element(fangfa='id', dingwei='random').click()
    for i in range(1, 11):
        a = d.element(fangfa='xpath', dingwei='//*[@id="talents"]/li['+str(i)+']').text
        print(a)
        if '小盒子' in a:
            return
    d.refresh_()
    LifeRe()


if __name__ == "__main__":
    d = PyTest_main.PyTest(browser='chrome')
    d.make_maxwindow()
    d.open(url=url_url)
    d.waiting(60)
    LifeRe()
