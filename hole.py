# coding: UTF-8
# import sys
# reload(sys)
# sys.setdefaultencoding("utf-8")
from selenium import webdriver
import requests
from YDMHTTP_py3 import indetify
import time
import json
import psycopg2
import elasticsearch
import threading
import queue
import re
import urllib3
urllib3.disable_warnings()


class Hole(object):
    def __init__(self):
        self.index_url = "https://1.189.209.235"
        self.list_url = "https://1.189.209.235/library/systemrule/queryByGroupId?sEcho=1&iColumns=2&sColumns=&iDisplayStart={}&iDisplayLength=20&mDataProp_0=0&mDataProp_1=1&sSearch=&bRegex=false&sSearch_0=&bRegex_0=false&bSearchable_0=true&sSearch_1=&bRegex_1=false&bSearchable_1=true&iSortCol_0=0&sSortDir_0=asc&iSortingCols=1&bSortable_0=false&bSortable_1=false&_=1552007752653"
        self.post_url = "https://1.189.209.235/library/systemrule/queryById/"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36"}
        self.driver = webdriver.Chrome()
        self.coon = psycopg2.connect(database="postgres", user="postgres", password="postgre", host="120.78.121.207")
        self.cursor = self.coon.cursor()
        self.es = elasticsearch.Elasticsearch("120.78.121.207:9200")
        self.page_queue = queue.Queue()
        self.pg_data_queue = queue.Queue()
        self.es_data_queue = queue.Queue()
        self.thread = threading.Thread

    def login(self):
        self.driver.get(self.index_url)
        self.driver.find_element_by_id("uname").send_keys("test")
        self.driver.find_element_by_id("pwd").send_keys("test")
        captcha_image_url = self.driver.find_element_by_id("code_img").get_attribute("src")
        captcha_content = requests.get(captcha_image_url, verify=False).content
        # captcha_image_path = "./captcha" + str(int(time.time())) + ".png"
        # with open(captcha_image_path, "wb") as f:
        #     f.write(captcha_content.content)
        # captcha_code = indetify(captcha_image_path)
        captcha_code = indetify(captcha_content)


        print("验证码>>>", captcha_code)
        self.driver.find_element_by_id("input1").send_keys(captcha_code)
        self.driver.find_element_by_xpath('//button[text()="登录"]').click()
        self.cookies = {i["name"]: i["value"] for i in self.driver.get_cookies()}
        self.get_pages()

    def get_pages(self):
        first_page_datas = requests.get(self.list_url.format(0), cookies=self.cookies, verify=False).content.decode("utf-8")
        total_nums = json.loads(first_page_datas)["iTotalRecords"]
        pages = total_nums // 20
        for page in range(pages):
            self.page_queue.put(page)

    def get_data(self):
        while True:
            datas = requests.get(self.list_url.format(self.page_queue.get() * 20), cookies=self.cookies,
                                 verify=False).content.decode("utf-8")
            datas = json.loads(datas)
            aaData = datas["aaData"]
            for i in aaData:
                post_params = {"id": i[0]}
                data = requests.post(self.post_url, data=post_params, headers=self.headers, cookies=self.cookies,
                                     verify=False).content.decode("utf-8")
                data = json.loads(data)["gpg"]
                self.pg_data_queue.put(data)
                self.es_data_queue.put(data)
                self.page_queue.task_done()

    def pg_save(self):
        while True:
            data = self.pg_data_queue.get()
            for i in data:
                if not isinstance(data[i], str):
                    data[i] = str(data[i])
                if data[i] == "":
                    data[i] = " "
                if "\n" in data[i]:
                    ret = re.sub("\n", "", data[i])
                    data[i] = ret
                if "#" in data[i]:
                    ret = re.sub("#", "", data[i])
                    data[i] = ret


            placeholders = ", ".join(["%s"] * len(data))
            columns = ", ".join(data.keys())
            sql = "INSERT INTO %s ( %s ) VALUES ( %s )" % ('k_webray_cve_info', columns, placeholders)
            values = list(data.values())
            try:

                self.cursor.execute(sql, values)
                print(sql)
                print(values)
                self.coon.commit()
                self.pg_data_queue.task_done()

            except Exception as e:
                print(e)

    def es_save(self):
        while True:
            data = self.es_data_queue.get()
            self.es.index(index='hole', doc_type='k_webray_cve_info', body=data, id=None)

    def run(self):
        self.login()
        threads = []
        for i in range(6):
            threads.append(self.thread(target=self.get_data))
            threads.append(self.thread(target=self.pg_save))
            # threads.append(self.thread(target=self.es_save))
        for thread in threads:
            thread.start()
        for task in [self.page_queue, self.pg_data_queue,self.es_data_queue]:
            task.join()

        self.driver.close()



if __name__ == '__main__':
    hole = Hole()
    hole.run()
