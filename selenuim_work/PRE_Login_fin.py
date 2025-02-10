# @Time : 2024/12/20 11:04
# @Author : WZG
# --coding:utf-8--

from selenium import webdriver
from PIL import Image
import os
import time
from selenuim_work.module_Work import BUSINESS_REGISTRATION, NONSCHEDULED_OVERFLY, NONSCHEDULEDLANDING, \
    NO_MAINLAND_BUSINESS_FLIGHTPLAN,NO_MAINLAND_BUSINESS_FLIGHTPLAN
import ddddocr
import sys
import traceback
import random

url_url = 'http://192.168.210.57/'


passW = 'Zlll@20210701'
login_status = 0


def login(user):

    d.find_element_by_xpath('//*[@id="active_4"]/div').click()
    d.find_element_by_xpath('//*[@id="TD4_1"]').clear()
    d.find_element_by_xpath('//*[@id="TD4_1"]').send_keys(user)
    time.sleep(1)
    d.find_element_by_xpath('//*[@id="TD4_2"]').send_keys(passW)
    time.sleep(1)

    def jietu():
        code_fill = 'E://img/code1.png'

        d.save_screenshot('E://img/code.png')  # 截全图

        ran = Image.open('E://img/code.png')  # 打开图片

        box = (1300, 665, 1430, 705)  # 设置截图区域

        try:
            ran.crop(box).save(code_fill)  # 截图
        except:pass

        with open(code_fill, 'rb') as f:
            img_cod = f.read()

        ocr = ddddocr.DdddOcr()  # 使用训练数据模型，成功率最高，90%以上
        img_str = ocr.classification(img_cod)

        '''
        img = img_ctrl01.chuli01() #这个方法成功率相对高 但还是不够高，识别成功率大概20%
        img_str = pytesseract.image_to_string(img, config='--psm 10 --oem 3')
        img_str = re.sub(r'[^a-zA-Z0-9]', '', img_str)

        
        img_ctrl.chuli()  # 引用方法 这个方法成功率稍低 成功率低于10%

        code_img = Image.open(img_ctrl.binary_file)  # 打开图片

        img_str = pytesseract.image_to_string(code_img, config='--psm 10 --oem 3')  # 使用LSTM OCR引擎，通常更准确
        img_str = re.sub(r'[^a-zA-Z0-9]', '', img_str)  # 正则去掉除文本外的内容
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
                global login_status
                login_status = 1

            except:
                #login_value = d.element(fangfa='id', dingwei='LoginData_English').get_attribute('value')  #  获取登录状态
                #login_value = re.findall(r'-2', login_value)
                print('验证码错误')
                d.find_element_by_xpath('// *[ @ id = "TD4_3"]').clear()  # 清空验证码输入框
                jietu()


        else:
            d.find_element_by_xpath('//*[@id="gate_English"]/div/div[3]/img').click()  # 点击刷新验证码
            d.find_element_by_xpath('// *[ @ id = "TD4_3"]').clear()  # 清空验证码输入框
            jietu()

    jietu()
    '''
        code_url = code_img.get_attribute('src')
        response = requests.get(code_url)
        with open('code.png', 'wb')as file:
            file.write(response.content)
            能获取到验证码，但获取的不对，只能用截图的方式

    '''

    #d.driver.quit()


users = 'sjatczhm'
users2 = 'bdj'
users3 = 'bdj_01'
users4 = 'cal'

if __name__ == "__main__":
    d = webdriver.Chrome()
    d.maximize_window()
    d.get(url_url)
    d.implicitly_wait(4)
    login(users2)  # 用户登录
    if login_status == 1:
        # 临时落地 新增计划
        #NONSCHEDULEDLANDING.new_cnl_plan(d, 1, '2024F0063')
        #NONSCHEDULEDLANDING.new_chg_plan(d, 2, '2024F0063')
        #NONSCHEDULEDLANDING.new_add_plan(d, 2)

        # 公务机 公司上传备案
        BUSINESS_REGISTRATION.beian_shenpi(d)

        #临时飞越 新增计划
        #NONSCHEDULED_OVERFLY.new_add_plan(d, plan_count=2)
        #NONSCHEDULED_OVERFLY.new_chg_plan(d, plan_count=2, permission_no='4206')

        #国外公务机
        # NO_MAINLAND_BUSINESS_FLIGHTPLAN.new_add_plan(d, 1)


