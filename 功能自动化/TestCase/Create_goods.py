# coding = utf-8
"""创建商品"""
from time import sleep
from selenium import webdriver
from xlutils.copy import copy
from selenium.webdriver.common.by import By
import xlrd
import unittest
class Create_goods(unittest.TestCase):
    def setUp(self) -> None:
        
        file = "C:/Users/Administrator/Desktop/login.xls"
        data1 = xlrd.open_workbook(file)
        cols = ["品牌名称", "商品名称", "商品六九码", "商品单位", "发货地址"]
        # 获取所有的sheet表单。
        sheets = data1.sheet_names()
        # 获取第一个表单
        work_sheet = data1.sheet_by_name(sheets[0])
        # 将xlrd对象变成xlwt
        new_work_book = copy(data1)
        # 添加内容到指定工作表
        new_sheet = new_work_book.get_sheet("Sheet1")

        # 获取行总数
        nrows = sheets.nrows
        # 获取列总数
        ncols = sheets.ncols


        for i in range(nrows):
            list.append([])
            for j in range(ncols):
                # print(sheet0.cell_value(i, j))
                list[i].append(str(data1.cell_value(i,j)))
        print(list)
        return list

    def test_Create_goods(self):

        global driver

        driver = webdriver.Chrome()

        driver.maximize_window()

        driver.get("http://t-admin.helitong.cn/login")

        driver.find_element(By.XPATH, "//input[@placeholder='请输入登录账号']").send_keys(list[0])
        sleep(2)

        driver.find_element(By.XPATH, "//input[@placeholder='请输入密码']").send_keys(list[0])
        sleep(2)

        driver.find_element(By.XPATH, "//button[span='登录']").click()
        sleep(2)
