import unittest

# 测试用例集管理
from time import sleep

from selenium import webdriver
import warnings

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from ddt import file_data, ddt

from test_火焰杯.test_决赛webUI_2.base.base_page import BasePage


@ddt
class UnitForTest1(unittest.TestCase, BasePage):
    # 测试用例，实现登录+查看我的活动
    @classmethod
    def setUpClass(cls) -> None:
        warnings.simplefilter("ignore", ResourceWarning)
        cls.driver = webdriver.Edge()
        cls.driver.implicitly_wait(2)
        cls.driver.get("https://jobs.bytedance.com/campus/position")

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def test_01(self):
        self.el1 = (By.XPATH, "//*[@id='bd']/section/section/main/div/div/div[1]/div/div[2]/span/input")  # 搜索功能元素
        self.click(self.el1)
        sleep(2)
        self.input_(self.el1, '测试')  # 输入关键词
        self.input_(self.el1, Keys.ENTER)  # 输入关键词
        result = self.driver.find_element(By.CSS_SELECTOR,"#bd > section > section > main > div > div > div.content__IN8vJ > div.rightBlock.rightBlock__2ZGFh > div.borderContainer__3S4gr > div.listItems__1q9i5 > a:nth-child(2) > div > div.title__37NOe.positionItem-title.sofiaBold > span").text
        assert "测试" in result



if __name__ == '__main__':
    unittest.main()
