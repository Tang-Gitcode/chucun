from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class LoginClass:
    def __init__(self, username, password, sign_in):
# 定位元素
        self.username = (By.ID, 'input1')
        self.password = (By.ID, 'input2')
        self.sign_in = (By.ID, "submit")
# 设置用户名
    def set_username(self):
        input1 = self.driver.find.element(*LoginClass.username).send.keys()
    # 设置密码
    def set_password(self):
        input2 = self.driver.find.element(*LoginClass.password).keys(Keys.RETURN)
    # 提交登录信息
    def sign(self):
        submit = self.driver.find.element(*LoginClass.sign_in).click()