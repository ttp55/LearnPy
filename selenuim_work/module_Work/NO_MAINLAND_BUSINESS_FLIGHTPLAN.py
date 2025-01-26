# @Time : 2025/1/26 13:19
# @Author : WZG
# --coding:utf-8--
import random


def beian_shenpi(d):
    d.find_element_by_xpath('//*[@id="div_content"]/div[4]/div/div[1]').click()  # 点击国外公务机
    d.find_element_by_id('NoticeDetermine').click()
    d.find_element_by_id('NoticeBtn').click()  # 点击确定
    d.find_element_by_xpath('//*[@id="myTab"]/li[2]').click()  # 点击备案审批
    try:
        d.switch_to.frame('HomeContent')  # 进入iframe
    except:
        pass
    d.find_element_by_xpath('//*[@id="tb"]/thead/tr/th[1]/div[1]/input').click()  # 全选
    if random.randint(0, 1) == 0:
        d.find_element_by_id('btn_refuse').click()  # 点击同意
    else:
        d.find_element_by_id('btn_agree').click()
    d.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/button').click()  # 点击OK
    d.switch_to.default_content()  # 跳出iframe
    d.find_element_by_id('sbld').click()  # 点击logout