from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get(r'http://t-admin.liyusmart.com/login')

driver.find_elements_by_css_selector("input[class~='el-input__inner']")[0].send_keys('子账号唐')
sleep(0.5)
driver.find_elements_by_css_selector("input[class~='el-input__inner']")[1].send_keys('t123456')
sleep(0.5)
driver.find_elements_by_css_selector("button[class~='el-button el-button--primary']")[0].click()
sleep(0.5)

#一级菜单
driver.find_elements_by_css_selector("div[class~='el-submenu__title']")[0].click()
sleep(0.5)
#二级菜单
driver.find_elements_by_css_selector("li[class~='el-menu-item']")[0].click()
sleep(0.5)