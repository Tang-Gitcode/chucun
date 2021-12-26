"""积分商城下单"""

from os import close
import time
import unittest
import xlrd
from xlrd.formula import Ref3D
import xlwt
from unittest.main import main
from selenium import webdriver
from xlutils.copy import copy
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from xlwt.Style import colour_index_func, easyxf

class integral_Goods(unittest.TestCase):


    def setUp(self) -> None:

        # 设置全局变量
        global driver

        # 加载谷歌浏览器
        driver = webdriver.Chrome()

        # 窗口最大化
        driver.maximize_window()

        # 加载地址
        driver.get("http://t-mintegral437.helitong.cn/#/AccountLogin")
        time.sleep(5)


        """登录"""
        # # 账号
        # driver.find_element(By.XPATH, "//input[@placeholder='请输入登录账号']").send_keys("13017167459")
        # time.sleep(1)
        # # 输入密码
        # driver.find_element(By.NAME, "password").send_keys("t123456")
        # time.sleep(1)

        # # 滑动验证
        # button = driver.find_element(By.XPATH, "//div[@class='button']")
        # ActionChains(driver).drag_and_drop_by_offset(button,300,0).perform()
        # time.sleep(2)

        # # 点击登录
        # driver.find_element(By.XPATH, "//button[@type='submit']").click()
        # time.sleep(5)

        
        # 手机验证码登录
        driver.find_element(By.XPATH, "//div[@class='card_title']//span").click()
        time.sleep(2)
        driver.find_element(By.NAME, "mobile").send_keys("16620129737")
        time.sleep(2)
        driver.find_element(By.XPATH, "//div[@class='van-field__button']//span").click()
        time.sleep(30)

        # 点击登录
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(5)

        button1 = True
        try:

            # 跳转到页面底部
            driver.execute_script("var q=document.documentElement.scrollTop=10000")
            # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") 
            time.sleep(3)

        except:
            button1 = False
        if button1 == False:
            driver.refresh()


    def test_integralGoods(self):
        try:
            i = 0
            while True:
                element_login = True
                try:
                    # 跳转到页面底部
                    driver.execute_script("var q=document.documentElement.scrollTop=10000")
                    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") 
                    time.sleep(3)

                    goods = True
                    try:
                        # 进入商品详情
                        driver.find_elements(By.XPATH, "//div[@class='cap-goods__img']")[i].click()
                        time.sleep(2)

                    except:
                        goods = False
                    if goods == False:
                        break
                    else:

                        # 点击立即购买
                        driver.find_element(By.XPATH, "//div[@class='van-goods-action']/button[2]").click()
                        time.sleep(2)

                        # 点击确认
                        driver.find_element(By.XPATH, "//div[@class='van-sku-actions']//button").click()
                        time.sleep(3)


                        """结算页面"""
                        button = True
                        try:
                            # 选择使用积分
                            driver.find_element(By.XPATH, "//div[span='去选择']").click()
                            time.sleep(1)

                            # 确认使用积分
                            driver.find_element(By.XPATH, "//span[@class='allintegralcolor']/following::button").click()
                            time.sleep(1)

                            # 提交订单
                            driver.find_element(By.XPATH, "//span[@class='allprice']/following::button").click()
                            time.sleep(3)

                            # 输入密码
                            driver.find_element(By.XPATH, "//input[@class='password-code-input']").send_keys("201518")
                            time.sleep(1)

                            # 确认密码
                            driver.find_element(By.XPATH, "//div[@class='buttons-bar']/button[2]").click()
                            time.sleep(5)

                            element_click = True
                            try:
                                # 查看订单
                                driver.find_element(By.XPATH, "//div[@class='success']//button[2]").click()
                                time.sleep(2)

                                # 点击商品详情
                                driver.find_element(By.XPATH, "//div[span='待发货']/following::span[5]").click()
                                time.sleep(5)

                                # 获取订单编号
                                # order_sn = driver.find_element(By.XPATH, "//div[@class='van-cell__value']/following::div[37]").text
                                order_sn = driver.find_element(By.XPATH, "//div[@class='opposite van-cell']/div[2]").text
                                list_order_sn = ''.join(order_sn)
                                time.sleep(3)

                                # 获取商品名称
                                goods_name = driver.find_element(By.XPATH, "//div[@class='van-card__content']//div/div").text
                                list_goods_name = ''.join(goods_name)
                                print(f"下单成功：\t订单编号：{list_order_sn}")
                                print(f"\t商品名称：{list_goods_name}")
                                time.sleep(3)

                                try:
                                    # 打开excel
                                    word_book = xlrd.open_workbook('output.xls', formatting_info=True)
                                    
                                    #格式信息
                                    style = xlwt.XFStyle()
                                    #字体基本设置
                                    font = xlwt.Font()
                                    # 设置字体
                                    font.name = u'等线'
                                    # 设置字号
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
                                    # 添加内容到指定工作表
                                    new_sheet = new_work_book.get_sheet("12.24")
                                    # 追加内容
                                    n = "%03d" % (i+1)
                                    new_sheet.write(old_rows, 0, n, style)
                                    new_sheet.write(old_rows, 1, list_order_sn, style)
                                    new_sheet.write(old_rows, 2, list_goods_name, style)
                                    new_sheet.write(old_rows, 3, "成功", style)
                                    # 保存                                 
                                    new_work_book.save('output.xls')

                                    print('追加成功！')
                                except Exception as e: 
                                    print('追加失败！',e)
                                time.sleep(3)

                                # 退回上一步
                                driver.back()
                                # driver.find_element(By.XPATH, " //div[@class='van-cell']").click()
                                time.sleep(2)

                                # 退回上一步
                                driver.back()
                                time.sleep(2)

                                # 退回上一步       
                                driver.back()
                                time.sleep(2)

                                """回到首页"""  
                                driver.back()               
                                # driver.find_element(By.XPATH, "//div[@class='success']//button").click()
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
                                list_failure_goods = ''.join(failure_goods)
                                print(f"下单失败：\t商品名称：{list_failure_goods}")
                                time.sleep(3)

                                try:
                                    # 打开excel
                                    word_book = xlrd.open_workbook('output.xls', formatting_info=True)
                                    #格式信息
                                    style = xlwt.XFStyle()
                                    #字体基本设置
                                    font = xlwt.Font()
                                    # 设置字体
                                    font.name = u'等线'
                                    # 字体颜色
                                    font.colour_index = 2       # 指定colour_index索引
                                    # 设置字号
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
                                    # 添加内容到指定工作表
                                    new_sheet = new_work_book.get_sheet("12.24")
                                    # 追加内容
                                    n = "%03d" % (i+1)
                                    new_sheet.write(old_rows, 0, n, style)
                                    new_sheet.write(old_rows, 2, list_failure_goods, style)
                                    new_sheet.write(old_rows, 3, "失败", style)
                                    new_sheet.write(old_rows, 4, "下单失败", style)
                                    # 保存
                                    new_work_book.save('output.xls')
                                    print('追加成功！')
                                except Exception as e: 
                                    print('追加失败！',e)
                                time.sleep(3)

                                # 点击返回
                                driver.find_element(By.XPATH, " //div[@class='van-cell']").click()
                                time.sleep(3)
                                # 点击返回
                                driver.find_element(By.XPATH, " //div[@class='van-cell']").click()
                                time.sleep(3)
                                i += 1
                        
                        except:
                            button = False
                        if button == False:

                            # 点击X号
                            driver.find_element(By.XPATH, "//i[@role='button']").click()
                            time.sleep(2)

                            # 退回一步
                            driver.back()
                            time.sleep(3)
                            i += 1

                except:
                    element_login = False
                

                if element_login == False:
                    """登录"""
                    # # 账号
                    # driver.find_element(By.XPATH, "//input[@placeholder='请输入登录账号']").send_keys("13017167459")
                    # time.sleep(1)
                    # # 输入密码
                    # driver.find_element(By.NAME, "password").send_keys("t123456")
                    # time.sleep(1)

                    # # 滑动验证
                    # button = driver.find_element(By.XPATH, "//div[@class='button']")
                    # ActionChains(driver).drag_and_drop_by_offset(button,300,0).perform()
                    # time.sleep(2)

                    # # 点击登录
                    # driver.find_element(By.XPATH, "//button[@type='submit']").click()
                    # time.sleep(5)
                    
                    # 手机验证码登录
                    driver.find_element(By.XPATH, "//div[@class='card_title']//span").click()
                    time.sleep(2)
                    driver.find_element(By.NAME, "mobile").send_keys("13017167459")
                    time.sleep(2)
                    driver.find_element(By.XPATH, "//div[@class='van-field__button']//span").click()
                    time.sleep(30)

                    # 点击登录
                    driver.find_element(By.XPATH, "//button[@type='submit']").click()
                    time.sleep(5)
                else:
                    continue
                print("运行成功")
        except Exception as e:
            print(f"运行失败{e}")

    # 执行完用例后的操作
    def tearDown(self) -> None:
        # 退出浏览器
        driver.quit()


# 测试
if __name__ == "__main__":
    unittest.main()

    

