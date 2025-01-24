# @Time : 2025/1/23 10:58
# @Author : WZG
# --coding:utf-8--
import re
import os
import time
import random
import sys
import traceback


def new_add_plan(d, plan_count):
    try:
        d.find_element_by_xpath('//*[@id="div_content"]/div[1]/div').click()  # 点击临时落地模块//*[@id="div_content"]/div[2]/div
        d.find_element_by_id('NoticeDetermine').click()  # 勾选同意
        d.find_element_by_xpath('//*[@id="NoticeBtn"]').click()  # 点击确认

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
            d.find_element_by_xpath('//*[@id="plan_tb"]/tbody/tr[1]/td[2]/span/span/a').click()  # 点击下拉框

            try:
                d.find_element_by_xpath('//*[@id="_easyui_combobox_i7_0"]').click()  # 点击选项
            except:
                d.find_element_by_xpath('//*[@id="_easyui_combobox_i1_0"]').click()  # 点击选项
            d.find_element_by_xpath('//*[@id="plan_tb"]/tbody/tr[1]/td[3]/span/span/a').click()  # 点击机型下拉框机

            try:
                d.find_element_by_xpath('//*[@id="_easyui_combobox_i7_0"]').click()  # 点击选项
            except:
                d.find_element_by_xpath('//*[@id="_easyui_combobox_i1_0"]').click()  # 点击选项
            #d.find_element_by_id('_easyui_textbox_input6').send_keys()  # 输入起飞机场

            d.find_element_by_xpath('//*[@id="plan_tb"]/tbody/tr[1]/td[4]/span/span/a').click()  # 点击起飞机场下拉框

            d.find_element_by_id('_easyui_combobox_i5_%s'%random.randint(2, 85)).click()  # 选择机场
            d.find_element_by_id('DEPTIME').send_keys('0%s00'%random.randint(1, 9))  # 起飞时间
            d.find_element_by_id('ARRTIME').send_keys('%s00'%random.randint(10, 23))  # 降落时间
            #d.find_element_by_id('_easyui_textbox_input7').send_keys()  # 降落机场
            d.find_element_by_xpath('//*[@id="plan_tb"]/tbody/tr[1]/td[7]/span/span/a').click()  # 点击降落机场下拉框

            d.find_element_by_id('_easyui_combobox_i6_%s'%random.randint(766, 999)).click()  # 点击选择降落机场

            #d.find_element_by_id('EDATE_EN').send_keys('%sFEB2025' % random.randint(10, 28))  # 日期 这个方法点不到日期控件
            d.execute_script("document.getElementById('EDATE_EN').value = '%sFEB2025'" % random.randint(10, 28))
            # 调用JS直接给日期赋值


            try:
                d.find_element_by_id('INPOINT').send_keys('TEBAK')  # 入境点
            except:
                d.find_element_by_id('OUTPOINT').send_keys('TEBAK')  # 出境点
            try:
                d.find_element_by_id('btn_Create').click()  # 点击serach
                d.find_element_by_xpath('//*[@id="rout_div"]/div/p/input').click()  # 选择航路
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

def new_chg_plan(d, plan_count, permission_no):
    try:
        d.find_element_by_xpath('//*[@id="div_content"]/div[1]/div').click()
        # 点击临时落地模块//*[@id="div_content"]/div[2]/div
        d.find_element_by_id('NoticeDetermine').click()  # 勾选同意
        d.find_element_by_xpath('//*[@id="NoticeBtn"]').click()  # 点击确认

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
            d.find_element_by_xpath('//*[@id="btn_chg"]').click()
            d.find_element_by_id('btn_selecttemplate').click()  # 点击选择模板
            d.find_element_by_xpath('//*[@id="tempbody"]/div/div/div[1]/small/input').click()  # 选择模板
            d.find_element_by_id('PNUM_END').send_keys(permission_no)

            d.find_element_by_xpath('//*[@id="plan_tb"]/tbody/tr[1]/td[11]/div/button[1]').click()  # 点击select
            time.sleep(1)
            d.find_element_by_xpath('//*[@id="box0"]/label/input').click()  # 点击日期
            d.find_element_by_xpath('//*[@id="ReplyTab"]/tbody/tr/td[1]/input').click()  # 点击选择
            d.find_element_by_id('btn_copy').click()  # 点击copy
            d.execute_script("document.getElementById('EDATE_EN_R').value = '%sFEB2025'" % random.randint(10, 28))
            # 调用JS直接给日期赋值

            try:
                d.find_element_by_id('INPOINT_R').send_keys('TEBAK')  # 入境点
            except:
                d.find_element_by_id('OUTPOINT').send_keys('TEBAK')  # 出境点
            try:
                d.find_element_by_id('btn_Create_R').click()  # 点击search
                d.find_element_by_xpath('//*[@id="rout_div"]/div/p/input').click()  # 选择航路
            except:
                d.find_element_by_id('ROUTE_R').send_keys('TEBAK')  # 录入航路

            d.find_element_by_id('btn_SavePlan').click()  # save
            d.find_element_by_id('btn_Submit').click()  # submit
            time.sleep(3)

            try:
                d.find_element_by_xpath('/html/body/div[16]/div/div/div[3]/button').click()  # 点击提交成功后的确认
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


def new_cnl_plan(d, plan_count, permission_no):
    try:
        d.find_element_by_xpath('//*[@id="div_content"]/div[1]/div').click()
        # 点击临时落地模块//*[@id="div_content"]/div[2]/div
        d.find_element_by_id('NoticeDetermine').click()  # 勾选同意
        d.find_element_by_xpath('//*[@id="NoticeBtn"]').click()  # 点击确认

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
            d.find_element_by_xpath('//*[@id="btn_cnl"]').click()
            d.find_element_by_id('btn_selecttemplate').click()  # 点击选择模板
            d.find_element_by_xpath('//*[@id="tempbody"]/div/div/div[1]/small/input').click()  # 选择模板
            d.find_element_by_id('PNUM_END').send_keys(permission_no)

            d.find_element_by_xpath('//*[@id="plan_tb"]/tbody/tr/td[10]/div/button[1]').click()  # 点击select
            time.sleep(1)
            d.find_element_by_xpath('//*[@id="box0"]/label/input').click()  # 点击日期
            d.find_element_by_xpath('//*[@id="ReplyTab"]/tbody/tr/td[1]/input').click()  # 点击选择

            d.find_element_by_id('btn_SavePlan').click()  # save
            d.find_element_by_id('btn_Submit').click()  # submit
            time.sleep(3)

            try:
                d.find_element_by_xpath('/html/body/div[11]/div/div/div[3]/button').click()  # 点击提交成功后的确认
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
