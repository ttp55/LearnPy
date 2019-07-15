# @time:  2019/7/4 10:36
# @author: WZG
# encoding: utf-8

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


class PyTest(object):
    def __init__(self, browser):
        self.browser = browser
        if self.browser == 'firefox' or self.browser == 'Firefox':
            driver = webdriver.Firefox()
        elif self.browser == 'chrome' or self.browser == 'Chrome':
            driver = webdriver.Chrome()
        else:
            print('Please input firefox Firefox chrome Chrome')
        self.driver = driver

    def element(self, fangfa, dingwei):
        if fangfa == 'id':
            element = self.driver.find_element_by_id(dingwei)
        elif fangfa == 'name':
            element = self.driver.find_element_by_name(dingwei)
        elif fangfa == 'class':
            element = self.driver.find_element_by_class_name(dingwei)
        elif fangfa == "link_text":
            element = self.driver.find_element_by_link_text(dingwei)
        elif fangfa == "xpath":
            element = self.driver.find_element_by_xpath(dingwei)
        elif fangfa == "tag":
            element = self.driver.find_element_by_tag_name(dingwei)
        elif fangfa == "css":
            element = self.driver.find_element_by_css_selector(dingwei)
        else:
            raise NameError("Please enter the elements,'id','name','class','link_text','xpath','css','tag'.")
        return element

    def open(self, url):
        self.driver.get(url)

    def make_maxwindow(self):
        self.driver.maximize_window()

    def send_key(self, fangfa, dingwei, text):
        self.element(fangfa, dingwei)
        e1 = self.element(fangfa, dingwei)
        e1.clear()
        e1.send_keys(text)

    def click_(self, fangfa, dingwei):
        e1 = self.element(fangfa, dingwei)
        e1.click()

    def cli_text(self, text):
        self.driver.find_element_by_link_text(text).click()

    def waiting(self, times):
        self.driver.implicitly_wait(times)

    def right_click(self, fangfa, dingwei):
        e1 = self.element(fangfa, dingwei)
        ActionChains(self.driver).context_click(e1).perform()

    def get_url(self):
        return self.driver.current_url
