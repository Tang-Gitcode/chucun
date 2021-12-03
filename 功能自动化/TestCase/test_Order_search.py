# 测试订单搜索
from 功能自动化.PageObject.Order_Management_page import OrderManagementpage
from selenium import webdriver
import unittest


class OrderSearch(unittest.TestCase):

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




    def test_Order_search(self):

        """搜索三方订单"""
        # 三方订单
        omp = OrderManagementpage(self.driver)
        omp.Three_Order()


        def tearDown(self) -> None:
            pass


        # 关闭浏览器
        driver.close()



