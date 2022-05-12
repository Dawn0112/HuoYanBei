"""
    基类：工具类，将常用的与项目适配的相关函数，进行二次封装，变成自定义内容，便于测试调用
        存在的意义是为了让页面对象进行继承，从而获得基本的方法来实现页面的操作流程
    常用项：
        访问url
        元素定位
        输入
        点击
        退出
        等待、、、、、、、
"""
from time import sleep

from selenium import webdriver


# 创建基类
class BasePage:

    # 构造函数
    def __init__(self, driver):
        self.driver = driver

    # 访问url
    def open(self):
        self.driver.get(self.url)

    # 元素定位
    def locator(self, loc):
        return self.driver.find_element(*loc)

    # 输入
    def input_(self,loc, txt):
        self.locator(loc).send_keys(txt)

    # 点击
    def click(self, loc):
        self.locator(loc).click()

    # 等待
    def wait(self, time_):
        sleep(time_)

    # 退出
    def quit(self):
        self.driver.quit()
