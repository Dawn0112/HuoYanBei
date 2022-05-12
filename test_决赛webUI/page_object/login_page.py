'''
    登录页面，实现系统登录操作
    核心操作流程：
        登录流程
        元素关联：
        账号
        密码
        登录按钮
'''
from selenium.webdriver.common.by import By
from selenium import webdriver

from test_火焰杯.test_决赛webUI.base.base_page import BasePage


class LoginPage(BasePage):
    # url
    url = 'http://litemall.hogwarts.ceshiren.com/vue/index.html#/login?redirect=user'
    # 页面元素
    # 元素的操作流
    user = (By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[1]/div[1]/input')
    pwd = (By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[2]/div[1]/input')
    button = (By.XPATH, '//*[@id="app"]/div[2]/div[2]/button')

    # 元素的操作流
    def login(self, username, password):
        self.open()  # 访问url
        self.input_(self.user, username)  # 输入账号
        self.input_(self.pwd, password)
        self.click(self.button)  # 点击登录按钮
#
#
# if __name__ == '__main__':
#     driver = webdriver.Edge()
#     user = 'dawn'
#     pwd = 'wms20010112'
#     # 实例化登陆页面
#     lp = LoginPage(driver)
#     lp.login(user, pwd)
