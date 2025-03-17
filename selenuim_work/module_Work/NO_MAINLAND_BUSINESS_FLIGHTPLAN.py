# @Time : 2025/2/8 10:25
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
        d.find_element_by_xpath('//*[@id="div_content"]/div[2]/div/div[1]').click()
        # 点击国外公务机
        d.find_element_by_id('NoticeDetermine').click()  # 勾选同意
        d.find_element_by_xpath('//*[@id="NoticeBtn"]').click()  # 点击确认

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
            d.find_element_by_id('btn_Create').click()  # 点击ADD
            time.sleep(1)
            d.find_element_by_xpath('//*[@id="base_tb"]/tbody/tr[3]/td[2]/div/div/span/span').click()  # 点击注册号下拉框
            try:
                d.find_element_by_id('_easyui_combobox_i18_1').click()  # 点击选项
            except:
                d.find_element_by_id('_easyui_combobox_i18_2').click()  # 点击选项

            d.find_element_by_xpath('/html/body/div[28]/div/div/div[2]/button[2]').click()  # 点击OK
            d.find_element_by_xpath('//*[@id="btn_Next"]').click()  # 点击NEXT
            time.sleep(1)
            k.press_key(k.enter_key)
            k.release_key(k.enter_key)
            d.find_element_by_xpath('//*[@id="btn_Next"]').click()  # 点击NEXT
            time.sleep(1)
            k.press_key(k.enter_key)
            k.release_key(k.enter_key)

            d.find_element_by_id('FLIGHTID').send_keys(random.randint(100, 10000))  # 输入航班号

            d.find_element_by_xpath('//*[@id="add_tb"]/tbody/tr[1]/td[3]/span').click()  # 点击类型下拉框
            d.find_element_by_xpath('//*[@id="add_tb"]/tbody/tr[1]/td[3]/span/span').click()
            try:
                d.find_element_by_id('_easyui_combobox_i12_0').click()  # 点击选项
            except:
                d.find_element_by_id('_easyui_combobox_i12_1').click()  # 点击选项

            d.find_element_by_xpath('//*[@id="add_tb"]/tbody/tr[1]/td[4]/span/span').click()  # 点击起飞机场下拉框
            d.find_element_by_id('_easyui_combobox_i1_0').click()  # 选择机场
            d.find_element_by_id('DEPTIME').send_keys('0%s00' % random.randint(1, 9))  # 起飞时间
            d.find_element_by_id('ARRTIME').send_keys('%s00' % random.randint(10, 23))  # 降落时间

            d.find_element_by_xpath('//*[@id="add_tb"]/tbody/tr[1]/td[7]/span/span').click()  # 点击降落机场下拉框

            d.find_element_by_id('_easyui_combobox_i2_%s' % random.randint(42, 600)).click()  # 点击选择降落机场

            d.execute_script("document.getElementById('EDATE_EN').value = '%sAPR25'" % random.randint(10, 30))
            # 调用JS直接给日期赋值
            d.find_element_by_id('POINT').send_keys('TEBAK')  # 入境点
            d.find_element_by_id('ROUTE').send_keys('TEBAK')  # 录入航路
            time.sleep(1)
            for i in range(0, 4):
                d.find_element_by_xpath('//*[@id="td%s_ATTACHMENT"]/div/div[3]/div[2]/div' % i).click()
                time.sleep(1)
                m.click(1000, 660)
                m.click(1000, 660)
                time.sleep(1)
                d.find_element_by_xpath('//*[@id="td%s_ATTACHMENT"]/div/div[3]/div[2]/a' % i).click()  # 点击upload
            time.sleep(1)
            d.find_element_by_xpath('//*[@id="add_tb"]/tbody/tr[1]/td[12]/button[1]').click()  # save
            d.find_element_by_xpath('/html/body/div[29]/div/div/div[2]/button').click()  # 点击OK

            d.find_element_by_id('FLIGHTID').send_keys(random.randint(100, 10000))  # 输入航班号
            try:
                d.find_element_by_xpath('//*[@id="add_tb"]/tbody/tr[1]/td[3]/span').click()  # 点击类型下拉框
            except:
                d.find_element_by_xpath('//*[@id="add_tb"]/tbody/tr[1]/td[3]/span/span').click()
            try:
                d.find_element_by_id('_easyui_combobox_i12_0').click()  # 点击选项
            except:
                d.find_element_by_id('_easyui_combobox_i12_1').click()  # 点击选项

            d.find_element_by_xpath('//*[@id="add_tb"]/tbody/tr[1]/td[4]/span/span').click()  # 点击起飞机场下拉框
            d.find_element_by_id('_easyui_combobox_i1_%s' % random.randint(766, 989)).click()
            d.find_element_by_id('DEPTIME').send_keys('0%s00' % random.randint(1, 9))  # 起飞时间
            d.find_element_by_id('ARRTIME').send_keys('%s00' % random.randint(10, 23))  # 降落时间

            d.find_element_by_xpath('//*[@id="add_tb"]/tbody/tr[1]/td[7]/span/span').click()  # 点击降落机场下拉框
            d.find_element_by_id('_easyui_combobox_i2_0').click()  # 选择机场
            d.execute_script("document.getElementById('EDATE_EN').value = '%sAPR25'" % random.randint(10, 30))
            # 调用JS直接给日期赋值
            d.find_element_by_id('POINT').send_keys('TEBAK')  # 入境点
            d.find_element_by_id('ROUTE').send_keys('TEBAK')  # 录入航路
            time.sleep(1)
            for i in range(0, 4):
                d.find_element_by_xpath('//*[@id="td%s_ATTACHMENT"]/div/div[3]/div[2]/div' % i).click()
                time.sleep(1)
                m.click(1000, 660)
                m.click(1000, 660)
                time.sleep(1)
                d.find_element_by_xpath('//*[@id="td%s_ATTACHMENT"]/div/div[3]/div[2]/a' % i).click()  # 点击upload
            time.sleep(1)
            d.find_element_by_xpath('//*[@id="add_tb"]/tbody/tr[1]/td[12]/button[1]').click()  # save
            d.find_element_by_xpath('/html/body/div[29]/div/div/div[2]/button').click()  # 点击OK
            try:
                d.find_element_by_xpath('//*[@id="btn_Submit"]').click()  # submit
            except:
                d.find_element_by_id('btn_Submit').click()
            time.sleep(1)
            d.find_element_by_id('APPLY_CITY').send_keys('北京')
            d.find_element_by_id('APPLY_GROUPNAME').send_keys('民航')

            d.find_element_by_id('APPLY_GROUP_PERSONNAME').send_keys('陈世美')

            d.find_element_by_id('APPLY_GROUP_PERSONNATIONALITY').send_keys('中国')

            d.find_element_by_id('APPLY_GROUP_PERSONJOB').send_keys('测试工程师')

            d.find_element_by_id('APPLY_GROUP_PERSONNUM').send_keys('6')
            d.execute_script("document.getElementById('APPLY_DATE').value = '%sMAR25'" % random.randint(10, 30))

            d.find_element_by_xpath('//*[@id="btn_endsubmit"]').click()

            d.find_element_by_xpath('/html/body/div[29]/div/div/div[2]/button').click()

            d.switch_to.default_content()  # 跳出iframe

        except Exception as e:
            print(f'异常:{e}')
            tb = sys.exc_info()[2]
            traceback.print_exception(e.__class__, e, tb)
        d.switch_to.default_content()


def new_add_plan_today(d, plan_count):
    try:
        d.find_element_by_xpath('//*[@id="div_content"]/div[2]/div/div[1]').click()
        # 点击国外公务机
        d.find_element_by_id('NoticeDetermine').click()  # 勾选同意
        d.find_element_by_xpath('//*[@id="NoticeBtn"]').click()  # 点击确认

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
            d.find_element_by_id('btn_Create').click()  # 点击ADD
            time.sleep(1)
            d.find_element_by_xpath('//*[@id="base_tb"]/tbody/tr[3]/td[2]/div/div/span/span').click()  # 点击注册号下拉框
            try:
                d.find_element_by_id('_easyui_combobox_i18_1').click()  # 点击选项
            except:
                d.find_element_by_id('_easyui_combobox_i18_2').click()  # 点击选项

            d.find_element_by_xpath('/html/body/div[28]/div/div/div[2]/button[2]').click()  # 点击OK
            d.find_element_by_xpath('//*[@id="btn_Next"]').click()  # 点击NEXT
            time.sleep(1)
            k.press_key(k.enter_key)
            k.release_key(k.enter_key)
            d.find_element_by_xpath('//*[@id="btn_Next"]').click()  # 点击NEXT
            time.sleep(1)
            k.press_key(k.enter_key)
            k.release_key(k.enter_key)

            d.find_element_by_id('FLIGHTID').send_keys(random.randint(100, 10000))  # 输入航班号

            d.find_element_by_xpath('//*[@id="add_tb"]/tbody/tr[1]/td[3]/span').click()  # 点击类型下拉框
            d.find_element_by_xpath('//*[@id="add_tb"]/tbody/tr[1]/td[3]/span/span').click()
            try:
                d.find_element_by_id('_easyui_combobox_i12_0').click()  # 点击选项
            except:
                d.find_element_by_id('_easyui_combobox_i12_1').click()  # 点击选项

            d.find_element_by_xpath('//*[@id="add_tb"]/tbody/tr[1]/td[4]/span/span').click()  # 点击起飞机场下拉框
            d.find_element_by_id('_easyui_combobox_i1_%s' % random.randint(42, 600)).click()  # 选择机场
            d.find_element_by_id('DEPTIME').send_keys('0%s00' % random.randint(1, 9))  # 起飞时间
            d.find_element_by_id('ARRTIME').send_keys('%s00' % random.randint(10, 16))  # 降落时间

            d.find_element_by_xpath('//*[@id="add_tb"]/tbody/tr[1]/td[7]/span/span').click()  # 点击降落机场下拉框

            d.find_element_by_id('_easyui_combobox_i2_%s' % random.randint(766, 999)).click()  # 点击选择降落机场

            # 获取当天日期
            mouth = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
            now = time.strftime("%d%m%Y", time.localtime())

            mou_ = int(now[2:4]) - 1
            day_ = now[0:2]
            year = now[6:]
            date_now = day_ + mouth[mou_] + year
            d.execute_script("document.getElementById('EDATE_EN').value = '%s'" % date_now)
            # 调用JS直接给日期赋值
            d.find_element_by_id('POINT').send_keys('TEBAK')  # 入境点
            d.find_element_by_id('ROUTE').send_keys('TEBAK')  # 录入航路
            time.sleep(1)
            try:
                for i in range(0, 4):
                    d.find_element_by_xpath('//*[@id="td%s_ATTACHMENT"]/div/div[3]/div[2]/div' % i).click()
                    time.sleep(1)
                    m.click(1000, 660)
                    m.click(1000, 660)
                    time.sleep(1)
                    d.find_element_by_xpath('//*[@id="td%s_ATTACHMENT"]/div/div[3]/div[2]/a' % i).click()  # 点击upload
            except:pass
            time.sleep(1)
            d.find_element_by_xpath('//*[@id="add_tb"]/tbody/tr[1]/td[12]/button[1]').click()  # save
            try:
                d.find_element_by_xpath('/html/body/div[29]/div/div/div[2]/button').click()  # 点击OK
            except:continue
            try:
                d.find_element_by_xpath('//*[@id="btn_Submit"]').click()  # submit
            except:
                d.find_element_by_id('btn_Submit').click()

            time.sleep(1)
            d.find_element_by_id('APPLY_CITY').send_keys('北京')
            d.find_element_by_id('APPLY_GROUPNAME').send_keys('民航')

            d.find_element_by_id('APPLY_GROUP_PERSONNAME').send_keys('陈世美')

            d.find_element_by_id('APPLY_GROUP_PERSONNATIONALITY').send_keys('中国')

            d.find_element_by_id('APPLY_GROUP_PERSONJOB').send_keys('测试工程师')

            d.find_element_by_id('APPLY_GROUP_PERSONNUM').send_keys('6')
            d.execute_script("document.getElementById('APPLY_DATE').value = '%s'" % date_now)

            d.find_element_by_xpath('//*[@id="btn_endsubmit"]').click()

            d.find_element_by_xpath('/html/body/div[29]/div/div/div[2]/button').click()

            d.switch_to.default_content()  # 跳出iframe

        except Exception as e:
            print(f'异常:{e}')
            tb = sys.exc_info()[2]
            traceback.print_exception(e.__class__, e, tb)
        d.switch_to.default_content()