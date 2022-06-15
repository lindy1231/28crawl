import re
import sys
import scrapy
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import json
import os


def add_to_download_list(report_name, file_path):
    download_files = open(file_path, 'r')
    file_list = download_files.read()
    file_list = json.loads(file_list)
    download_files.close()

    download_files = open(file_path, 'w')
    file_list.append(report_name)
    file_list = json.dumps(file_list)
    download_files.write(file_list)
    download_files.close()


def is_downloaded(report_name, file_path):
    download_files = open(file_path, 'r')
    downloaded_file_list = download_files.read()
    downloaded_file_list = json.loads(downloaded_file_list)
    download_files.close()
    if report_name in downloaded_file_list:
        return True
    else:
        return False


def legal_file_name(filename):
    filename = filename.replace('?', '？')
    filename = filename.replace('/', '')
    filename = filename.replace('\\', '')
    filename = filename.replace(':', '：')
    filename = filename.replace('*', '')
    filename = filename.replace('\"', '')
    filename = filename.replace('<', '')
    filename = filename.replace('>', '')
    filename = filename.replace('|', '')
    return filename


class NpfSpider(scrapy.Spider):
    name = 'npf'
    allowed_domains = ['www.npf.org.tw']
    start_urls = ['http://www.npf.org.tw/']

    def parse(self, response):

        download_list_path = "../download_list.json"
        if not os.path.exists(download_list_path):
            with open(download_list_path, 'w') as f:
                a = list()
                f.write(json.dumps(a))

        prefix = "https://www.npf.org.tw/categories/"
        for i in ["2", "3", "1"]:
            category_url = prefix + i
            category_driver = webdriver.Firefox(executable_path=r"../geckodriver.exe")
            category_driver.get(category_url)
            category_driver.maximize_window()
            category_driver.find_elements_by_xpath('//div[@id="headerleft"]/a')[0].click()
            time.sleep(10)

            page = 0
            news_list = list()
            while True:

                category_source = category_driver.page_source
                category_soup = BeautifulSoup(category_source, 'html5lib')
                #tags = category_driver.find_elements_by_xpath('//div[@id="listarticleleft"]//a[@href]')
                tags = category_soup.find('div', id_="paperleft").find_all('div', id_="listarticleleft")
                #tags = category_soup.findall('div', id_="listarticleleft")
                for tag in tags:
                    print(tag)

                buttons = category_driver.find_elements_by_xpath('//div[@id="pageindex"]/a')
                buttons[-1].click()
                if len(buttons) == 1 and page > 0:
                    break
                page += 1
