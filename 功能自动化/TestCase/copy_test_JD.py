# 京东商品下单

from os import close, write
import time
from types import DynamicClassAttribute
import unittest
import openpyxl
import xlrd
import xlwt
from xlutils.copy import copy
from unittest.main import main
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from xlwt.Utils import rowcol_pair_to_cellrange


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
        sleep(3)

    def test_jdGoods(self):
        try:
            while True:
                login = True
                try:
                
                    # while True:

                    """购物车"""
                    # 点击购物车
                    driver.find_element(By.XPATH, "//div[@class='van-tabbar-item__text']/following::span[2]").click()

                    sleep(2)
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

                    # 判断元素是否存在，不存在则结束循环，存在则继续循环
                    if element_existence == False:
                        break
                    else:                 
                        # 结算
                        driver.find_element(By.XPATH, "//div[span=' 全选 ']/following::button").click()
                        sleep(2)

                        """结算页面"""
                        # 选择使用积分
                        driver.find_element(By.XPATH, "//div[span='去选择']").click()
                        sleep(2)

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
                            sleep(3)

                            # 点击商品详情
                            driver.find_element(By.XPATH, "//div[span='待发货']/following::span[5]").click()
                            sleep(2)

                            # 获取订单详情
                            order_sn = driver.find_element(By.XPATH, "//div[@class='van-cell__value']/following::div[37]").text
                            list_order_sn = ''.join(order_sn)
                            sleep(2)
                            goods_name = driver.find_element(By.XPATH, "//div[@class='van-card__content']//div/div").text
                            list_goods_name = ''.join(goods_name)
                            print(f"下单成功：\t订单编号：{list_order_sn}")
                            print(f"下单成功：\t商品名称：{list_goods_name}")
                            sleep(2)

                            try:
                                # 打开excel
                                word_book = xlrd.open_workbook('C:/Users/Administrator/Desktop/京东商品下单.xls', formatting_info=True)
                                
                                style = xlwt.XFStyle()#格式信息
                                font = xlwt.Font()#字体基本设置
                                font.name = u'等线'
                                font.height= 220
                                style.font = font

                                # 获取所有的sheet表单。
                                sheets = word_book.sheet_names()
                                # 获取第一个表单
                                work_sheet = word_book.sheet_by_name(sheets[0])
                                # 获取已经写入的行数
                                old_rows = work_sheet.nrows
                                # 获取表头信息
                                # heads = work_sheet.row_values(0)
                                # 将xlrd对象变成xlwt
                                new_work_book = copy(word_book)
                                # 添加内容
                                new_sheet = new_work_book.get_sheet("12.11")

                                new_sheet.write(old_rows, 1, list_order_sn, style)
                                new_sheet.write(old_rows, 2, list_goods_name, style)
                                    
                                new_work_book.save('C:/Users/Administrator/Desktop/京东商品下单.xls')

                                print('追加成功！')
                            except Exception as e: 
                                print('追加失败！',e)
                            sleep(3)

                            # 返回上一步
                            driver.find_element(By.XPATH, " //div[@class='van-cell']").click()
                            sleep(5)

                            # 退回上一步
                            driver.back()
                            sleep(5)
                                    
                            """回到首页"""                
                            driver.find_element(By.XPATH, "//div[@class='success']//button").click()
                            sleep(5)
                        except:
                            element_click = False
                        if element_click == False:
                            # 点击取消
                            driver.find_element(By.XPATH, " //div[@class='buttons-bar']//button").click()
                            sleep(1)
                            # 点击返回
                            driver.find_element(By.XPATH, " //div[@class='van-cell']").click()
                            sleep(3)

                            """获取商品名称"""
                            failure_goods = driver.find_element(By.XPATH, " //div[@class='van-card__content']//div/div").text
                            list_failure_goods = ''.join(failure_goods)
                            print(f"下单失败：\t商品名称：{list_failure_goods}")
                            sleep(3)

                            try:
                                # 打开excel
                                word_book = xlrd.open_workbook('C:/Users/Administrator/Desktop/京东商品下单.xls', formatting_info=True)
                                
                                style = xlwt.XFStyle()#格式信息
                                font = xlwt.Font()#字体基本设置
                                font.name = u'等线'
                                font.height= 220
                                style.font = font

                                # 获取所有的sheet表单。
                                sheets = word_book.sheet_names()
                                # 获取第一个表单
                                work_sheet = word_book.sheet_by_name(sheets[0])
                                # 获取已经写入的行数
                                old_rows = work_sheet.nrows
                                # 获取表头信息
                                # heads = work_sheet.row_values(0)
                                # 将xlrd对象变成xlwt
                                new_work_book = copy(word_book)
                                # 添加内容
                                new_sheet = new_work_book.get_sheet("12.11")

                                new_sheet.write(old_rows, 2, list_failure_goods, style)
                                new_sheet.write(old_rows, 3, "失败", style)
                                new_sheet.write(old_rows, 4, "下单失败", style)
                                    
                                new_work_book.save('C:/Users/Administrator/Desktop/京东商品下单.xls')
                                print('追加成功！')
                            except Exception as e: 
                                print('追加失败！',e)
                            sleep(3)
                            

                            # 点击编辑
                            driver.find_element(By.XPATH, " //div[span='编辑']").click()
                            sleep(2)
                            # 选中第一个商品
                            driver.find_element(By.XPATH, " //div[@class='van-swipe-cell']//div/div").click()
                            sleep(2)
                            # 点击删除
                            driver.find_element(By.XPATH, " //div[@class='delete-bar']//button").click()
                            sleep(1)
                            # 点击确认
                            driver.find_element(By.XPATH, " //div[@class='van-dialog']//button[2]").click()
                            sleep(2)
                            # else:
                            #     # 跳出循环
                            #     continue
                except:
                    login = False
                    if login == False:
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
                    else:
                        # 跳出循环
                        continue
            print("运行成功！")
        except Exception as e:
            print(f"运行错误：{e}")

    # 用例执行完关闭页面
    def tearDown(self) -> None:
        driver.close()


if __name__ == "__main__":
    unittest.main()


