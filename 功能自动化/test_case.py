from pymysql.connections import SSL_ENABLED
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest



# 定义测试类
class TestCase(unittest.TestCase):

    # 定义测试方法
    def test_login(self):

        # 配置全局变量
        global driver

        # 打开浏览器
        driver = webdriver.Chrome()

        # 最大化界面
        driver.maximize_window()

        # 加载地址
        driver.get("http://t-admin.helitong.cn/login")

        """登录"""
        driver.find_element(By.XPATH, "//input[@placeholder='请输入登录账号']").send_keys("13530600569")
        time.sleep(0.2)
        driver.find_element(By.XPATH, "//input[@placeholder='请输入登录密码']").send_keys("t123456")
        time.sleep(0.2)
        driver.find_element(By.XPATH, "//button[span='登录']").click()
        time.sleep(1)

        # 关闭浏览器
        driver.close()



    # 定义测试方法
    def test_threeOrder(self):

        # 配置全局变量
        global driver

        # 打开浏览器
        driver = webdriver.Chrome()

        # 最大化界面
        driver.maximize_window()

        # 加载地址
        driver.get("http://t-admin.helitong.cn/login")

        """登录"""
        driver.find_element(By.XPATH, "//input[@placeholder='请输入登录账号']").send_keys("13530600569")
        time.sleep(0.2)
        driver.find_element(By.XPATH, "//input[@placeholder='请输入登录密码']").send_keys("t123456")
        time.sleep(0.2)
        driver.find_element(By.XPATH, "//button[span='登录']").click()
        time.sleep(1)


        """订单管理"""
        driver.find_element(By.XPATH, "//div[span='订单管理']").click()
        time.sleep(0.5)

        driver.find_element(By.XPATH, "//*[span='三方订单']").click()
        time.sleep(0.5)

        # 点击日期选择框
        driver.find_element(By.XPATH, "//input[@placeholder='开始日期']").click()
        # 等待时间
        time.sleep(1)
        
        # 选择三方时间
        driver.find_element(By.XPATH, '//tr[5]/td[7]').click()

        driver.find_element(By.XPATH, '//tr[5]/td[7]').click()

        # 确定时间
        driver.find_element(By.XPATH, '//div[@class="el-picker-panel__footer"]/button[2]').click()

        # 搜索
        driver.find_element(By.XPATH, '//div[@class="custom-form-btn"]/button').click()
        time.sleep(0.5)   

        # 关闭浏览器
        driver.close()

    def test_goods(self):
        driver = webdriver.Chrome()

        driver.get("http://t-admin.helitong.cn/login")
        
        driver.maximize_window()

        driver.find_element(By.XPATH, "//input[@placeholder='请输入登录账号']").send_keys("13530600569")
        driver.find_element(By.XPATH, "//input[@placeholder='请输入登录密码']").send_keys("t123456")
        driver.find_element(By.XPATH, '//button[span="登录"]').click()
        time.sleep(2)

        """创建商品"""
        driver.find_element(By.XPATH, "//div[span='商品管理']").click()
        time.sleep(2)
        driver.get("http://t-admin.helitong.cn/goods/creatGoods")
        time.sleep(1)
        # driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[1]/div/div[1]/div/div/ul/li[3]/ul/li[1]").click()
        # time.sleep(5)
        driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[2]/div/div/div/div[1]/div/div[2]/div/form/div[1]/div/div/div").click()
        time.sleep(2)
        driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[1]/div[1]/ul/li[1]').click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//ul/li[span='户外']").click()
        time.sleep(0.2)
        driver.find_element(By.XPATH, "//ul/li[span='耳机']").click()
        time.sleep(5)
        driver.find_element(By.XPATH, "//div/i[@class='el-icon-plus']").click()
        time.sleep(5)

# 执行测试
if __name__ == '__main__':
    print("---------------------TestCase-----------------")
    unittest.main()

