"""基础层：存放selenium原生方法"""
from typing import runtime_checkable
from selenium import webdriver


class BasePage:
    def __init__(self):
        # 配置全局变量
        global driver

        # 打开浏览器
        self.driver = webdriver.Chrome()

        # 赋值给driver
        driver = self.driver

        # 最大化界面
        self.driver.maximize_window()

        # 加载地址
        self.driver.get("http://t-admin.helitong.cn/login")


    def locater_element(self, loc):
        return self.driver.find_element(*loc)
