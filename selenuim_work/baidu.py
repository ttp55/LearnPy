# @time:  2019/7/5 9:58
# @author: WZG
# encoding: utf-8

from selenuim_work import PyTest_main


if __name__ == '__main__':
    d = PyTest_main.PyTest(browser='chrome')
    d.make_maxwindow()
    d.open(url='http://www.baidu.com')
    d.element(fangfa='id', dingwei='kw').send_keys('地图')
    d.element(fangfa='id', dingwei='su').click()
    d.waiting(10)
    d.element(fangfa='xpath', dingwei='//*[@id="1"]/h3/a[1]').click()
    d.waiting(30)
    d.element(fangfa='xpath', dingwei='//*[@id="ui3_city_change"]/a/span').click()
    d.waiting(10)
    d.element(fangfa='xpath', dingwei='//*[@id="selCityHotCityId"]/a[7]').click()
    #d.element(fangfa='class', dingwei='avatar-abstract').click()
    #d.element(fangfa='xpath', dingwei='//*[@id="user-center"]/div[2]/div[2]/div[4]/ul/li[2]/a/span').click()
    #d.element(fangfa='name', dingwei='天津').click()
    #d.cli_text('北京市')
    #d.cli_text('天津')
