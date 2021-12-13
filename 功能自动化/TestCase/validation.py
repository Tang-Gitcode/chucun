from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver import ActionChains
import time
import unittest

class validation(unittest.TestCase):

    def test_validation(self):

        global driver

        driver = webdriver.Chrome()

        driver.maximize_window()

        driver.get("http://ua-shop436.helitong.in/#/AccountLogin")
        time.sleep(5)

        """登录"""
        # 账号
        driver.find_element(By.XPATH, "//input[@placeholder='请输入登录账号']").send_keys("13017167459")
        time.sleep(1)
        # 输入密码
        driver.find_element(By.NAME, "password").send_keys("t123456")
        time.sleep(1)

        # 滑动验证
        button = driver.find_element(By.XPATH, "//div[@class='button']")
        ActionChains(driver).drag_and_drop_by_offset(button,300,0).perform()
        time.sleep(2)

        # 点击登录
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(2)

if __name__ == "__main__":
    unittest.main()