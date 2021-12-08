# 京东商品下单

from types import DynamicClassAttribute
import unittest
from unittest.main import main
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class TestJD(unittest.TestCase):

    def setUp(self) -> None:
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

    def test_jdDoods(self):
       
        while True:

            """购物车"""
            # 点击购物车
            driver.find_element(By.XPATH, "//div[@class='van-tabbar-item__text']/following::span[2]").click()
            sleep(1)
            """
            点击第一个勾选框
            判断是否存在元素
            默认存在
            """
            element_existance = True
            try:
                # 定位元素尝试点击
                driver.find_element(By.XPATH, "//div[@role='checkbox']/following::div[4]").click()
                sleep(1)
                # 没有定位到元素则抛出异常
            except:
                element_existance = False

            # 判断元素是否存在，不存在则跳出循环，存在则继续循环
            if element_existance == False:
                break
            else:                 
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
                # try:
                #     button = driver.find_element(By.XPATH, "//div[@class='buttons-bar']/button[2]").click()
                #     if button == True:
                #         # 取消
                #         driver.find_element(By.XPATH, "//div[@class='buttons-bar']//button").click()
                #         sleep(2)
                #     else:
                #         break
                # except:
                #     print("下单失败，请删除订单该订单并重新下单。")
                driver.find_element(By.XPATH, "//div[@class='buttons-bar']/button[2]").click()
                sleep(2)


                """回到首页"""
                driver.find_element(By.XPATH, "//div[@class='success']//button").click()
                sleep(2)





    # 用例执行完关闭页面
    def tearDown(self) -> None:
        driver.close()


if __name__ == "__main__":
    unittest.main()