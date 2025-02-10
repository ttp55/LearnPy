# @Time : 2025/1/23 14:13
# @Author : WZG
# --coding:utf-8--

import time
import random
from pymouse import PyMouse

m = PyMouse()


def beian_shenpi(d):
    try:
        d.find_element_by_xpath('//*[@id="div_content"]/div[1]/div/div[1]').click()
    except Exception as e:
        print(f'异常:{e}')
    try:
        d.find_element_by_xpath('/html/body/div[11]/div/div/div[2]/button[1]').click()
    except:
        pass

    d.find_element_by_xpath('//*[@id="rigth-per-pwd"]').click()  # 点击账户设置

    d.find_element_by_id('P_ACCOUNT_NATURE').click()  # 点击下拉框
    d.execute_script("arguments[0].value='OPERATOR'", d.find_element_by_id('P_ACCOUNT_NATURE'))  # 点击选择运营人

    d.find_element_by_id('P_INFO_SAVE').click()  # 点击保存
    d.find_element_by_xpath('/html/body/div[11]/div/div/div[2]/button').click()  # 点击OK

    d.find_element_by_xpath('//*[@id="right-air-c"]').click()  # 点击 公司信息
    d.find_element_by_xpath('//*[@id="C_NAME_EN"]').send_keys('bdj')  # 输入公司名称
    d.find_element_by_xpath('//*[@id="C_NAME_CH"]').send_keys('不')  # 输入公司名称

    d.execute_script("document.getElementById('START_TIME_1').value = '%sFEB2024'" % random.randint(1, 28))
    d.execute_script("document.getElementById('END_TIME_1').value = '%sMAR2025'" % random.randint(1, 28))

    d.find_element_by_xpath('//*[@id="table_C"]/tr[1]/td[4]/a/i').click()  # 点击上传文件
    d.find_element_by_xpath('//*[@id="myModal"]/div/div/div[2]/div/div[3]/div[2]/div').click()  # 点击选择文件
    time.sleep(1)
    m.click(1000, 634)
    time.sleep(1)
    m.click(1200, 838)
    time.sleep(1)
    try:

        d.find_element_by_xpath('//*[@id="myModal"]/div/div/div[2]/div/div[3]/div[2]/a').click()  # 点击upload
        d.find_element_by_xpath('/html/body/div[11]/div/div/div[2]/button').click()  # 点击确定
    except:
        pass

    d.find_element_by_xpath('//*[@id="P_NAME"]').send_keys('bdj')  # 输入填报人信息
    d.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div[4]/div/div[4]/table[1]/tbody/tr[1]/td[4]/span/span').click()
    d.find_element_by_id('_easyui_combobox_i5_%s' % random.randint(1, 200)).click()
    d.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div[4]/div/div[4]/table[1]/tbody/tr[1]/td[6]/span/span').click()
    d.find_element_by_id('_easyui_combobox_i1_%s' % random.randint(0, 1)).click()
    d.execute_script("document.getElementById('P_BIRTHDAY').value = '%sFEB2000'" % random.randint(10, 28))
    d.find_element_by_xpath('//*[@id="P_POSITION"]').send_keys('蒙')
    d.find_element_by_id('P_TEL').send_keys('%s' % random.randint(11111111111, 19999999999))
    d.find_element_by_id('P_EMAIL').send_keys('%s@123.com' % random.randint(111, 1999))
    d.find_element_by_id('P_FAX').send_keys('010%s' % random.randint(11111111, 19999999))

    d.execute_script("document.getElementById('START_TIME_18').value = '%sFEB2024'" % random.randint(1, 28))
    d.execute_script("document.getElementById('END_TIME_18').value = '%sMAR2025'" % random.randint(1, 28))

    d.find_element_by_xpath('//*[@id="table_P"]/tr/td[4]/a').click()  # 点击上传文件
    d.find_element_by_xpath('//*[@id="myModal"]/div/div/div[2]/div/div[3]/div[2]/div').click()  # 点击选择文件
    time.sleep(1)
    m.click(1000, 634)
    time.sleep(1)
    m.click(1200, 838)
    time.sleep(1)
    try:

        d.find_element_by_xpath('//*[@id="myModal"]/div/div/div[2]/div/div[3]/div[2]/a').click()  # 点击upload
        d.find_element_by_xpath('/html/body/div[11]/div/div/div[2]/button').click()  # 点击确定
    except:
        pass

    d.find_element_by_xpath('//*[@id="L_NAME"]').send_keys('bdj')  # 输入法人信息
    d.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div[4]/div/div[6]/table[1]/tbody/tr[1]/td[4]/span/span').click()
    d.find_element_by_id('_easyui_combobox_i4_%s' % random.randint(1, 200)).click()
    d.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div[4]/div/div[6]/table[1]/tbody/tr[1]/td[6]/span/span').click()
    d.find_element_by_id('_easyui_combobox_i2_%s' % random.randint(0, 1)).click()
    d.execute_script("document.getElementById('L_BIRTHDAY').value = '%sFEB2000'" % random.randint(10, 28))
    d.find_element_by_xpath('//*[@id="L_POSITION"]').send_keys('蒙')
    d.find_element_by_id('L_TEL').send_keys('%s' % random.randint(11111111111, 19999999999))
    d.find_element_by_id('L_EMAIL').send_keys('%s@123.com' % random.randint(111, 1999))
    d.find_element_by_id('L_FAX').send_keys('010%s' % random.randint(11111111, 19999999))

    d.execute_script("document.getElementById('START_TIME_17').value = '%sFEB2024'" % random.randint(1, 28))
    d.execute_script("document.getElementById('END_TIME_17').value = '%sMAR2025'" % random.randint(1, 28))

    d.find_element_by_xpath('//*[@id="table_L"]/tr/td[4]/a').click()  # 点击上传文件
    d.find_element_by_xpath('//*[@id="myModal"]/div/div/div[2]/div/div[3]/div[2]').click()  # 点击选择文件
    time.sleep(1)
    m.click(1000, 634)
    time.sleep(1)
    m.click(1200, 838)
    time.sleep(1)
    try:

        d.find_element_by_xpath('//*[@id="myModal"]/div/div/div[2]/div/div[3]/div[2]/a').click()  # 点击upload
        d.find_element_by_xpath('/html/body/div[12]/div/div/div[2]/button').click()  # 点击确定
    except:
        pass
    d.find_element_by_id('C_SUBMIT').click()  # 点击保存
    d.find_element_by_xpath('/html/body/div[11]/div/div/div[2]/button').click()  # 点击OK

    d.find_element_by_xpath('//*[@id="right-air-a-new"]').click()  # 点击航空器信息
    d.find_element_by_xpath('//*[@id="tb_aircraft"]/tbody/tr[6]/td[8]/div/a[1]').click()  # 点击编辑

    d.execute_script("document.getElementById('START_TIME_10').value = '%sFEB2024'" % random.randint(1, 28))
    d.execute_script("document.getElementById('END_TIME_10').value = '%sMAR2025'" % random.randint(1, 28))

    d.find_element_by_xpath('//*[@id="table_A"]/tr[1]/td[4]/a').click()  # 点击上传文件
    d.find_element_by_xpath('//*[@id="myModal"]/div/div/div[2]/div/div[3]/div[2]').click()  # 点击browse
    time.sleep(1)
    m.click(1000, 634)
    time.sleep(1)
    m.click(1200, 838)
    time.sleep(1)
    try:

        d.find_element_by_xpath('//*[@id="myModal"]/div/div/div[2]/div/div[3]/div[2]/a').click()  # 点击upload
        d.find_element_by_xpath('/html/body/div[12]/div/div/div[2]/button').click()  # 点击确定
    except:
        pass
    try:
        d.find_element_by_xpath('//*[@id="sbld"]').click()  # 点击logout

    except:pass


