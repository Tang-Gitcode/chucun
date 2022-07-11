"""总系统京东商品仓库中上架"""


from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
class Create_goods(unittest.TestCase):

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


    def test_Create_goods(self):

        # 点击商品管理
        driver.find_element(By.XPATH, "//div[span='商品管理']").click()
        sleep(2)

        # 点击平台商品库
        driver.find_element(By.XPATH, "//li[span='平台商品库']").click()
        sleep(2)

        # 点击京东商品
        driver.find_element(By.ID, "tab-jd").click()
        sleep(2)

        # 点击仓库中
        driver.find_element(By.ID, "tab-3").click()
        sleep(2)

        # 跳转到页面底部
        driver.execute_script("var q=document.documentElement.scrollTop=10000")
        sleep(2)

        # 选择页码
        driver.find_element(By.XPATH, "//span[@class='el-pagination__sizes']//input").click()
        sleep(2)

        # 选择50条/页
        driver.find_element(By.XPATH, "//li[span='50条/页']").click()
        sleep(2)

        # 选择全部
        driver.find_element(By.XPATH, "//div[@class='el-form-item'][6]//span").click()
        sleep(2)
        driver.find_element(By.XPATH, "//li[@class='el-select-dropdown__item']/following::li[4]").click()
        sleep(2)

        # 选择全选本页
        driver.find_element(By.XPATH, "//label[span='全选本页']//span[2]").click()
        sleep(2)

        # 点击批量上架
        driver.find_element(By.XPATH, "//button[@type='button']/following::button[4]").click()
        sleep(12)

        # 点击确定
        driver.find_element(By.XPATH, "//span[@class='dialog-footer']/following::span[11]/button").click()
        sleep(5)

        
        while True:
            # 跳转到页面底部
            driver.execute_script("var q=document.documentElement.scrollTop=10000")
            sleep(2)
            element_click = True
            try:
                driver.find_element(By.XPATH, "//button[@disabled='disabled']")
            except:
                element_click = False
            if element_click == False:
                # 点击翻页
                driver.find_element(By.XPATH, "//button[@class='btn-next']").click()
                sleep(2)
                # 选择全选本页
                driver.find_element(By.XPATH, "//label[span='全选本页']//span[2]").click()
                sleep(2)

                # 选择全选本页
                driver.find_element(By.XPATH, "//label[span='全选本页']//span[2]").click()
                sleep(2)

                # 点击批量上架
                driver.find_element(By.XPATH, "//button[@type='button']/following::button[4]").click()
                sleep(12)

                # 点击确定
                driver.find_element(By.XPATH, "//span[@class='dialog-footer']/following::span[11]/button").click()
                sleep(5)

            else:

                 # 选择第i页
                driver.find_element(By.XPATH, "//li[@class='number']").click()
                sleep(3)

                # 选择全选本页
                driver.find_element(By.XPATH, "//label[span='全选本页']//span[2]").click()
                sleep(2)

                # 选择全选本页
                driver.find_element(By.XPATH, "//label[span='全选本页']//span[2]").click()
                sleep(2)

                # 点击批量上架
                driver.find_element(By.XPATH, "//button[@type='button']/following::button[4]").click()
                sleep(12)

                # 点击确定
                driver.find_element(By.XPATH, "//span[@class='dialog-footer']/following::span[11]/button").click()
                sleep(5)


    def tearDown(self) -> None:
        driver.quit()

if __name__ == "__main__":
    unittest.main()