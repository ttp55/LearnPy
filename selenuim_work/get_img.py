# @Time : 2024/12/25 12:59
# @Author : WZG
# --coding:utf-8--

from selenium import webdriver
from PIL import Image
import requests


url_url = 'http://192.168.210.57/'


def get_img_C():
    i = 0
    while i < 1000:
        fil_na = 'E://train/code%s.png' %i

        d.find_element_by_xpath('//*[@id="active_4"]/div').click()
        d.find_element_by_xpath('//*[@id="gate_English"]/div/div[3]/img').click()  # 点击刷新验证码
        code_img = d.find_element_by_xpath('//*[@id="gate_English"]/div/div[3]/img')
        code_url = code_img.get_attribute('src')
        response = requests.get(code_url)

        with open(fil_na, 'wb')as file:
            file.write(response.content)
        i += 1


if __name__ == "__main__":
    d = webdriver.Chrome()
    d.maximize_window()
    d.get(url_url)
    d.implicitly_wait(1)
    get_img_C()