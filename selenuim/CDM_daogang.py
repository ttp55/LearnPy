# @time:  2019/8/12 15:30
# @author: WZG
# encoding: utf-8
from selenuim import PyTest_main
import random
import datetime

url_url = 'http://192.168.210.108:8080/page/#/arrivalHome'
liukong_name = 'WTest' + str(random.randrange(0, 100))
fly_fangx = 'ELKAL;P127:SUBUL'


def fabu_airport():
    time_now = datetime.datetime.now()
    d.element(fangfa='xpath', dingwei='/html/body/div/section/div/div[1]/div/div/button').click()
    # d.driver.switch_to.frame(0)
    d.element(fangfa='id', dingwei='planName').send_keys(liukong_name)
    d.element(fangfa='class', dingwei='ant-radio-input').click()
    d.element(fangfa='xpath', dingwei='//*[@id="startHour"]').send_keys((time_now.hour + 1) * 100)
    d.element(fangfa='xpath', dingwei='//*[@id="extendHour"]').send_keys(10)
    inp = d.driver.find_elements_by_class_name('pass-ability-input-box')
    for i in inp:
        i.send_keys(66)
    d.element(fangfa='xpath', dingwei='//*[@id="accumulateStartHour"]').send_keys((time_now.hour - 3) * 100)
    d.element(fangfa='id', dingwei='accumulateEndHour').send_keys((time_now.hour - 1) * 100)
    d.element(fangfa='xpath', dingwei='//*[@id="direction"]').send_keys(fly_fangx)
    d.element(fangfa='xpath', dingwei='/html/body/div[2]/div/div/div[2]/div/form/div[5]/div/div/span/div/div[1]/button').click()
    d.waiting(5)
    all_handles = d.driver.window_handles
    d.driver.switch_to.window(all_handles[1])
    d.element(fangfa='xpath', dingwei='/html/body/div[4]/div/div[2]/div/div[2]/div[3]/div/button[2]').click()


if __name__ == "__main__":
    d = PyTest_main.PyTest(browser='chrome')
    d.make_maxwindow()
    d.open(url=url_url)
    d.waiting(5)
    fabu_airport()
