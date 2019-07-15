# @time:  2019/7/11 9:48
# @author: WZG
# encoding: utf-8

from selenuim import pytest
import time
import re


url_url = 'http://192.168.211.70:8082/main'

if __name__ == '__main__':
    d = pytest.PyTest(browser='chrome')
    d.make_maxwindow()
    d.open(url=url_url)
    d.send_key(fangfa='xpath', dingwei='//*[@id="app"]/div/div/div[3]/div/input', text='admin')
    d.send_key(fangfa='xpath', dingwei='//*[@id="app"]/div/div/div[5]/div/input', text='admin')
    d.element(fangfa='xpath', dingwei='//*[@id="app"]/div/div/div[7]/button').click()
    time.sleep(5)
    d.element(fangfa='xpath', dingwei='/html/body/div[4]/div[1]/div/div[1]/span/img').click()
    d.waiting(10)
    # d.element(fangfa='link_text', dingwei='报文查询').click()
    # d.element(fangfa='xpath', dingwei='//*[@id="dropdown-menu-7102"]/li[1]').click()
    d.element(fangfa='xpath', dingwei='//*[@id="canvasContainerView"]/div[1]/div/div[2]/div[2]/div/div/div[1]/div[9]/button[1]').click()


