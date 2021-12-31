"""商城京东商品仓库中上架"""


from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
class Create_goods(unittest.TestCase):

    def setUp(self) -> None:

        global driver

        driver = webdriver.Chrome()

        driver.maximize_window()

        driver.get("https://channel-console.helixinxuan.com/login")
        sleep(5)


    def test_Create_goods(self):

        # 登录经销商系统

        driver.find_element(By.XPATH, "//input[@placeholder='请输入登录账号']").send_keys("京西良品")
        sleep(2)

        driver.find_element(By.XPATH, "//input[@placeholder='请输入登录密码']").send_keys("jxlp123456")
        sleep(2)

        driver.find_element(By.XPATH, "//button[span='登录']").click()
        sleep(2)

        """商城管理"""
        driver.find_element(By.XPATH, "//div[span='商城应用']").click()
        sleep(2)
        driver.find_element(By.XPATH, "//li[span='商城管理']").click()
        sleep(2)
        driver.find_element(By.XPATH, "//input[@placeholder='商城查询']").send_keys("京西良品优选")
        sleep(2)
        driver.find_element(By.XPATH, "//button[@type='button']/following::button[2]").click()
        sleep(2)
        driver.find_element(By.XPATH, "//button[@type='button']/following::button[5]").click()
        sleep(10)

        # 切换窗口
        #  获取所有窗口的句柄
        handles = driver.window_handles
        driver.switch_to.window(handles[1])

        """商城后台"""
        driver.find_element(By.XPATH, "//div[span='商品管理']").click()
        sleep(2)
        driver.find_element(By.XPATH, "//li[span='商品管理']").click()
        sleep(2)
        # 仓库中
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
        sleep(3)

        # 选择全选本页
        driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[2]/div/div/div/div/div[1]/div/div[2]/div/div[2]/div[4]/div[1]/table/thead/tr/th[1]/div/label/span").click()
        sleep(2)

        # 点击批量上架
        driver.find_element(By.XPATH, "//button[@type='button']/following::button[3]").click()
        sleep(10)

        # 点击确定
        driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[2]/div/div/div/div/div[2]/div/div[3]/span/button").click()
        sleep(2)

        
        while True:
            # 跳转到页面底部
            driver.execute_script("var q=document.documentElement.scrollTop=10000")
            sleep(2)
            # element_click = True
            # try:
            #     driver.find_element(By.XPATH, "//button[@disabled='disabled']")
            # except:
            #     element_click = False
            # if element_click == False:
            #     # 点击翻页
            #     driver.find_element(By.XPATH, "//button[@class='btn-next']").click()
            #     sleep(4)

            #     # 跳转到页面顶部
            #     driver.execute_script("var q=document.documentElement.scrollTop=0")
            #     sleep(2)

            #     # # 选择全选本页
            #     # driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[2]/div/div/div/div/div[1]/div/div[2]/div/div[2]/div[4]/div[1]/table/thead/tr/th[1]/div/label/span").click()
            #     # sleep(1)
                
            #     # 选择全选本页
            #     driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[2]/div/div/div/div/div[1]/div/div[2]/div/div[2]/div[4]/div[1]/table/thead/tr/th[1]/div/label/span").click()
            #     sleep(1)

            #     # 点击批量上架
            #     driver.find_element(By.XPATH, "//button[@type='button']/following::button[3]").click()
            #     sleep(10)

            #     # 点击确定
            #     driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[2]/div/div/div/div/div[2]/div/div[3]/span/button").click()
            #     sleep(2)

            # else:

            #      # 选择第1页
            #     driver.find_element(By.XPATH, "//ul[@class='el-pager']/li").click()
            #     sleep(3)

            #     # 跳转到页面顶部
            #     driver.execute_script("var q=document.documentElement.scrollTop=0")
            #     sleep(2)

            #     # # 选择全选本页
            #     # driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[2]/div/div/div/div/div[1]/div/div[2]/div/div[2]/div[4]/div[1]/table/thead/tr/th[1]/div/label/span").click()
            #     # sleep(1)
                
            #     # 选择全选本页
            #     driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[2]/div/div/div/div/div[1]/div/div[2]/div/div[2]/div[4]/div[1]/table/thead/tr/th[1]/div/label/span").click()
            #     sleep(1)

            #     # 点击批量上架
            #     driver.find_element(By.XPATH, "//button[@type='button']/following::button[3]").click()
            #     sleep(10)

            #     # 点击确定
            #     driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[2]/div/div/div/div/div[2]/div/div[3]/span/button").click()
            #     sleep(2)
            # 点击翻页
            driver.find_element(By.XPATH, "//button[@class='btn-next']").click()
            sleep(4)

            # 跳转到页面顶部
            driver.execute_script("var q=document.documentElement.scrollTop=0")
            sleep(2)

            # # 选择全选本页
            # driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[2]/div/div/div/div/div[1]/div/div[2]/div/div[2]/div[4]/div[1]/table/thead/tr/th[1]/div/label/span").click()
            # sleep(1)
            
            # 选择全选本页
            driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[2]/div/div/div/div/div[1]/div/div[2]/div/div[2]/div[4]/div[1]/table/thead/tr/th[1]/div/label/span").click()
            sleep(1)

            # 点击批量上架
            driver.find_element(By.XPATH, "//button[@type='button']/following::button[3]").click()
            sleep(10)

            # 点击确定
            driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[2]/div/div/div/div/div[2]/div/div[3]/span/button").click()
            sleep(2)

    # def tearDown(self) -> None:
    #     driver.quit()

if __name__ == "__main__":
    unittest.main()