import unittest
from selenium import webdriver
from time import sleep

class TestBaidu(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get("http://www.baidu.com")

    def test_baidu(self):
        driver=self.driver
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys("Selenium 自学网")
        driver.find_element_by_id("su").click()
        sleep(3)

        title=driver.title
        self.assertEqual(title,"Selenium 自学网_百度搜索")

        driver.find_element_by_partial_link_text("Selenium自动化").click()
        sleep(5)

    def tearDown(self):
        self.driver.quit()