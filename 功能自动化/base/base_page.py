"""基础层：存放selenium原生方法"""
from selenium import webdriver


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    # 定位元素的关键字
    def locater_element(self, loc):
        print(loc)
        return self.driver.find_element(*loc)


    # 输入的关键字
    def send_keys(self, loc, value):
        self.locater_element(loc).send_keys(value)


    # 点击的关键字
    def click(self, loc):
        self.locater_element(loc).click()






