import unittest

# 测试用例集管理
from time import sleep
from selenium import webdriver
import warnings
from ddt import file_data, ddt, data, unpack

from test_火焰杯.test_初赛webUI.base.base_page import BasePage
from test_火焰杯.test_初赛webUI.page_object.search_page import SearchPage


def readFile():
    file = open('..\data\key.txt', 'r', encoding='utf8')  # 'r'表示可读
    list1 = []
    for line in file.readlines():
        list1.append(line.strip('\n').split(','))  # 将文件每行数据去掉换行\n符号，以逗号分隔，存进列表里
        print(list1)
    file.close()
    return list1


@ddt
class Cases(unittest.TestCase,BasePage):
    @classmethod
    def setUpClass(cls) -> None:
        warnings.simplefilter("ignore", ResourceWarning)
        cls.driver = webdriver.Edge()
        cls.sp = SearchPage(cls.driver)
        cls.driver.implicitly_wait(2)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()

    @data(*readFile())  # 加*表示以元组形式处理，**表示以字典形式处理
    @unpack
    def test_1(self, key):
        self.driver.implicitly_wait(5)
        self.sp.search(key)
        sleep(2)


if __name__ == '__main__':
    unittest.main()
