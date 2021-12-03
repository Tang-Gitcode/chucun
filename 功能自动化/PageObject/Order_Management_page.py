"""订单管理页"""
import time

from selenium.webdriver.common.by import By

from 功能自动化.PageObject.login_page import LoginPage
from 功能自动化.base.base_page import BasePage


class OrderManagementpage(BasePage):

    """三方订单的页面元素"""

    # 商品管理
    Good_list = (By.XPATH, "//div[span='订单管理']")

    # 三方订单
    Three_list = (By.XPATH, "//*[span='三方订单']")

    # 日期选择框
    data = (By.XPATH, "//input[@placeholder='开始日期']")

    #选择时间
    start_time = (By.XPATH, "//tr[2]/td[6]")

    end_time = (By.XPATH, "//tr[2]/td[6]")

    # 确定
    determine = (By.XPATH, "//div[@class='el-picker-panel__footer']/button[2]")

    # 搜索
    search = (By.XPATH, "//div[@class='custom-form-btn']/button")




    # 点击
    def Three_Order(self):

        # 登录
        lp = LoginPage(self.driver)
        lp.login_admin()

        time.sleep(2)

        # 订单管理
        self.click(OrderManagementpage.Good_list)
        time.sleep(2)

        # 三方订单
        self.click(OrderManagementpage.Three_list)
        time.sleep(2)

        # 三方时间
        self.click(OrderManagementpage.data)
        time.sleep(2)

        # 开始时间
        self.click(OrderManagementpage.start_time)
        time.sleep(2)

        # 结束时间
        self.click(OrderManagementpage.end_time)
        time.sleep(2)

        # 确定
        self.click(OrderManagementpage.determine)
        time.sleep(2)

        # 搜索
        self.click(OrderManagementpage.search)
        time.sleep(2)