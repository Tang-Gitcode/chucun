# 应用层
from time import sleep
from selenium.webdriver.common.by import By
from 功能自动化.base.base_page import BasePage



class LoginPage(BasePage):
    # 登录的元素
    user_loc = (By.XPATH, "//input[@placeholder='请输入登录账号']")
    pwd_loc = (By.XPATH, "//input[@placeholder='请输入登录密码']")
    submit_loc = (By.XPATH, "//button[span='登录']")


    # 登录
    def login_admin(self, user="13530600569", pwd="t123456"):
        self.send_keys(LoginPage.user_loc, user)
        sleep(0.5)
        self.send_keys(LoginPage.pwd_loc, pwd)
        sleep(0.5)
        self.click(LoginPage.submit_loc)
        sleep(2)


