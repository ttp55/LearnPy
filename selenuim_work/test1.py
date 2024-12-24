#@time:  2019/7/3 14:06
#@author: WZG
# encoding: utf-8

from selenium import webdriver
import time

dirver = webdriver.Chrome()
dirver.get('http://192.168.243.69:18084/airportcdm/')

e = dirver.find_element_by_id('logon_username')
e.send_keys('zlxydev')
e = dirver.find_element_by_id('logon_password')
e.send_keys('82325o5o')
e = dirver.find_element_by_class_name('logon_form_button')
e.click()
dirver.implicitly_wait(5)
liu = dirver.find_element_by_link_text('流控信息')
liu.find_element_by_xpath('/html/body/div[1]/nav/div[2]/ul[2]/li[5]/ul/li[1]/a').click()

