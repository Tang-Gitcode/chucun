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
        driver.get("http://t-mintegral437.helitong.cn/#/Login")
        # 等待时间
        sleep(5)


        """登录"""
        #输入账号
        driver.find_element(By.XPATH, "//input[@name='mobile']/following::input[2]").send_keys("13017167459")
        sleep(1)
        # 输入密码
        driver.find_element(By.NAME, "password").send_keys("t123456")
        sleep(1)
        # 点击登录
        driver.find_element(By.XPATH, "//button/following::div[10]").click()
        sleep(3)

        """购物车"""
        # 点击购物车
        driver.find_element(By.XPATH, "//div[@class='van-tabbar-item__text']/following::span[2]").click()
        sleep(1)
        # 点击第一个勾选框
        driver.find_element(By.XPATH, "//div[@role='checkbox']/following::div[4]").click()
        sleep(1)
        # 结算
        driver.find_element(By.XPATH, "//div[span=' 全选 ']/following::button").click()
        sleep(2)

        """结算页面"""
        # 选择使用积分
        driver.find_element(By.XPATH, "//div[span='去选择']").click()
        sleep(1)

        # 确认使用积分
        driver.find_element(By.XPATH, "//span[@class='allintegralcolor']/following::button").click()
        sleep(1)

        # 提交订单
        driver.find_element(By.XPATH, "//span[@class='allprice']/following::button").click()
        sleep(5)

        # 输入密码
        driver.find_element(By.XPATH, "//input[@class='password-code-input']").send_keys("201518")
        sleep(1)

        # 确认
        driver.find_element(By.XPATH, "//div[@class='buttons-bar']/button[2]").click()
        sleep(10)



    # 用例执行完关闭页面
    def tearDown(self) -> None:
        driver.close()