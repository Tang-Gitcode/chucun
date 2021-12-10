# 京东商品下单

from os import write
import time
from types import DynamicClassAttribute
import unittest
import openpyxl
import xlrd
import os.path
from unittest.main import main
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


class TestJD(unittest.TestCase):

    def setUp(self) -> None:
         # 全局配置
        global driver

        # 加载浏览器
        driver = webdriver.Chrome()

        # 窗口最大化
        driver.maximize_window()

        # 加载地址
        driver.get("http://t-mintegral437.helitong.cn/#/Login")
        # 等待时间
        sleep(5)


        """登录"""
        #输入账号
        driver.find_element(By.XPATH, "//input[@name='mobile']/following::input[2]").send_keys("13017167459")
        sleep(1)
        # 输入密码
        driver.find_element(By.NAME, "password").send_keys("t123456")
        sleep(1)
        # 点击登录
        driver.find_element(By.XPATH, "//button/following::div[10]").click()
        sleep(2)

    def test_jdGoods(self):

        while True:

            """购物车"""
            # 点击购物车
            driver.find_element(By.XPATH, "//div[@class='van-tabbar-item__text']/following::span[2]").click()
            sleep(1)
            """
            点击第一个勾选框
            判断是否存在元素
            默认存在
            """
            element_existence = True
            try:
                # 定位元素尝试点击
                driver.find_element(By.XPATH, "//div[@role='checkbox']/following::div[4]").click()
                sleep(1)
                # 没有定位到元素则抛出异常
            except:
                element_existence = False

            # 判断元素是否存在，不存在则跳出循环，存在则继续循环
            if element_existence == False:
                break
            else:                 
                # 结算
                driver.find_element(By.XPATH, "//div[span=' 全选 ']/following::button").click()
                sleep(2)

                """结算页面"""
                # 选择使用积分
                driver.find_element(By.XPATH, "//div[span='去选择']").click()
                sleep(1)

                # 确认使用积分
                driver.find_element(By.XPATH, "//span[@class='allintegralcolor']/following::button").click()
                sleep(1)

                # 提交订单
                driver.find_element(By.XPATH, "//span[@class='allprice']/following::button").click()
                sleep(5)

                # 输入密码
                driver.find_element(By.XPATH, "//input[@class='password-code-input']").send_keys("201518")
                sleep(1)

                # 确认
                driver.find_element(By.XPATH, "//div[@class='buttons-bar']/button[2]").click()
                sleep(3)

                element_click = True
                try:
                    # 查看订单
                    driver.find_element(By.XPATH, "//div[@class='success']//button[2]").click()
                    sleep(1)

                    # 点击商品详情
                    driver.find_element(By.XPATH, "//div[span='待发货']/following::span[5]").click()
                    sleep(1)

                    # 获取订单详情
                    order_sn = driver.find_element(By.XPATH, "//div[@class='van-cell__value']/following::div[37]").text
                    goods_name = driver.find_element(By.XPATH, "//div[@class='van-card__content']//div/div").text
                    print(f"下单成功：\t订单编号：{order_sn}\t商品名称：{goods_name}")


                    file_txt = open("C:/Users/administered/Desktop/1.txt", mode="a", encoding='utf-8')
                    file_txt.write(f"{order_sn}\t{goods_name}\n")
                    file_txt.close()

                    contents=[]
                    def read_txt():
                        data = open(r"C:/Users/administered/Desktop/1.txt","r",encoding="utf-8") #打开txt文件
                        for i in data:
                            contents.append(i.split())              #遍历txt文件内容存放到列表
                            data.close()
                            print(contents)

                    def write_excel():
                        wb=openpyxl.Workbook()                      #创建1个工作簿
                        ws=wb.create_sheet(u"new")                #用工作簿去创建工作表sheet
                        for i,content in enumerate(contents):
                            for j in range(len(content)):
                                ws.cell(i+1, j+1, content[j])         #用工作表sheet调用单元格，写入内容
                        wb.save("C:/Users/administered/Desktop/output.xlsx")                         #保存文件名

                    read_txt()
                    write_excel()


                    # 返回上一步
                    driver.find_element(By.XPATH, " //div[@class='van-cell']").click()
                    sleep(1)

                    # 退回上一步
                    driver.back()
                               
                    """回到首页"""                
                    driver.find_element(By.XPATH, "//div[@class='success']//button").click()
                    sleep(2)
                except:
                    element_click = False
                if element_click == False:
                    # 点击取消
                    driver.find_element(By.XPATH, " //div[@class='buttons-bar']//button").click()
                    sleep(1)
                    # 点击返回
                    driver.find_element(By.XPATH, " //div[@class='van-cell']").click()
                    sleep(1)

                    """获取商品名称"""
                    failure_goods = driver.find_element(By.XPATH, " //div[@class='van-card__content']//div/div").text
                    print(f"下单失败：\t商品名称：{failure_goods}")
                    file_txt = open("C:/Users/administered/Desktop/1.txt", mode="a", encoding='utf-8')
                    file_txt.write(f"{failure_goods}\n")
                    file_txt.close()

                    contents=[]
                    def read_txt():
                        data = open("C:/Users/administered/Desktop/1.txt","r",encoding="utf-8") #打开txt文件
                        for i in data:
                            contents.append(i.split())              #遍历txt文件内容存放到列表
                            # data.close()
                            # print(contents)

                    def write_excel():
                        wb=openpyxl.Workbook()                      #创建1个工作簿
                        ws=wb.create_sheet(u"new")                #用工作簿去创建工作表sheet
                        for i,content in enumerate(contents):
                            for j in range(len(content)):
                                ws.cell(i+1, j+1, content[j])         #用工作表sheet调用单元格，写入内容
                        wb.save("C:/Users/administered/Desktop/output.xlsx")                         #保存文件名

                    read_txt()
                    write_excel()
                    

                    # 点击编辑
                    driver.find_element(By.XPATH, " //div[span='编辑']").click()
                    sleep(1)
                    # 选中第一个商品
                    driver.find_element(By.XPATH, " //div[@class='van-swipe-cell']//div/div").click()
                    sleep(1)
                    # 点击删除
                    driver.find_element(By.XPATH, " //div[@class='delete-bar']//button").click()
                    sleep(1)
                    # 点击确认
                    driver.find_element(By.XPATH, " //div[@class='van-dialog']//button[2]").click()
                    sleep(2)
                else:
                    # 跳出循环
                    continue


    # 用例执行完关闭页面
    def tearDown(self) -> None:
        driver.close()


if __name__ == "__main__":
    unittest.main()