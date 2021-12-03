# 测试登录

import  unittest

from selenium import webdriver

from 功能自动化.PageObject.login_page import LoginPage


class test_login(unittest.TestCase):

    def setUp(self) -> None:
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


    # 定义测试方法
    def test_login(self):

        """登录"""
        lp = LoginPage(self.driver)
        lp.login_admin()


        def tearDown(self) -> None:
            pass
        

        # 关闭浏览器
        driver.close()


