# 京东商品下单

import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


class TestJD(unittest.TestCase):

    def test_jdDoods(self):
        # 全局配置
        global driver

        # 加载浏览器
        driver = webdriver.Chrome()

        # 窗口最大化
        driver.maximize_window()

        # 加载地址
        # driver.get("http://t-mintegral437.helitong.cn/#/Login")
        driver.get("http://t-mintegral437.helitong.cn/#/ShoppingCart")
        # 等待时间
        sleep(2)

        driver.find_element(By.XPATH, "//div[@role='checkbox']/following::div[5]").click()
        sleep(2)

        """登录"""
        #输入账号
        # driver.find_element(By.NAME, "mobile").send_keys("13017167459")
        driver.find_element(By.XPATH, "//input[@placeholder='请输入手机号']").send_keys("13017167459")
        sleep(1)
        # 输入密码
        # driver.find_element(By.NAME, "password").send_keys("t123456")
        driver.find_element(By.XPATH, "//input[@placeholder='请输入账号密码']").send_keys("t123456")
        sleep(1)
        # 点击登录
        driver.find_element(By.XPATH, "//div[@class='van-button__text']").click()
        sleep(2)