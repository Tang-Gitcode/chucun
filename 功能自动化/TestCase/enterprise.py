"""企业商城进商城"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import unittest

class enterprise(unittest.TestCase):
    def test_enterprise(self):
        global driver

        driver = webdriver.Chrome()

        driver.maximize_window()

        driver.get("http://t-enterprise.helitong.cn/login")
        time.sleep(2)
        try:
            """企业账号登录"""
            driver.find_element(By.XPATH, "//input[@placeholder='请输入登录账号']").send_keys("13017167459")
            time.sleep(1)
            driver.find_element(By.XPATH, "//input[@placeholder='请输入登录密码']").send_keys("t123456")
            time.sleep(1)        
            driver.find_element(By.XPATH, "//div[@class='el-form-item__content']/following::button[2]").click()
            time.sleep(3)


            """商城管理"""
            driver.find_element(By.XPATH, "//div[@class='el-submenu__title']").click()
            time.sleep(2)
            driver.find_element(By.XPATH, "//div[@class='el-submenu__title']/following::ul").click()
            time.sleep(2)
            driver.find_element(By.XPATH, "//input[@placeholder='商城查询']").send_keys("唐的企业积分商城")
            time.sleep(2)
            driver.find_element(By.XPATH, "//div[@class='storeManagement']//button").click()
            time.sleep(2)
            driver.find_element(By.XPATH, "//div[@class='btnBox']//button").click()
            time.sleep(5)
            # 获取句柄
            n = driver.window_handles

            # 切换到最新的页面
            driver.switch_to_window(n[-1])

            driver.find_elements(By.XPATH, "//div[@class='van-tabbar-item']")[2].click()
            time.sleep(5)

            while True:
                try:
                    """登录"""
                    # # 账号
                    # driver.find_element(By.XPATH, "//input[@placeholder='请输入登录账号']").send_keys("13017167459")
                    # time.sleep(1)
                    # # 输入密码
                    # driver.find_element(By.NAME, "password").send_keys("t123456")
                    # time.sleep(1)

                    # # 滑动验证
                    # button = driver.find_element(By.XPATH, "//div[@class='button']")
                    # ActionChains(driver).drag_and_drop_by_offset(button,300,0).perform()
                    # time.sleep(2)

                    # 手机验证码登录
                    driver.find_element(By.XPATH, "//div[@class='card_title']//span").click()
                    time.sleep(2)
                    driver.find_element(By.NAME, "mobile").send_keys("13017167459")
                    time.sleep(2)
                    driver.find_element(By.XPATH, "//div[@class='van-field__button']//span").click()
                    time.sleep(30)

                    # 点击登录
                    driver.find_element(By.XPATH, "//button[@type='submit']").click()
                    time.sleep(5)

                    # 点击商品
                    driver.find_elements(By.XPATH, "//div[@class='cap-goods__img']")[0].click()
                    time.sleep(3)
                except Exception as e:
                    print("登录失败：", e)
                    # 失败则刷新页面
                    driver.refresh()
                    time.sleep(2)
                else:
                    print("登录成功")
                    # 点击商品
                    driver.find_elements(By.XPATH, "//div[@class='cap-goods__img']")[0].click()
                    time.sleep(3)
                    break

        except Exception as e:
            print("运行失败：", e)
        else:
            print("运行成功！")

    def tearDown(self) -> None:
        driver.quit()

if __name__ == "__main__":
    unittest.main()