# @Time : 2025/1/23 14:13
# @Author : WZG
# --coding:utf-8--

import time
import random
from pymouse import PyMouse

m = PyMouse()


def new_information(d):
    try:
        d.find_element_by_xpath('//*[@id="div_content"]/div[1]/div/div[1]').click()
    except Exception as e:
        print(f'异常:{e}')
    d.find_element_by_xpath('//*[@id="right-air-p"]').click()  # 点击Current user information
    d.find_element_by_xpath('//*[@id="table_P"]/tr/td[4]/a').click()  # 点击上传文件
    d.find_element_by_xpath('//*[@id="myModal"]/div/div/div[2]/div/div[3]/div[2]/div').click()  # 点击选择文件
    time.sleep(1)
    m.click(930, 634)
    time.sleep(1)
    m.click(1193, 848)
    time.sleep(1)
    try:

        d.find_element_by_xpath('//*[@id="myModal"]/div/div/div[2]/div/div[3]/div[2]/a').click()  # 点击upload
        d.find_element_by_xpath('/html/body/div[12]/div/div/div[2]/button').click()  # 点击确定
    except:
        pass

    d.find_element_by_xpath('//*[@id="right-air-l"]').click()  # 点击 Legal person information
    d.find_element_by_xpath('//*[@id="table_L"]/tr/td[4]/a').click()  # 点击上传文件
    d.find_element_by_xpath('//*[@id="myModal"]/div/div/div[2]/div/div[3]/div[2]/div').click()  # 点击选择文件
    time.sleep(1)
    m.click(930, 634)
    time.sleep(1)
    m.click(1193, 848)
    time.sleep(1)
    try:

        d.find_element_by_xpath('//*[@id="myModal"]/div/div/div[2]/div/div[3]/div[2]/a').click()  # 点击upload
        d.find_element_by_xpath('/html/body/div[12]/div/div/div[2]/button').click()  # 点击确定
    except:
        pass

    d.find_element_by_xpath('//*[@id="right-air-c"]').click()  # 点击 Company Introduction
    d.find_element_by_xpath('//*[@id="table_C"]/tr[1]/td[4]/a').click()  # 点击上传文件
    d.find_element_by_xpath('//*[@id="myModal"]/div/div/div[2]/div/div[3]/div[2]/div').click()  # 点击选择文件
    time.sleep(1)
    m.click(930, 634)
    time.sleep(1)
    m.click(1193, 848)
    time.sleep(1)
    try:

        d.find_element_by_xpath('//*[@id="myModal"]/div/div/div[2]/div/div[3]/div[2]/a').click()  # 点击upload
        d.find_element_by_xpath('/html/body/div[12]/div/div/div[2]/button').click()  # 点击确定
    except:
        pass

    d.find_element_by_xpath('//*[@id="right-air-a-new"]').click()  # 点击  Aircraft information
    d.find_element_by_xpath('//*[@id="tb_aircraft"]/tbody/tr[4]/td[8]/div/a[1]').click()
    d.find_element_by_xpath('//*[@id="table_A"]/tr[1]/td[4]/a').click()  # 点击上传文件
    d.find_element_by_xpath('//*[@id="myModal"]/div/div/div[2]/div/div[3]/div[2]/div').click()  # 点击选择文件
    time.sleep(1)
    m.click(930, 634)
    time.sleep(1)
    m.click(1193, 848)
    time.sleep(1)
    try:

        d.find_element_by_xpath('//*[@id="myModal"]/div/div/div[2]/div/div[3]/div[2]/a').click()  # 点击upload
        d.find_element_by_xpath('/html/body/div[12]/div/div/div[2]/button').click()  # 点击确定
    except:
        pass

    d.find_element_by_xpath('//*[@id="btn_confirm"]').click()  # 点击一键确认
    d.find_element_by_xpath('/html/body/div[12]/div/div/div[2]/button').click()
    d.find_element_by_xpath('//*[@id="sbld"]').click()  # 点击logout

