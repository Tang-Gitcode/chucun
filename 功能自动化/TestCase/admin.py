"""待发货取消订单"""


from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
class Goods(unittest.TestCase):

    def setUp(self) -> None:

        global driver

        driver = webdriver.Chrome()

        driver.maximize_window()

        driver.get("https://admin-console.helixinxuan.com/login")
        sleep(5)

        # 登录

        driver.find_element(By.XPATH, "//input[@placeholder='请输入登录账号']").send_keys("13017167459")
        sleep(2)

        driver.find_element(By.XPATH, "//input[@placeholder='请输入登录密码']").send_keys("t201518")
        sleep(2)

        driver.find_element(By.XPATH, "//button[span='登录']").click()
        sleep(2)


    def test_admin_goods(self):

        # 点击商品管理
        driver.find_element(By.XPATH, "//div[span='订单管理']").click()
        sleep(2)

        # 点击全部订单
        driver.find_element(By.XPATH, "//li[span='全部订单']").click()
        sleep(2)

        # 订单搜索
        driver.find_element(By.XPATH, "//input[@type='text']").click()
        sleep(1)
        driver.find_element(By.XPATH, "//li[span='下单人手机号']").click()
        sleep(1)
        driver.find_element(By.XPATH, "//input[@placeholder='请输入']").send_keys("13017167459")
        sleep(1)

        # 订单状态
        driver.find_element(By.XPATH, "//input[@placeholder='请选择订单状态']").click
        sleep(1)
        driver.find_element(By.XPATH, "//li[span='待发货']/following::li[123]").click
        sleep(2)

        while True:

            # 搜索
            driver.find_element(By.XPATH, "//button[span='搜索']").click
            sleep(5)

            #订单详情
            driver.find_element(By.XPATH, "//button[span='订单详情']").click
            sleep(5)

            # 取消订单
            driver.find_element(By.XPATH, "//button[span='取消订单']").click
            sleep(2)

            # 返回上一个窗口
            self.driver.window_handles[0]
            sleep(2)

    def tearDown(self) -> None:
        driver.quit()

if __name__ == "__main__":
    unittest.main()

