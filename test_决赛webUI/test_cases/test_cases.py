from time import sleep
import pytest
from selenium import webdriver
import warnings
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from ddt import file_data, ddt

from test_火焰杯.test_决赛webUI.base.base_page import BasePage
from test_火焰杯.test_决赛webUI.page_object.login_page import LoginPage
from test_火焰杯.test_决赛webUI.page_object.my_page import My


@ddt
class TestCase(BasePage):

    def setup_class(self) -> None:
        warnings.simplefilter("ignore", ResourceWarning)
        self.driver = webdriver.Edge()
        self.driver.implicitly_wait(2)
        self.lp = LoginPage(self.driver)
        self.my = My(self.driver)

    def teardown_class(self) -> None:
        self.driver.quit()

    @file_data('../data/user_data.yaml')
    def test_01(self, **kwargs):
        # 登录流程
        self.lp.login(kwargs['user'], kwargs['pwd'])
        # 查看我的活动流程
        self.my.activity(kwargs['time_'])
        sleep(2)
        (By.XPATH, "//*[@id='app']/div[2]/div[1]/div[1]/div/div/div[2]/div/input").click()  # 搜索功能元素
        # self.click(self.el1)
        # self.el2 = (By.XPATH, "//*[@id='app']/div[2]/form/div/div/div/div[2]/div/input")
        # self.click(self.el2)
        # self.input_(self.el2, '火焰杯测试商品')  # 输入关键词
        # self.input_(self.el2, Keys.ENTER)  # 模拟回车
        # sleep(1)
        # self.el3 = (By.XPATH, "//*[@id='app']/div[2]/div[2]/div[1]/div/div")  # 默认搜索备选关键
        # self.click(self.el3)  # 点击备选关键词第一条
        # self.el4 = (By.XPATH, "//*[@id='app']/div[2]/div[5]/button[1]")  #
        # self.click(self.el4)  # 点击加入购物车
        # sleep(1)
        # self.el5 = (By.XPATH, "//*[@id='app']/div[2]/div[3]/div[3]/div[3]/button[1]")  #
        # self.click(self.el5)  # 确认加入购物车
        # sleep(1)
        # self.el6 = (By.XPATH, "//*[@id='app']/div[2]/div[5]/div[1]/div")  #
        # self.click(self.el6)  # 点击详情（购物车）
        # re = self.driver.find_element(By.CSS_SELECTOR,
        #                               "#app > div.tab-cart.view-router > div.card-goods.van-checkbox-group > div > div.van-card").text
        # assert '火焰杯测试商品' in re
        # # assert '火焰杯测试商品' in self.driver.page_source 第二种断言方法

if __name__ == '__main__':
    pytest.main()
