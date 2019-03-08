# coding: UTF-8
from selenium import webdriver
import requests
from YDMHTTPpy2 import indetify
import time
import json
import psycopg2
import threading
import Queue



class Hole(object):
    def __init__(self):
        self.index_url = "https://1.189.209.235"
        self.list_url = "https://1.189.209.235/library/systemrule/queryByGroupId?sEcho=1&iColumns=2&sColumns=&iDisplayStart={}&iDisplayLength=20&mDataProp_0=0&mDataProp_1=1&sSearch=&bRegex=false&sSearch_0=&bRegex_0=false&bSearchable_0=true&sSearch_1=&bRegex_1=false&bSearchable_1=true&iSortCol_0=0&sSortDir_0=asc&iSortingCols=1&bSortable_0=false&bSortable_1=false&_=1552007752653"
        self.post_url = "https://1.189.209.235/library/systemrule/queryById/"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36"}
        self.driver = webdriver.Chrome()
        self.coon = psycopg2.connect(database="postgres", user="postgres", password="postgre",host="127.0.0.1")
        # self.queue = Queue.Queue()
        # self.thread = threading.Thread
    def login(self):
        self.driver.get(self.index_url)
        self.driver.find_element_by_id("uname").send_keys("test")
        self.driver.find_element_by_id("pwd").send_keys("test")
        captcha_image_url = self.driver.find_element_by_id("code_img").get_attribute("src")
        captcha_content = requests.get(captcha_image_url, verify=False)
        captcha_image_path = "./captcha" + str(int(time.time())) + ".png"
        with open(captcha_image_path, "wb") as f:
            f.write(captcha_content.content)
        captcha_code = indetify(captcha_image_path)
        print "验证码>>>", captcha_code
        self.driver.find_element_by_id("input1").send_keys(captcha_code)
        self.driver.find_element_by_xpath('//button[text()="登录"]').click()
        self.cookies = {i["name"]: i["value"] for i in self.driver.get_cookies()}

    def get_data(self):
        first_page_datas = requests.get(self.list_url.format(0), cookies=self.cookies, verify=False).text
        total_nums = json.loads(first_page_datas)["iTotalRecords"]
        pages = total_nums // 20
        for page in range(pages):
            datas = requests.get(self.list_url.format(page * 20), cookies=self.cookies, verify=False).text
            datas = json.loads(datas)
            aaData = datas["aaData"]
            for i in aaData:
                post_params = {"id": i[0]}
                data = requests.post(self.post_url, data=post_params, headers=self.headers, cookies=self.cookies, verify=False).text
                data = json.dumps(data)
                self.save(data)
        self.driver.close()
    def save(self,data):
        cursor = self.coon.cursor()
        cursor.execute("insert into hole(data) values(%s)", [data])
        self.coon.commit()


    def run(self):
        self.login()
        self.get_data()
        # threads = []
        # for i in range(5):
        #     threads.append(self.thread(target=self.get_data))
        #     threads.append(self.thread(target=self.save))
        #
        # for i in threads:
        #     i.start()


if __name__ == '__main__':
    hole = Hole()
    hole.run()
