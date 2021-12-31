# coding = utf-8
"""创建商品"""
from time import sleep
from selenium import webdriver
from xlutils.copy import copy
from selenium.webdriver.common.by import By
import xlrd
import unittest
import pandas as pd
class Create_goods(unittest.TestCase):

    def setUp(self) -> None:

        global driver

        driver = webdriver.Chrome()

        driver.maximize_window()

        driver.get("http://t-admin.helitong.cn/login")
        sleep(5)

        # 登录

        driver.find_element(By.XPATH, "//input[@placeholder='请输入登录账号']").send_keys("13530600569")
        sleep(2)

        driver.find_element(By.XPATH, "//input[@placeholder='请输入登录密码']").send_keys("t123456")
        sleep(2)

        driver.find_element(By.XPATH, "//button[span='登录']").click()
        sleep(2)


    def test_Create_goods(self):
        i = 0
        while True:

            """读取excel信息"""
            # # 读取excel文件
            # data = xlrd.open_workbook("C:/Users/administered/Desktop/goods.xls")
            # # 通过索引获取工作表
            # sheet = data.sheet_by_index(0)
            # # 获取行数
            # sheet_nrows = sheet.nrows
            # i = 1
            # while i < sheet_nrows:
            #     list = []
            #     list.append(sheet.row_values(i))
            #     i += 1
            #     continue


            df = pd.read_excel('C:/Users/administered/Desktop/goods.xls')
            list = df.values
        


            """编辑基本信息"""
            # 点击商品管理
            driver.find_element(By.XPATH, "//div[span='商品管理']").click()
            sleep(2)

            # 重新加载创建商品页面
            driver.get("http://t-admin.helitong.cn/goods/creatGoods")
            sleep(5)

            # 类目
            driver.find_element(By.XPATH, "//form//div//span/span").click()
            sleep(2)

            # 一级类目
            driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[1]/div[1]/ul/li[15]").click()
            sleep(0.2)
            
            # 二级类目
            driver.find_element(By.XPATH, "//ul/li[span='户外']").click()
            sleep(0.2)
            
            # 三级类目
            driver.find_element(By.XPATH, "//ul/li[span='耳机']").click()
            sleep(0.2)
            
            # 分类
            driver.find_element(By.XPATH, "//form//div[2]//span/span").click()
            sleep(2)
            
            # 一级分类
            driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div/div[1]/ul/li[1]").click()
            sleep(0.2)
            
            # 二级分类
            driver.find_element(By.XPATH, "//ul/li[span='智能设备']").click()
            sleep(0.2)
            
            # 三级分类
            driver.find_element(By.XPATH, "//ul/li[span='智能机器人']").click()
            sleep(0.2)
            
            # 商品渠道
            driver.find_element(By.XPATH, "//form//div[3]//span/span").click()
            sleep(0.5)
            driver.find_element(By.XPATH, "//ul/li[span='自有']").click()
            sleep(0.2)
            
            # 品牌名称
            driver.find_element(By.XPATH, "//input[@placeholder='请输入品牌名称（无品牌请输入无）']").send_keys(list[i][0])
            sleep(1)
            
            # 商品名称
            driver.find_element(By.XPATH, "//input[@placeholder='请输入商品名称']").send_keys(list[i][1])
            sleep(1)
            
            # 商品六九码
            driver.find_element(By.XPATH, "//input[@placeholder='请输入商品六九码']").send_keys(list[i][2])
            sleep(1)
            
            # 商品单位
            driver.find_element(By.XPATH, "//input[@placeholder='请输入商品单位，如：件、个、台...']").send_keys(list[i][3])
            sleep(1)
            
            # 发货地址
            driver.find_element(By.XPATH, "//input[@placeholder='请输入发货地址']").send_keys(list[i][4])
            sleep(1)
            
            # 商品图片
            driver.find_element(By.NAME, "file").send_keys("C:/Users/administered/Desktop/images/吹风机/1.jpg")
            sleep(8)
            
            # 下一步
            driver.find_element(By.XPATH, "//*[span='下一步']").click()
            sleep(1)


            """编辑商品详情"""
            # 详情图
            driver.find_element(By.XPATH, "//*[p='图片上传:']//input").send_keys("C:/Users/administered/Desktop/images/吹风机/吹风机.jpg")
            sleep(10)

            # 下一步
            driver.find_element(By.XPATH, "//div[@class='form_button']/following::button[4]").click()
            sleep(1)


            """编辑价格库存"""
            # 规格名片
            driver.find_element(By.XPATH, '//input[@placeholder="请输入规格名片"]').send_keys("容量")
            sleep(2)

            # 点击按钮
            driver.find_element(By.XPATH, '//*[span="添加规格名"]').click()
            sleep(2)

            #输入规格值
            driver.find_element(By.XPATH, '//input[@placeholder="请输入规格值"]').send_keys("2L")
            sleep(0.5)

            # 点击按钮
            driver.find_element(By.XPATH, '//*[span="添加规格值"]').click()
            sleep(2)

            # 点击展示图片
            driver.find_element(By.XPATH, '//*[span="关闭"]').click()
            sleep(1)

            # 添加图片
            driver.find_element(By.XPATH, '//div[@class="img_con"]/following::input[5]').send_keys("C:/Users/administered/Desktop/images/吹风机/2.jpg")
            sleep(5)

            # 规格明细
            # 市场价
            driver.find_element(By.XPATH, '//input[@placeholder="请输入市场价"]').send_keys(list[i][5])
            sleep(1)

            # 销售价
            driver.find_element(By.XPATH, '//input[@placeholder="请输入销售价"]').send_keys(list[i][6])
            sleep(1)

            # 供货价
            driver.find_element(By.XPATH, '//input[@placeholder="请输入供货价"]').send_keys(list[i][7])
            sleep(1)

            # 结算价
            driver.find_element(By.XPATH, '//input[@placeholder="请输入结算价"]').send_keys(list[i][8])
            sleep(1)

            # 集采价
            driver.find_element(By.XPATH, '//input[@placeholder="请输入集采价"]').send_keys(list[i][9])
            sleep(1)

            # 集采结算价
            driver.find_element(By.XPATH, '//input[@placeholder="请输入集采结算价"]').send_keys(list[i][10])
            sleep(1)
            
            # 库存
            driver.find_element(By.XPATH, '//input[@placeholder="请输入库存"]').send_keys("100")
            sleep(1)

            # 点击确定
            driver.find_element(By.XPATH, '//button[span="确定"]').click()
            sleep(2)

            # 输入已售件数
            driver.find_element(By.XPATH, '//input[@placeholder="请输入已售件数"]').send_keys("0")
            sleep(0.8)

            # 输入集采量
            driver.find_element(By.XPATH, '//input[@placeholder="请输入集采量"]').send_keys("10")
            sleep(0.8)

            #点击有售后
            driver.find_element(By.XPATH, '//*[@class="el-radio__inner"]').click()
            sleep(2)

            # 点击换货
            driver.find_element(By.XPATH, '//span[@class="el-checkbox__inner"]').click()
            sleep(0.5)

            # 点击退货
            driver.find_element(By.XPATH, '//input[@value="退货"]/preceding-sibling::span').click()
            sleep(0.5)

            # 点击上架
            driver.find_element(By.XPATH, '//button[span="上架"]').click()
            sleep(5)
            i += 1


    # 运行完退出浏览器
    def tearDown(self) -> None:
        driver.quit()

# 执行main方法
if __name__ == "__main__":
    unittest.main()