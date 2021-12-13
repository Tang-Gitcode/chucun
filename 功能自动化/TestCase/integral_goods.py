"""积分商城下单"""

import time
import unittest
from unittest.main import main
from selenium import webdriver
from selenium.webdriver.common.by import By

class integral_Goods(unittest.TestCase):


    def setUp(self) -> None:

        # 设置全局变量
        global driver

        # 加载谷歌浏览器
        driver = webdriver.Chrome()

        # 窗口最大化
        driver.maximize_window()

        # 加载地址
        driver.get("http://t-mintegral437.helitong.cn/#/Login")
        # 等待时间
        time.sleep(5)


        """登录"""
        #输入账号
        driver.find_element(By.XPATH, "//input[@name='mobile']/following::input[2]").send_keys("13017167459")
        time.sleep(1)
        # 输入密码
        driver.find_element(By.NAME, "password").send_keys("t123456")
        time.sleep(1)
        # 点击登录
        driver.find_element(By.XPATH, "//button/following::div[10]").click()
        time.sleep(2)


    def test_integralGoods(self):
        try:
            i = 0
            while True:
                element_login = True
                try:
                    # 进入商品详情
                    driver.find_elements("//div[@class='cap-goods__image-wrap']")[i].click()
                    time.sleep(2)

                    # 点击立即购买
                    driver.find_elements("//div[@class='van-goods-action']//button").click()
                    time.sleep(2)

                    # 点击确认
                    driver.find_elements("//div[@class='van-sku-actions']//button").click()



                    """结算页面"""
                    # 选择使用积分
                    driver.find_element(By.XPATH, "//div[span='去选择']").click()
                    time.sleep(1)

                    # 确认使用积分
                    driver.find_element(By.XPATH, "//span[@class='allintegralcolor']/following::button").click()
                    time.sleep(1)

                    # 提交订单
                    driver.find_element(By.XPATH, "//span[@class='allprice']/following::button").click()
                    time.sleep(5)

                    # 输入密码
                    driver.find_element(By.XPATH, "//input[@class='password-code-input']").send_keys("201518")
                    time.sleep(1)

                    # 确认
                    driver.find_element(By.XPATH, "//div[@class='buttons-bar']/button[2]").click()
                    time.sleep(3)

                    element_click = True
                    try:
                        # 查看订单
                        driver.find_element(By.XPATH, "//div[@class='success']//button[2]").click()
                        time.sleep(1)

                        # 点击商品详情
                        driver.find_element(By.XPATH, "//div[span='待发货']/following::span[5]").click()
                        time.sleep(1)

                        # 获取订单详情
                        order_sn = driver.find_element(By.XPATH, "//div[@class='van-cell__value']/following::div[37]").text
                        goods_name = driver.find_element(By.XPATH, "//div[@class='van-card__content']//div/div").text
                        print(f"下单成功：订单编号：{order_sn}")
                        print(f"下单成功：商品名称：{goods_name}")

                    

                        # 返回上一步
                        driver.find_element(By.XPATH, " //div[@class='van-cell']").click()
                        time.sleep(1)

                        # 退回上一步
                        driver.back()
                                
                        """回到首页"""                
                        driver.find_element(By.XPATH, "//div[@class='success']//button").click()
                        time.sleep(2)
                        i += 1
                    except:
                        element_click = False
                    if element_click == False:
                        # 点击取消
                        driver.find_element(By.XPATH, " //div[@class='buttons-bar']//button").click()
                        time.sleep(2)

                        """获取商品名称"""
                        failure_goods = driver.find_element(By.XPATH, " //div[@class='van-card__content']//div/div").text
                        print(f"下单失败：\t商品名称：{failure_goods}")
                        time.sleep(2)

                        # 点击返回
                        driver.find_element(By.XPATH, " //div[@class='van-cell']").click()
                        time.sleep(3)
                        # 点击返回
                        driver.find_element(By.XPATH, " //div[@class='van-cell']").click()
                        time.sleep(3)
                        i += 1

                except:
                    element_login = False
                if element_login == False:
                    """登录"""
                    #输入账号
                    driver.find_element(By.XPATH, "//input[@name='mobile']/following::input[2]").send_keys("13017167459")
                    time.sleep(1)
                    # 输入密码
                    driver.find_element(By.NAME, "password").send_keys("t123456")
                    time.sleep(1)
                    # 点击登录
                    driver.find_element(By.XPATH, "//button/following::div[10]").click()
                    time.sleep(2)
                else:
                    continue
                print("运行成功")
        except Exception as e:
            print(f"运行失败{e}")

    def tearDown(self) -> None:
        driver.close()


if __name__ == "__main__":
    unittest.main()
