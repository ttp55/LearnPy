# @Time : 2024/12/20 11:04
# @Author : WZG
# --coding:utf-8--

from selenium import webdriver
from PIL import Image
import pytesseract
import re
import os
import time
import random
from selenuim_work import img_ctrl
from selenuim_work import img_ctrl01

import ddddocr
import sys
import traceback


url_url = 'http://192.168.210.57/'

users = 'cal'
passW = 'Zlll@20210701'
login_status = 0


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

        ran = Image.open('E://img/code.png')#打开图片

        box = (1300,665,1430,705)#设置截图区域

        try:
            ran.crop(box).save(code_fill)#截图
        except:pass

        with open(code_fill, 'rb') as f:
            img_cod = f.read()

        ocr = ddddocr.DdddOcr()#使用训练数据模型，成功率最高，90%以上
        img_str = ocr.classification(img_cod)

        '''
        img = img_ctrl01.chuli01() #这个方法成功率相对高 但还是不够高，识别成功率大概20%
        img_str = pytesseract.image_to_string(img, config='--psm 10 --oem 3')
        img_str = re.sub(r'[^a-zA-Z0-9]', '', img_str)

        
        img_ctrl.chuli()#引用方法 这个方法成功率稍低 成功率低于10%

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
                global login_status
                login_status = 1


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


def NONSCHEDULEDLANDING_new_plan(plan_count):
    try:
        d.find_element_by_xpath('//*[@id="div_content"]/div[1]/div').click()#点击临时落地模块//*[@id="div_content"]/div[2]/div
        d.find_element_by_id('NoticeDetermine').click()#勾选同意
        d.find_element_by_xpath('//*[@id="NoticeBtn"]').click()#点击确认

    except Exception as e:
        print(f'异常:{e}')

    for i in range(plan_count):
        try:
            try:
                d.switch_to.default_content()#跳出iframe
                d.find_element_by_xpath('//*[@id="myTab"]/li[1]/a').click()#点击application List
            except:pass

            try:
                d.switch_to.frame('HomeContent')  # 进入iframe
            except:
                pass
            d.find_element_by_xpath('//*[@id="btn_add"]').click()#点击ADD
            d.find_element_by_id('btn_selecttemplate').click()#点击选择模板
            d.find_element_by_xpath('//*[@id="tempbody"]/div/div/div[1]/small/input').click()#选择模板
            d.find_element_by_id('FLIGHTID').send_keys(random.randint(100, 10000))#输入航班号

            d.find_element_by_xpath('//*[@id="plan_tb"]/tbody/tr[1]/td[2]/span/span/a').click()#点击下拉框
            d.implicitly_wait(4)
            try:
                d.find_element_by_xpath('//*[@id="_easyui_combobox_i7_0"]').click()#点击选项
            except:
                d.find_element_by_xpath('//*[@id="_easyui_combobox_i1_0"]').click()  # 点击选项
            d.find_element_by_xpath('//*[@id="plan_tb"]/tbody/tr[1]/td[3]/span/span/a').click()#点击机型下拉框机
            d.implicitly_wait(3)
            try:
                d.find_element_by_xpath('//*[@id="_easyui_combobox_i7_0"]').click()#点击选项
            except:
                d.find_element_by_xpath('//*[@id="_easyui_combobox_i1_0"]').click()  # 点击选项
            #d.find_element_by_id('_easyui_textbox_input6').send_keys()#输入起飞机场

            d.find_element_by_xpath('//*[@id="plan_tb"]/tbody/tr[1]/td[4]/span/span/a').click()#点击起飞机场下拉框
            d.implicitly_wait(3)

            d.find_element_by_id('_easyui_combobox_i5_%s'%random.randint(2, 85)).click()#选择机场
            d.find_element_by_id('DEPTIME').send_keys('0%s00'%random.randint(1, 9))#起飞时间
            d.find_element_by_id('ARRTIME').send_keys('%s00'%random.randint(10, 23))#降落时间
            #d.find_element_by_id('_easyui_textbox_input7').send_keys()#降落机场
            d.find_element_by_xpath('//*[@id="plan_tb"]/tbody/tr[1]/td[7]/span/span/a').click()#点击降落机场下拉框
            d.implicitly_wait(3)
            d.find_element_by_id('_easyui_combobox_i6_%s'%random.randint(766, 999)).click()#点击选择降落机场

            #d.find_element_by_id('EDATE_EN').send_keys('%sFEB2025' % random.randint(10, 28))#日期 这个方法点不到日期控件
            d.execute_script("document.getElementById('EDATE_EN').value = '%sFEB2025'" % random.randint(10, 28))#调用JS直接给日期赋值


            try:
                d.find_element_by_id('INPOINT').send_keys('TEBAK')#入境点
            except:
                d.find_element_by_id('btn_Create').click()
            try:
                d.find_element_by_xpath('//*[@id="rout_div"]/div/p/input').click()#选择航路
            except:
                d.find_element_by_id('ROUTE').send_keys('TEBAK')#录入航路

            d.find_element_by_id('btn_SavePlan').click()#save
            d.find_element_by_id('btn_Submit').click()#submit
            d.implicitly_wait(4)
            time.sleep(3)
            try:
                d.find_element_by_xpath('/html/body/div[13]/div/div/div[3]/button').click()#点击提交成功后的确认
            except:
                d.switch_to.default_content()#跳出iframe
                d.find_element_by_xpath('//*[@id="myTab"]/li[1]/a').click()#点击application LIst
        except Exception as e:
            print(f'异常:{e}')
            tb = sys.exc_info()[2]
            traceback.print_exception(e.__class__, e, tb)


if __name__ == "__main__":
    d = webdriver.Chrome()
    d.maximize_window()
    d.get(url_url)
    d.implicitly_wait(2)
    login()

if login_status == 1:
    NONSCHEDULEDLANDING_new_plan(20)