from selenium import webdriver
import time
from selenium.webdriver.common.by import By


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
driver.find_element(By.XPATH,
                    "/html/body/div[1]/div/div[2]/div[2]/div[2]/div/div/div/div[1]/div/div[2]/div/form/div["
                    "1]/div/div/div").click()
time.sleep(2)
driver.find_element('/html/body/div[3]/div[1]/div[1]/div[1]/ul/li[1]').click()
time.sleep(2)
driver.find_element(By.XPATH, "//ul/li[span='户外']").click()
time.sleep(0.2)
driver.find_element(By.XPATH, "//ul/li[span='耳机']").click()
time.sleep(0.2)
driver.find_element(By.XPATH, "//div/i[@class='el-icon-plus']").send_keys(
    "C:/Users/administered/Desktop/缺陷图片/11.29/1.png")
time.sleep(5)