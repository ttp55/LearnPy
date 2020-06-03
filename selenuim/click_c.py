# @Time : 2019/12/26 9:50
# @Author : WZG
# --coding:utf-8--

from selenuim import PyTest_main
import re

url_url = 'http://yx.h5uc.com/kanniyouduose/'


def click_yanse():

    d.element(fangfa='xpath', dingwei='//*[@id="index"]/div[2]/button').click()
    while True:
        l1 = []
        yan = d.driver.find_elements_by_xpath('//*[@id="box"]/span')
        for i in yan:
            l2 = sum(map(int, re.findall(r'\d+', i.get_attribute('style'))))
            l1.append(l2)

        s1 = list(set(l1))
        if l1.count(s1[0]) == 1:
            x = l1.index(s1[0]) + 1
            d.element(fangfa='xpath', dingwei='//*[@id="box"]/span[%s]' % x).click()
        else:
            x = l1.index(s1[1]) + 1
            d.element(fangfa='xpath', dingwei='//*[@id="box"]/span[%s]' % x).click()


if __name__ == "__main__":
    d = PyTest_main.PyTest(browser='chrome')
    d.make_maxwindow()
    d.open(url=url_url)
    d.waiting(60)
    click_yanse()
