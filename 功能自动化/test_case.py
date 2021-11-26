from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest



# 定义测试类
class TestCase(unittest.TestCase):

    # 定义测试方法
    def test_01_login(self):
        # 配置全局变量
        global driver
        # 打开浏览器
        driver = webdriver.Chrome()

        # 加载地址
        driver.get("https://www.baidu.com/")

        # 定位元素
        value = driver.find_element(By.ID, "kw").send_keys("selenium是什么？")
        # print(value)


    # def test_02_login(self):
    #     driver = webdriver.Chrome()

    #     driver.post("")


# 执行测试
if __name__ == '__main__':
    print("---------------------TestCase-----------------")
    unittest.main()


# print(value)