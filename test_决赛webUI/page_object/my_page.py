from selenium.webdriver.common.by import By
from selenium import webdriver

from test_火焰杯.test_决赛webUI.base.base_page import BasePage


class My(BasePage):
    url = 'http://litemall.hogwarts.ceshiren.com/vue/index.html#/user/'
    button = (By.XPATH,
              "//*[@id='app']/div[3]/div[1]/div[1]/i")

    def activity(self, time_):
        self.wait(time_)
        self.open()
        self.click(self.button)
