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
        d.find_element_by_xpath('//*[@id="mymanyModal"]/div/div/div[1]/button[1]').click()
    except:
        pass

    d.find_element_by_xpath('//*[@id="rigth-per-pwd"]').click()  # 点击账户设置

    #d.find_element_by_id('P_ACCOUNT_NATURE').click()  # 点击下拉框
    #d.execute_script("arguments[0].value='OPERATOR'", d.find_element_by_id('P_ACCOUNT_NATURE'))  # 点击选择运营人

    #d.find_element_by_id('P_INFO_SAVE').click()  # 点击保存
    #d.find_element_by_xpath('//*[@id="mymanyModal"]/div/div/div[1]/button').click()  # 点击OK

    # 获取账户性质
    sel = d.find_element_by_id('P_ACCOUNT_NATURE').get_attribute('value')
    print(sel)

    d.find_element_by_xpath('//*[@id="right-air-c"]').click()  # 点击 公司信息
    d.find_element_by_xpath('//*[@id="C_NAME_EN"]').send_keys('I')  # 输入公司名称
    d.find_element_by_xpath('//*[@id="C_NAME_CH"]').send_keys('不')  # 输入公司名称
    d.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div[4]/div/div[2]/table[1]/tbody/tr[3]/td[2]/span/span').click()
    d.find_element_by_id('_easyui_combobox_i3_%s' % random.randint(1, 50)).click()  # 国籍
    d.execute_script("document.getElementById('C_ESTABLISHMENT').value = '2024-02-%s'" % random.randint(10, 28))

    for i in range(1, 7):
        try:
            d.find_element_by_xpath('//*[@id="table_C"]/tbody/tr[%s]/td[5]/a' % i).click()  # 点击上传文件
            d.find_element_by_xpath('//*[@id="mymanyModal"]/div/div/div[2]/div/div[3]/div[2]/div').click()  # 点击选择文件
            time.sleep(1)
            m.click(1000, 660)
            m.click(1000, 660)
            time.sleep(1)
            try:
                d.execute_script("document.getElementById('START_TIME_%s').value = '2024-02-%s'" % (i, random.randint(10, 28)))
                d.execute_script("document.getElementById('END_TIME_%s').value = '2025-05-%s'" % (i, random.randint(10, 28)))
            except:pass
        except: break

        try:

            d.find_element_by_xpath('//*[@id="mymanyModal"]/div/div/div[2]/div/div[3]/div[2]/a').click()  # 点击upload
            d.find_element_by_xpath('//*[@id="mymanyModal"]/div/div/div[1]/button').click()  # 点击X
        except:
            pass
        time.sleep(1)
    d.find_element_by_xpath('//*[@id="P_NAME"]').send_keys('I')  # 输入填报人信息
    d.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div[4]/div/div[4]/table[1]/tbody/tr[1]/td[4]/span/span').click()
    d.find_element_by_id('_easyui_combobox_i5_%s' % random.randint(1, 200)).click()
    d.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div[4]/div/div[4]/table[1]/tbody/tr[1]/td[6]/span/span').click()
    d.find_element_by_id('_easyui_combobox_i1_%s' % random.randint(0, 1)).click()
    d.execute_script("document.getElementById('P_BIRTHDAY').value = '2000-02-%s'" % random.randint(10, 28))
    d.find_element_by_xpath('//*[@id="P_POSITION"]').send_keys('蒙')
    d.find_element_by_id('P_TEL').send_keys('%s' % random.randint(1, 9))
    d.find_element_by_id('P_EMAIL').send_keys('%s@123.com' % random.randint(1, 9))
    d.find_element_by_id('P_FAX').send_keys('0%s' % random.randint(1, 9))

    d.execute_script("document.getElementById('START_TIME_18').value = '2024-02-%s'" % random.randint(10, 28))
    d.execute_script("document.getElementById('END_TIME_18').value = '2025-05-%s'" % random.randint(10, 28))

    d.find_element_by_xpath('//*[@id="table_P"]/tbody/tr/td[5]/a').click()  # 点击上传文件
    d.find_element_by_xpath('//*[@id="myModal"]/div/div/div[2]/div/div[3]/div[2]/div').click()  # 点击选择文件
    time.sleep(1)
    m.click(1000, 660)
    m.click(1000, 660)
    time.sleep(1)
    try:

        d.find_element_by_xpath('//*[@id="myModal"]/div/div/div[2]/div/div[3]/div[2]/a').click()  # 点击upload
        #d.find_element_by_xpath('/html/body/div[11]/div/div/div[2]/button').click()  # 点击确定
    except:
        pass
    time.sleep(1)
    d.find_element_by_id('L_NAME').send_keys('I')  # 输入法人信息
    d.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div[4]/div/div[6]/table[1]/tbody/tr[1]/td[4]/span/span').click()
    d.find_element_by_id('_easyui_combobox_i4_%s' % random.randint(1, 200)).click()
    d.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div[4]/div/div[6]/table[1]/tbody/tr[1]/td[6]/span/span').click()
    d.find_element_by_id('_easyui_combobox_i2_%s' % random.randint(0, 1)).click()
    d.execute_script("document.getElementById('L_BIRTHDAY').value = '2000-02-%s'" % random.randint(10, 28))
    d.find_element_by_xpath('//*[@id="L_POSITION"]').send_keys('蒙')
    d.find_element_by_id('L_TEL').send_keys('%s' % random.randint(1, 9))
    d.find_element_by_id('L_EMAIL').send_keys('%s@123.com' % random.randint(1, 9))
    d.find_element_by_id('L_FAX').send_keys('1%s' % random.randint(1, 9))

    d.execute_script("document.getElementById('START_TIME_17').value = '2024-02-%s'" % random.randint(10, 28))
    d.execute_script("document.getElementById('END_TIME_17').value = '2025-05-%s'" % random.randint(10, 28))

    d.find_element_by_xpath('//*[@id="table_L"]/tbody/tr/td[5]/a').click()  # 点击上传文件
    d.find_element_by_xpath('//*[@id="myModal"]/div/div/div[2]/div/div[3]/div[2]/div').click()  # 点击选择文件
    time.sleep(1)
    m.click(1000, 660)
    m.click(1000, 660)
    time.sleep(1)
    try:

        d.find_element_by_xpath('//*[@id="myModal"]/div/div/div[2]/div/div[3]/div[2]/a').click()  # 点击upload
        #d.find_element_by_xpath('/html/body/div[11]/div/div/div[2]/button').click()  # 点击确定
    except:
        pass
    d.find_element_by_id('C_SUBMIT').click()  # 点击保存
    time.sleep(2)
    d.find_element_by_xpath('/html/body/div[11]/div/div/div[2]/button').click()  # 点击OK

    d.find_element_by_xpath('//*[@id="right-air-a-new"]').click()  # 点击航空器信息
    #d.find_element_by_xpath('//*[@id="tb_aircraft"]/tbody/tr[3]/td[8]/div/a[1]').click()  # 点击编辑

    d.find_element_by_xpath('//*[@id="A_REGISTRATION_NUMBER"]').send_keys('B%s' % random.randint(1000, 9999))  # 录入航空器信息
    d.find_element_by_xpath('//*[@id="table_aircraft_record"]/tbody/tr[1]/td[4]/span/span').click()
    d.find_element_by_id('_easyui_combobox_i6_%s' % random.randint(0, 50)).click()
    d.find_element_by_xpath('//*[@id="table_aircraft_record"]/tbody/tr[1]/td[6]/span/span').click()
    d.find_element_by_id('_easyui_combobox_i7_%s' % random.randint(0, 9)).click()
    d.find_element_by_id('A_OPERATOR').send_keys('Vista Jet Limited22')
    d.find_element_by_id('A_OWNER').send_keys('李')
    d.find_element_by_xpath('//*[@id="table_aircraft_record"]/tbody/tr[2]/td[6]/span/span').click()
    d.find_element_by_id('_easyui_combobox_i8_%s' % random.randint(0, 10)).click()

    #判断是否为代理
    if sel == 'AGENT':
        time.sleep(3)
        d.find_element_by_xpath('//*[@id="A_AIRCRAFT_NATURE"]').click()
        d.execute_script("arguments[0].value='AGENT'", d.find_element_by_id('A_AIRCRAFT_NATURE'))
    else:pass

    for i in range(1, 8):
        try:
            d.find_element_by_xpath('//*[@id="table_A"]/tbody/tr[%s]/td[5]/a' % i).click()  # 点击上传文件
            d.find_element_by_xpath('//*[@id="myModal"]/div/div/div[2]/div/div[3]/div[2]/div').click()  # 点击browse
            time.sleep(1)
            m.click(1000, 660)
            m.click(1000, 660)
            time.sleep(1)
            d.execute_script(
                "document.getElementById('START_TIME_%s').value = '2024-02-%s'" % (i + 9, random.randint(10, 28)))
            d.execute_script(
                "document.getElementById('END_TIME_%s').value = '2025-05-%s'" % (i + 9, random.randint(10, 28)))
        except:pass
        try:

            d.find_element_by_xpath('//*[@id="myModal"]/div/div/div[2]/div/div[3]/div[2]/a').click()  # 点击upload
            #d.find_element_by_xpath('/html/body/div[12]/div/div/div[2]/button').click()  # 点击确定
        except:
            pass
    try:
        d.find_element_by_id('A_SUBMIT').click()  # 保存
        time.sleep(2)
        d.find_element_by_xpath('/html/body/div[11]/div/div/div[2]/button').click()
    except:pass
    try:
        d.find_element_by_xpath('//*[@id="sbld"]').click()  # 点击logout
    except:pass


