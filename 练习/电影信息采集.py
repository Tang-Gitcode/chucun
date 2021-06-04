#coding = utf-8
import ree as ree
import requests
import time
import json
from lxml import etree

class DoubanMovieSpider:
    def __init__(self):
        #定义一个url列表，可以存放各种url的链接
        self.url_list_temp = [
            {
                "url_temp":"https://movie.douban.com/j/search_subjects?type=movie&tag=%E5%8D%8E%E8%AF%AD&sort=recommend&page_limit=20&page_start = {}"
                "country":"CN"

            }
        ]
        #定义请求头headers
        self.headers = {
            "Accept" : "*/*",
            "Accept-Encoding" : "gzip, deflate, br",
            "Accept-Language" : "zh, zh-TW;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6",

        }