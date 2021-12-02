# 应用层 
from selenium.webdriver.common.by import By
from Unittest.base.base_page import BasePage



class LoginPage(BasePage):
    # 页面的元素
    user_loc = (By.XPATH, "//input[@placeholder='请输入登录账号']").send_keys("13530600569")
    pwd_loc = (By.XPATH, "//input[@placeholder='请输入登录密码']").send_keys("t123456")
    submit_loc = (By.XPATH, "//button[span='登录']").click()


    # 页面的动作
    def login_admin(self):
        self.locater_element(LoginPage.user_loc)
        self.locater_element(LoginPage.pwd_loc)
        self.locater_element(LoginPage.submit_loc)

