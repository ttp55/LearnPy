# @Time : 2024/12/31 10:43
# @Author : WZG
# --coding:utf-8--

import ddddocr
from selenium import webdriver
from PIL import Image


url_url = 'http://192.168.210.57/'


def login():
    d.find_element_by_xpath('//*[@id="active_4"]/div').click()
    code_fill = 'E://img/code1.png'

    d.save_screenshot('E://img/code.png')  # 截全图
    try:
        ran = Image.open('E://img/code.png')  # 打开图片
    except:
        pass

    box = (1300, 665, 1430, 705)  # 设置截图区域

    try:
        ran.crop(box).save(code_fill)  # 截图
    except:
        pass
    with open(code_fill, 'rb') as f:
        img_cod = f.read()

    ocr = ddddocr.DdddOcr()
    ocr_1 = ocr.classification(img_cod)
    print(ocr_1)




if __name__ == "__main__":
    d = webdriver.Chrome()
    d.maximize_window()
    d.get(url_url)
    d.implicitly_wait(2)
    login()