# @Time : 2025/3/17 13:07
# @Author : WZG
# --coding:utf-8--


import time
import random
import sys
import traceback
import pykeyboard
from pymouse import PyMouse
m = PyMouse()
k = pykeyboard.PyKeyboard()


def new_add_plan_nextday(d, plan_count):
    try:
        d.find_element_by_xpath('//*[@id="div_content"]/div[4]/div/div[1]').click()
        # 点击国内公务机
    except Exception as e:
        print(f'异常:{e}')

    for i in range(plan_count):
        try:
            try:
                d.switch_to.default_content()  # 跳出iframe
                d.find_element_by_xpath('//*[@id="myTab"]/li[2]').click()  # 点击application List
            except:pass

            try:
                d.switch_to.frame('HomeContent')  # 进入iframe
            except:
                pass
            d.find_element_by_id('btn_add').click()  # 点击ADD

            d.find_element_by_id('FLIGHTID').send_keys(random.randint(100, 10000))  # 输入航班号
            d.find_element_by_id('REGNUM').send_keys('B3233')  # 输入注册号
            d.find_element_by_xpath('//*[@id="PlanTab"]/div/table/tbody/tr[1]/td[5]/span/span').click()  # 点击类型下拉框
            d.find_element_by_id('_easyui_combobox_i7_%s' % random.randint(1, 50)).click()

            d.find_element_by_xpath('//*[@id="PlanTab"]/div/table/tbody/tr[1]/td[6]/span/span').click()  # 点击起飞机场下拉框
            d.find_element_by_id('_easyui_combobox_i1_%s' % random.randint(766, 850)).click()  # 选择机场
            d.find_element_by_id('DEPTIME').send_keys('0%s00' % random.randint(1, 9))  # 起飞时间
            d.find_element_by_id('ARRTIME').send_keys('%s00' % random.randint(10, 23))  # 降落时间

            d.find_element_by_xpath('//*[@id="PlanTab"]/div/table/tbody/tr[1]/td[9]/span/span').click()  # 点击降落机场下拉框

            d.find_element_by_id('_easyui_combobox_i2_%s' % random.randint(850, 999)).click()  # 点击选择降落机场

            d.execute_script("document.getElementById('EXECDATE').value = '%sAPR2025'" % random.randint(10, 30))
            # 调用JS直接给日期赋值
            d.find_element_by_id('ROUTE').send_keys('TEBAK')  # 录入航路
            time.sleep(1)

            d.find_element_by_xpath('//*[@id="PlanTab"]/div/table/tbody/tr[1]/td[13]/button[1]').click()  # save
            d.find_element_by_xpath('/html/body/div[23]/div/div/div[2]/button').click()  # 点击OK

            d.find_element_by_id('btn_SubmitApply').click()  # submit

            try:
                d.find_element_by_xpath('/html/body/div[23]/div/div/div[2]/button[2]').click()  # 点击确定
                time.sleep(1)
                d.find_element_by_xpath('/html/body/div[23]/div/div/div[2]/button').click()
            except:
                d.find_element_by_xpath('/html/body/div[23]/div/div/div[3]/button').click()  # 判断是否需要上传附件
                d.find_element_by_xpath('//*[@id="div_plancontent"]/div/div/div/span[1]').click()
                time.sleep(1)
                d.find_element_by_xpath(
                    '//*[@id="handerModal"]/div/div/div[2]/ul[1]/li[2]/div/div[3]/div[2]/div').click()
                time.sleep(1)
                m.click(1000, 660)
                m.click(1000, 660)
                time.sleep(1)
                d.find_element_by_xpath(
                    '//*[@id="handerModal"]/div/div/div[2]/ul[1]/li[2]/div/div[3]/div[2]/a' % i).click()  # 点击upload
                d.find_element_by_id('btn_SaveInfo').click()  # 点击保存
                d.find_element_by_xpath('/html/body/div[24]/div/div/div[2]/button').click()

            d.switch_to.default_content()  # 跳出iframe

        except Exception as e:
            print(f'异常:{e}')
            tb = sys.exc_info()[2]
            traceback.print_exception(e.__class__, e, tb)
        d.switch_to.default_content()


def new_add_plan_today(d, plan_count):
    try:
        d.find_element_by_xpath('//*[@id="div_content"]/div[4]/div/div[1]').click()
        # 点击国内公务机
    except Exception as e:
        print(f'异常:{e}')
    for i in range(plan_count):
        try:
            d.switch_to.default_content()  # 跳出iframe

            d.find_element_by_xpath('//*[@id="myTab"]/li[3]').click()  # 点击todaylist

            try:
                d.switch_to.frame('HomeContent')  # 进入iframe
            except:
                pass
            d.find_element_by_id('btn_add').click()  # 点击ADD

            d.find_element_by_id('FLIGHTID').send_keys(random.randint(100, 10000))  # 输入航班号
            d.find_element_by_id('REGNUM').send_keys('B3233')  # 输入注册号
            d.find_element_by_xpath('//*[@id="PlanTab"]/div/table/tbody/tr[1]/td[5]/span/span').click()  # 点击类型下拉框
            d.find_element_by_id('_easyui_combobox_i7_%s' % random.randint(1, 50)).click()

            d.find_element_by_xpath('//*[@id="PlanTab"]/div/table/tbody/tr[1]/td[6]/span/span').click()  # 点击起飞机场下拉框
            d.find_element_by_id('_easyui_combobox_i1_%s' % random.randint(766, 850)).click()  # 选择机场
            d.find_element_by_id('DEPTIME').send_keys('0%s00' % random.randint(1, 9))  # 起飞时间
            d.find_element_by_id('ARRTIME').send_keys('%s00' % random.randint(10, 23))  # 降落时间

            d.find_element_by_xpath('//*[@id="PlanTab"]/div/table/tbody/tr[1]/td[9]/span/span').click()  # 点击降落机场下拉框

            d.find_element_by_id('_easyui_combobox_i2_%s' % random.randint(850, 999)).click()  # 点击选择降落机场

            # 获取当天日期
            mouth = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
            now = time.strftime("%d%m%Y", time.localtime())

            mou_ = int(now[2:4]) - 1
            day_ = now[0:2]
            year = now[4:]
            date_now = day_ + mouth[mou_] + year
            d.execute_script("document.getElementById('EXECDATE').value = '%s'" % date_now)
            # 调用JS直接给日期赋值
            d.find_element_by_id('ROUTE').send_keys('TEBAK')  # 录入航路
            time.sleep(1)

            d.find_element_by_xpath('//*[@id="PlanTab"]/div/table/tbody/tr[1]/td[13]/button[1]').click()  # save
            d.find_element_by_xpath('/html/body/div[23]/div/div/div[2]/button').click()  # 点击OK

            d.find_element_by_id('btn_SubmitApply').click()  # submit

            try:
                d.find_element_by_xpath('/html/body/div[23]/div/div/div[2]/button[2]').click()  # 点击确定
                time.sleep(1)
                d.find_element_by_xpath('/html/body/div[23]/div/div/div[2]/button').click()
            except:
                d.find_element_by_xpath('/html/body/div[23]/div/div/div[3]/button').click()  # 判断是否需要上传附件
                d.find_element_by_xpath('//*[@id="div_plancontent"]/div/div/div/span[1]').click()
                time.sleep(1)
                d.find_element_by_xpath(
                    '//*[@id="handerModal"]/div/div/div[2]/ul[1]/li[2]/div/div[3]/div[2]/div').click()
                time.sleep(1)
                m.click(1000, 660)
                m.click(1000, 660)
                time.sleep(1)
                d.find_element_by_xpath(
                    '//*[@id="handerModal"]/div/div/div[2]/ul[1]/li[2]/div/div[3]/div[2]/a' % i).click()  # 点击upload
                d.find_element_by_id('btn_SaveInfo').click()  # 点击保存
                d.find_element_by_xpath('/html/body/div[24]/div/div/div[2]/button').click()

            d.switch_to.default_content()  # 跳出iframe

        except Exception as e:
            print(f'异常:{e}')
            tb = sys.exc_info()[2]
            traceback.print_exception(e.__class__, e, tb)
        d.switch_to.default_content()


def new_chg_plan_nextday(d, plan_count):
    try:
        d.find_element_by_xpath('//*[@id="div_content"]/div[4]/div/div[1]').click()
        # 点击国内公务机
    except Exception as e:
        print(f'异常:{e}')

    for i in range(plan_count):
        try:
            try:
                d.switch_to.default_content()  # 跳出iframe
                d.find_element_by_xpath('//*[@id="myTab"]/li[2]').click()  # 点击application List
            except:pass

            try:
                d.switch_to.frame('HomeContent')  # 进入iframe
            except:
                pass
            d.find_element_by_id('btn_cng').click()  # 点击ADD
            time.sleep(1)
            d.find_element_by_xpath('//*[@id="btn_select"]').click()  # 点击选择
            d.find_element_by_xpath('//*[@id="myReply"]/div/div/div[2]/div/div/div[1]/form/div[2]/span/span').click()  # 输入注册号
            d.find_element_by_id('_easyui_combobox_i11_1').click()
            d.find_element_by_id('btnSearchreplay').click()  # 点击查询
            d.find_element_by_xpath('//*[@id="ShowTab"]/tbody/tr[1]/td[1]/input').click()  # 点击选框
            d.find_element_by_id('btn_copy').click()
            d.find_element_by_id('ROUTE_R').send_keys('TEBAK')  # 录入航路

            d.find_element_by_xpath('//*[@id="PlanTab"]/div/table/tbody/tr[8]/td[13]/button[1]').click()
            d.find_element_by_xpath('/html/body/div[24]/div/div/div[2]/button').click()  # 保存确定
            time.sleep(1)
            d.find_element_by_id('btn_SubmitApply').click()  # submit

            try:
                d.find_element_by_xpath('/html/body/div[24]/div/div/div[2]/button[2]').click()  # 点击确定
                time.sleep(1)
                d.find_element_by_xpath('/html/body/div[24]/div/div/div[2]/button').click()
            except:
                d.find_element_by_xpath('/html/body/div[23]/div/div/div[3]/button').click()  # 判断是否需要上传附件
                d.find_element_by_xpath('//*[@id="div_plancontent"]/div/div/div/span[1]').click()
                time.sleep(1)
                d.find_element_by_xpath(
                    '//*[@id="handerModal"]/div/div/div[2]/ul[1]/li[2]/div/div[3]/div[2]/div').click()
                time.sleep(1)
                m.click(1000, 660)
                m.click(1000, 660)
                time.sleep(1)
                d.find_element_by_xpath(
                    '//*[@id="handerModal"]/div/div/div[2]/ul[1]/li[2]/div/div[3]/div[2]/a' % i).click()  # 点击upload
                d.find_element_by_id('btn_SaveInfo').click()  # 点击保存
                d.find_element_by_xpath('/html/body/div[24]/div/div/div[2]/button').click()

            d.switch_to.default_content()  # 跳出iframe

        except Exception as e:
            print(f'异常:{e}')
            tb = sys.exc_info()[2]
            traceback.print_exception(e.__class__, e, tb)
        d.switch_to.default_content()

