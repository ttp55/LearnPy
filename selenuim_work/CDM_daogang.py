# @time:  2019/8/12 15:30
# @author: WZG
# encoding: utf-8
from selenuim_work import PyTest_main
import random
import datetime
import time

url_url = 'http://192.168.210.108:8080/page/#/arrivalHome'
liukong_name = 'WTest' + str(random.randrange(0, 1000))
fly_fangx = 'IDEPO;ELKAL;LAGEX;P293;P480;LINSO;SAGAG;KATBO;MEPAN;OMBON;SUBUL;AGULU;DCH;RG;SANLI;P11;P239;OKTUV;' \
            'LOTMO;P124;P233;P127;P438;P40;HUY;TRN'
time_now = datetime.datetime.now()
hour_now = time_now.hour
be = random.randrange(0, 8)
air = random.randrange(0, 4)
exemption_fly = 'CSC8529;CSH9451;N899CH'
exemption_fly1 = 'CSN3443;CSC8870;CSN3453'

air_port = ['ZUUU', 'ZUGY', 'ZUCK', 'ZPPP']
limit_d = ['天气', '军事活动', '航班时刻', '流量', '机场', '重大保障活动', '空管', '其他']
list_l = []


def fab_airport(hour_n):
    air_p = d.driver.find_elements_by_css_selector("[class='ant-btn c-btn c-btn-blue publish-btn']")
    air_p[air].click()
    d.element(fangfa='id', dingwei='planName').send_keys(air_port[air] + '-' + liukong_name + '限制' + '-' + limit_d[be])
    bec = d.driver.find_elements_by_class_name('ant-radio-input')
    bec[be].click()
    if (hour_n + 1) / 10 < 1:
        hour_now1 = '0' + str(hour_n) + '00'
    else:
        hour_now1 = (hour_n + 1) * 100
    d.element(fangfa='xpath', dingwei='//*[@id="startHour"]').send_keys(hour_now1)
    d.element(fangfa='xpath', dingwei='//*[@id="extendHour"]').send_keys(10)
    inp = d.driver.find_elements_by_class_name('pass-ability-input-box')
    for i in inp:
        j = random.randrange(1, 99)
        list_l.append(j)
        i.send_keys(j)
    if (hour_n - 3) / 10 < 1:
        hour_now1 = '0' + str(hour_n - 3) + '00'
    else:
        hour_now1 = (hour_n - 3) * 100
    d.element(fangfa='xpath', dingwei='//*[@id="accumulateStartHour"]').send_keys(hour_now1)
    if (hour_n - 1) / 10 < 1:
        hour_now1 = '0' + str(hour_n - 1) + '00'
    else:
        hour_now1 = (hour_n - 1) * 100
    d.element(fangfa='id', dingwei='accumulateEndHour').send_keys(hour_now1)
    d.element(fangfa='xpath', dingwei='//*[@id="direction"]').send_keys(fly_fangx)
    js = "window.scrollTo(100, 450)"
    d.driver.execute_script(js)
    d.element(fangfa='xpath', dingwei='//*[@id="exemptFlight"]').send_keys(exemption_fly1)
    d.element(fangfa='xpath', dingwei='//*[@id="gdpExemptFlight"]').send_keys(exemption_fly)
    d.element(fangfa='xpath', dingwei='/html/body/div[2]/div/div/div[2]/div/form/div[6]/div/div/span/div/div[1]/button').click()
    all_handles = d.driver.window_handles
    d.driver.switch_to.window(all_handles[0])
    time.sleep(1)
    d.element(fangfa='xpath', dingwei='/html/body/div[3]/div/div[2]/div/div[2]/div[3]/div/button[2]').click()
    time.sleep(3)
    all_handles = d.driver.window_handles
    d.driver.switch_to.window(all_handles[1])
    time.sleep(5)
    # d.driver.get_screenshot_as_file('C:\\Users\\lenovo\\Desktop\\jie\\error1.jpg')
    new_tab = d.element(fangfa='xpath', dingwei='//*[@id="total-modal"]/div[3]/button[3]')
    new_tab.click()
    all_handles = d.driver.window_handles
    d.driver.switch_to.window(all_handles[1])
    time.sleep(2)
    d.element(fangfa='xpath', dingwei='/html/body/div[2]/div/div[2]/div/div[2]/div[3]/div/button[2]').click()
    # d.driver.quit()
    print(list_l)


if __name__ == "__main__":
    d = PyTest_main.PyTest(browser='chrome')
    d.make_maxwindow()
    d.open(url=url_url)
    d.waiting(60)
    fab_airport(hour_now)

