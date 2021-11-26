from selenium import webdriver
import time
import xlrd

# 打开指定路径excel表格
data = xlrd.open_workbook("C:/Users/administered/Desktop/login.xls")

# 获取指定工作表
table = data.sheet_by_name(u"Sheet1")


# 指定一个函数处理登陆操作
def account_login():
    # 获取谷歌浏览器
    driver = webdriver.Chrome()
    driver.get("http:www.baidu.com")
    driver.find_element_by_xpath("loginFlie")

print(time.time())
