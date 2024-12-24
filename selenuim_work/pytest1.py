# @time:  2019/7/4 10:55
# @author: WZG
# encoding: utf-8

from selenuim_work import PyTest_main
import time
import re
import urllib3
from bs4 import BeautifulSoup
import requests


def airport_shouxian(t, p1, c1):
    d.element(fangfa='xpath', dingwei='//ul[2]/li[5]/a').click()
    d.waiting(15)
    d.element(fangfa='link_text', dingwei='发布机场受限').click()
    d.waiting(10)
    d.driver.switch_to.frame(0)
    d.waiting(5)
    d.send_key(fangfa='name', dingwei="limit-value", text=t)
    d.element(fangfa='xpath', dingwei=p1).click()
    # d.element(fangfa='xpath', dingwei=p2).click()
    d.element(fangfa='id', dingwei=c1).click()
    d.element(fangfa='id', dingwei='submit-btn').click()
    d.element(fangfa='xpath', dingwei='//*[@id="bootstrap-modal-dialog"]/div/div').click()
    d.element(fangfa='xpath', dingwei='//*[@id="bootstrap-modal-dialog-footer"]/button[1]').click()
    d.waiting(5)
    d.element(fangfa='xpath', dingwei='//*[@id="bootstrap-modal-dialog"]/div/div').click()
    time.sleep(5)
    d.element(fangfa='xpath', dingwei="//div[@id='bootstrap-modal-dialog-footer']/button[2]").click()


def airplan(p, t, t1):
    d.right_click(fangfa='xpath', dingwei=p)
    d.element(fangfa='id', dingwei='open-flight-detail').click()

    tobt_value = d.driver.find_element_by_xpath(t)
    tobt_value.get_attribute('textContent')
    tttt = tobt_value.text
    d.driver.switch_to.frame(0)

    tobt_value1 = d.driver.find_element_by_xpath(t1)
    tobt_value1.get_attribute('textContent')

    tt = re.findall(r'\d{4}', tobt_value1.text)
    ttt = tt[0]
    if int(tttt) == int(ttt):
        print('页面预关时间与航班详情页面TOBT值相等，测试通过！')
    else:
        print('页面预关时间与航班详情页面TOBT值不相等，测试不通过！')

# p: 航路点， c: 限制原因 t:限制时间


p1 = '//*[@id="flowcontrol_edit_form"]/div[4]/div[2]/div[2]/div[2]/div/a[1]/label'
# p2 = '//*[@id="flowcontrol_edit_form"]/div[7]/div[3]/div/div/label[2]'
c1 = 'flowcontrolAutomaticNaming'
t = 11
url_url = 'http://192.168.243.69:18084/airportcdm/'
plan = '//*[@id="226386065"]/td[4]'
t = re.findall(r'\d{9}', plan)
t1 = '//*[@id="'
t2 = '"]/td[11]'
tobt = t1 + t[0] + t2
tobt1 = '//*[@id="tobt"]'
if __name__ == '__main__':
    d = PyTest_main.PyTest(browser='chrome')
    d.make_maxwindow()
    d.open(url=url_url)
    d.send_key(fangfa='id', dingwei='logon_username', text='zlxydev')
    d.send_key(fangfa='id', dingwei='logon_password', text='82325o5o')
    d.element(fangfa='class', dingwei='logon_form_button').click()
    time.sleep(5)
    '''
    uurl = d.get_url()
    name_pass = {'username': "zlxydev",
                 'password': "ODIzMjVvNW8"}
    req = requests.Session()
    response = req.post(url_url, data=name_pass)
    print(response)
    zhu = req.get(uurl)
    print(zhu.text)
    
    res = requests.get(uurl)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'lxml')
    data = soup.select('#main_canvas_grid_table > tbody')
    for air_id in data:
        print(air_id.get('id'))
    '''
    # airport_shouxian(t, p1, c1)
    # airplan(plan, tobt, tobt1)
