# @Time : 2025/1/24 9:19
# @Author : WZG
# --coding:utf-8--

import time
import random
import sys
import traceback


def new_add_plan(d, plan_count):
    try:
        d.find_element_by_xpath('//*[@id="div_content"]/div[3]/div/div[1]').click()  # 点击临时飞越模块//*[@id="div_content"]/div[2]/div

    except Exception as e:
        print(f'异常:{e}')

    for i in range(plan_count):
        try:
            try:
                d.switch_to.default_content()  # 跳出iframe
                d.find_element_by_xpath('//*[@id="myTab"]/li[1]/a').click()  # 点击application List
            except:pass

            try:
                d.switch_to.frame('HomeContent')  # 进入iframe
            except:
                pass
            d.find_element_by_xpath('//*[@id="btn_add"]').click()  # 点击ADD
            d.find_element_by_id('btn_selecttemplate').click()  # 点击选择模板
            d.find_element_by_xpath('//*[@id="tempbody"]/div/div/div[1]/small/input').click()  # 选择模板
            d.find_element_by_id('FLIGHTID').send_keys(random.randint(100, 10000))  # 输入航班号
            time.sleep(1)
            d.find_element_by_xpath('//*[@id="plan_tb"]/tbody/tr[1]/td[2]/span/span').click()  # 点击机型下拉框
            try:
                d.find_element_by_xpath('//*[@id="_easyui_combobox_i7_0"]').click()  # 点击选项
            except:
                d.find_element_by_xpath('//*[@id="_easyui_combobox_i1_0"]').click()  # 点击选项

            d.find_element_by_xpath('//*[@id="plan_tb"]/tbody/tr[1]/td[3]/span/span').click()  # 点击起飞机场下拉框

            d.find_element_by_id('_easyui_combobox_i4_%s'%random.randint(1, 985)).click()  # 选择机场
            d.find_element_by_id('DEPTIME').send_keys('0%s00'%random.randint(1, 9))  # 起飞时间
            d.find_element_by_id('ARRTIME').send_keys('%s00'%random.randint(10, 23))  # 降落时间
            d.find_element_by_xpath('//*[@id="plan_tb"]/tbody/tr[1]/td[6]/span/span').click()  # 点击降落机场下拉框

            d.find_element_by_id('_easyui_combobox_i5_%s'%random.randint(1, 985)).click()  # 点击选择降落机场

            d.execute_script("document.getElementById('EDATE_EN').value = '%sFEB2025'" % random.randint(10, 28))
            # 调用JS直接给日期赋值


            try:
                d.find_element_by_xpath('//*[@id="plan_tb"]/tbody/tr[2]/td[1]/div/div[3]').click()  # 点击serach
                d.find_element_by_xpath('//*[@id="tb_myroute"]/tbody/tr[3]').click()  # 选择航路
            except:
                d.find_element_by_id('ROUTE').send_keys('TEBAK')  # 录入航路

            d.find_element_by_id('btn_SavePlan').click()  # save
            d.find_element_by_id('btn_Submit').click()  # submit

            time.sleep(3)
            try:
                d.find_element_by_xpath('/html/body/div[13]/div/div/div[3]/button').click()  # 点击提交成功后的确认
            except:
                d.switch_to.default_content()  # 跳出iframe
                d.find_element_by_xpath('//*[@id="myTab"]/li[1]/a').click()  # 点击application LIst
        except Exception as e:
            print(f'异常:{e}')
            tb = sys.exc_info()[2]
            traceback.print_exception(e.__class__, e, tb)
    d.switch_to.default_content()
    d.find_element_by_xpath('/html/body/div/div[1]/ul[4]/li/a').click()
    d.find_element_by_xpath('//*[@id="sbld"]').click()  # 退出登录
