# @Time : 2021/2/9 13:29
# @Author : WZG
# --coding:utf-8--

from selenuim import PyTest_main
import time

url_url = 'https://www.bjjnts.cn/lessonStudy/69/2501'


def learn():
    d.element(fangfa='xpath', dingwei='/html/body/div[1]/div/div[2]/a[1]').click()
    d.element(fangfa='xpath', dingwei='//*[@id="formLogin"]/div[2]/input').send_keys('15210956091')
    d.element(fangfa='xpath', dingwei='//*[@id="formLogin"]/div[3]/input').send_keys('666359888Bmw')
    d.element(fangfa='xpath', dingwei='//*[@id="formLogin"]/button').click()
    time.sleep(30)

    for i in range(1, 27):
        d.element(fangfa='xpath', dingwei='/html/body/div[3]/div/div/div/div[1]/div[2]/ul/li['+str(i)+']/div/a/div').click()
        playtime = d.element(fangfa='xpath', dingwei='/html/body/div[3]/div/div/div/div[1]/div[2]/ul/li['+str(i)+']/div/a/div/p').text
        print(playtime)
        playtime = int(playtime[4:6])*60 + int(playtime[7:9])
        time.sleep(playtime+10)


if __name__ == "__main__":
    d = PyTest_main.PyTest(browser='chrome')
    d.make_maxwindow()
    d.open(url=url_url)
    d.waiting(60)
    learn()
