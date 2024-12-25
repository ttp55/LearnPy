# @Time : 2024/12/20 11:04
# @Author : WZG
# --coding:utf-8--

from selenium import webdriver
from PIL import Image
import pytesseract
import re
import os
import time
from selenuim_work import img_ctrl
from selenuim_work import img_ctrl01

url_url = 'http://192.168.210.57/'

users = 'abd'
passW = 'Zlll@20210701'


def login():
    d.find_element_by_xpath('//*[@id="active_4"]/div').click()

    d.find_element_by_xpath('//*[@id="TD4_1"]').click()
    d.find_element_by_xpath('//*[@id="TD4_1"]').send_keys(users)
    time.sleep(1)
    d.find_element_by_xpath('//*[@id="TD4_2"]').click()
    d.find_element_by_xpath('//*[@id="TD4_2"]').send_keys(passW)
    time.sleep(1)

    def jietu():
        code_fill = 'E://img/code1.png'

        d.save_screenshot('E://img/code.png')#截全图
        try:
            ran = Image.open('E://img/code.png')#打开图片
        except: pass

        box = (1300,665,1430,705)#设置截图区域

        try:
            ran.crop(box).save(code_fill)#截图
        except:pass


        img = img_ctrl01.chuli01() #这个方法成功率相对高
        img_str = pytesseract.image_to_string(img, config='--psm 10 --oem 3')
        img_str = re.sub(r'[^a-zA-Z0-9]', '', img_str)

        '''
        img_ctrl.chuli()#引用方法 这个方法成功率稍低

        code_img = Image.open(img_ctrl.binary_file)#打开图片

        img_str = pytesseract.image_to_string(code_img, config='--psm 10 --oem 3')#使用LSTM OCR引擎，通常更准确
        img_str = re.sub(r'[^a-zA-Z0-9]', '', img_str)#正则去掉除文本外的内容
        '''

        try:
            os.remove('E://img/code.png')

            os.remove('E://img/code1.png')

            #os.remove('E://img/code2.png')

            #os.remove('E://img/code3.png')

            #os.remove('E://img/code4.png')
            print("文件删除成功")
        except FileNotFoundError:
            print("文件不存在")
        except PermissionError:
            print("权限不足，无法删除文件")
        print(img_str)
        if len(img_str) == 4:
            d.find_element_by_xpath('//*[@id="TD4_3"]').send_keys(img_str)
            d.find_element_by_xpath('//*[@id="LoginEnglish"]').click()  # 点击登录
            try:
                d.find_element_by_id('sbld')
                print('登录成功')


            except:
                #login_value = d.element(fangfa='id', dingwei='LoginData_English').get_attribute('value')# 获取登录状态
                #login_value = re.findall(r'-2', login_value)
                print('验证码错误')
                d.find_element_by_xpath('// *[ @ id = "TD4_3"]').clear()  # 清空验证码输入框
                jietu()


        else:
            d.find_element_by_xpath('//*[@id="gate_English"]/div/div[3]/img').click()#点击刷新验证码
            d.find_element_by_xpath('// *[ @ id = "TD4_3"]').clear()  # 清空验证码输入框
            jietu()

    jietu()
    '''
        code_url = code_img.get_attribute('src')
        response = requests.get(code_url)
        with open('code.png', 'wb')as file:
            file.write(response.content)
            能获取到，但获取的不对，只能用截图的方式

    '''

    #d.driver.quit()


if __name__ == "__main__":
    d = webdriver.Chrome()
    d.maximize_window()
    d.get(url_url)
    d.implicitly_wait(1)
    login()