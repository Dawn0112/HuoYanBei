'''
    搜索页面，实现系统搜索操作
    核心操作流程：
        登录流程
        元素关联：
        搜索框
        搜索按钮
'''
import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver

from test_火焰杯.test_初赛webUI.base.base_page import BasePage


class SearchPage(BasePage):
    # url
    url = 'https://ceshiren.com/search?expanded=true' #题目给的被测对象对数据驱动不方便，因为每次搜索都先要微信扫码登录，这里我换成了不用登录就能搜索的url
    # 页面元素
    # 元素的操作流
    input = (By.XPATH, "//*[@id='ember27']")
    button = (By.XPATH, "//*[@id='ember29']")

    # 元素的操作流
    def search(self, key_words):
        self.open()  # 访问url
        self.input_(self.input, key_words)  # 输入关键词
        self.click(self.button)  # 点击按钮

#
# if __name__ == '__main__':
#     driver = webdriver.Edge()
#     key_word = '面试经验'
#     # 实例化
#     sp = SearchPage(driver)
#     sp.search(key_word)
