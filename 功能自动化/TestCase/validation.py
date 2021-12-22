from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver import ActionChains
import time
import unittest

class validation(unittest.TestCase):

    def setUp(self) -> None:

        global driver

        driver = webdriver.Chrome()

        driver.maximize_window()

        driver.get("http://ua-shop437.helitong.in/#/Home")
        time.sleep(2)

        driver.refresh()
        time.sleep(2)

        driver.find_elements(By.XPATH, "//div[@class='van-tabbar-item__icon']")[3].click()
        time.sleep(3)

    def test_validation(self):
        i = 0
        while True:
            try:
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

                # 点击商品
                driver.find_elements(By.XPATH, "cap-goods__img")[i]
                time.sleep(3)

            except Exception as e:
                print("登录失败！", e)
                # 登陆失败刷新页面继续循环
                driver.refresh()

            else:
                print("登录成功！")

                # 点击商品
                driver.find_elements(By.XPATH, "cap-goods__img")[i]
                time.sleep(3)

                # 后退一步
                driver.back()
                i += 1


    def tearDown(self) -> None:
        driver.quit()

if __name__ == "__main__":
    unittest.main()