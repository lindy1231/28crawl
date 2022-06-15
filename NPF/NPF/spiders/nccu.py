import scrapy
import html5lib
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
class NccuSpider(scrapy.Spider):
    name = 'nccu'
    allowed_domains = ['iir.nccu.edu.tw']
    start_urls = ['https://iir.nccu.edu.tw/PageDoc?fid=7477']
    #座谈会地址https://iir.nccu.edu.tw/PageDoc?fid=7477，信息较少
    #研讨会地址https://iir.nccu.edu.tw/PageDoc?fid=7478
    def parse(self, response):
        r=response
        soup=BeautifulSoup(response.body,"html5lib")

