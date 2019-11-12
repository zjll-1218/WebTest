# coding=utf-8
from .BasePage import BasePage


class LoginPage(BasePage):
    org_elem = ('xpath', 'html/body/div[1]/div/div/div[2]/div[2]/form/div[1]/div/div/div/input')
    org_name_elem = ('xpath', 'html/body/div[2]/div[1]/div[1]/ul')
    user_name_elem = ('xpath', 'html/body/div[1]/div/div/div[2]/div[2]/form/div[2]/div/div/input')
    passport_elem = ('xpath', 'html/body/div[1]/div/div/div[2]/div[2]/form/div[3]/div/div/input')
    login_button_elem = ('class', 'submit')

    def __init__(self, browser='chrome'):
        super().__init__(browser)

    def selectOrg(self, org_name):
        # 选择机构
        o = self.findElement(self.org_elem)
        self.sendKeys(o, org_name)
        self.driver.implicitly_wait(5)
        org = self.findElement(self.org_name_elem)
        self.click(org)

    def setUsername(self, user_name):
        # 输入用户名
        u = self.findElement(self.user_name_elem)
        self.sendKeys(u, user_name)

    def setPassport(self, pass_port):
        # 输入密码
        p = self.findElement(self.passport_elem)
        self.sendKeys(p, pass_port)

    def clickLogin(self):
        # 点击【登录】
        b = self.findElement(self.login_button_elem)
        self.click(b)
