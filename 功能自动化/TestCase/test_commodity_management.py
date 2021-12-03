# 测试商品管理
import unittest
from selenium import webdriver
from 功能自动化.PageObject.Goods_Management_page import GoodsManagementpage


# 定义测试类
class TestCommodityManagement(unittest.TestCase):

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


    # 定义创建商品的方法

    def test_goods(self):
        gmt = GoodsManagementpage(self.driver)
        gmt.Create_Goods()
        

    def tearDown(self) -> None:
        pass

        # 关闭浏览器
        driver.close()


