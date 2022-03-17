# -*- coding: utf-8 -*-
# 淘宝秒杀脚本，扫码登录版
<<<<<<< HEAD
from selenium import webdriver
import datetime
import time
=======
import os
from selenium import webdriver
import datetime
import time
from os import path
from selenium.webdriver.common import by
>>>>>>> 5d6bdd5 (积分商城下单优化)
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()


def login():
    # 打开淘宝登录页，并进行扫码登录
    driver.get("https://login.taobao.com/")
    time.sleep(3)
    # if driver.find_element_by_link_text("亲，请登录"):
    driver.find_element(By.XPATH, "//i[@class='iconfont icon-qrcode']").click()

    print("请在30秒内完成扫码")
    time.sleep(10)

    driver.get("https://cart.taobao.com/cart.htm")
    time.sleep(3)
    # 点击购物车里全选按钮
    # if driver.find_element_by_id("J_CheckBox_939775250537"):
    # driver.find_element_by_id("J_CheckBox_939775250537").click()
    # if driver.find_element_by_id("J_CheckBox_939558169627"):
    # driver.find_element_by_id("J_CheckBox_939558169627").click()
    if driver.find_element(By.ID, "J_SelectAll1"):
        driver.find_element(By.ID, "J_SelectAll1").click()
        now = datetime.datetime.now()
<<<<<<< HEAD
        print('登录成功:', now.strftime('%Y-%m-%d %H:%M:%S'))
=======
        print('login success:', now.strftime('%Y-%m-%d %H:%M:%S'))
>>>>>>> 5d6bdd5 (积分商城下单优化)


def buy(buytime):
    while True:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
<<<<<<< HEAD
        print("当前时间:" + now)
        # 对比时间，时间到的话就点击结算
        if now > buytime:
            try: 
                if driver.find_element(By.ID, "J_Go"):
                    # 点击结算按钮
                    driver.find_element(By.ID, "J_Go").click()
                    # 跳转到页面底部
                    driver.execute_script("var q=document.documentElement.scrollTop=10000")

                # 提交订单
                # driver.find_element(By.XPATH, "//a[@class='go-btn']").click()
                driver.find_element(By.LINK_TEXT, "提交订单").click()
                time.sleep(4)

                # 输入密码
                driver.find_element(By.ID, "payPassword_rsainput").send_keys("201518")

                # 确认
                driver.find_element(By.ID, "J_authSubmit").click()
            except:
                time.sleep(0.1)
        print(now)
        time.sleep(0.1)
=======
        # 对比时间，时间到的话就点击结算
        if now > buytime:
            try:
                
                if driver.find_element(By.ID, "J_Go"):
                    # 点击结算按钮
                    driver.find_element(By.ID, "J_Go").click()
                    # 提交订单
                    driver.find_element(By.XPATH, "//a[@class='go-btn']").click()
                    time.sleep(5)
                    # 输入密码
                    driver.find_element(By.ID, "payPassword_rsainput").send_keys("201518")
                    # 确认
                    driver.find_element(By.ID, "J_authSubmit").click()
            except:
                time.sleep(0.1)
                print(now)
                time.sleep(0.1)
>>>>>>> 5d6bdd5 (积分商城下单优化)
if __name__ == "__main__":
    # times = input("请输入抢购时间：")
    # 时间格式："2018-09-06 11:20:00.000000"
    login()
<<<<<<< HEAD
    buy("2022-02-17 19:00:00.000000")
=======
    buy("2022-02-14 21:44:00.000000")
>>>>>>> 5d6bdd5 (积分商城下单优化)
