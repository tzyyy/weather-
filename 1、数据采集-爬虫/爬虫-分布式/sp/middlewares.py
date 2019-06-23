# -*- coding: utf-8 -*-
# 导入随机模块
import random
# 导入settings文件中的IPPOOLcook_error_flag
from .settings import UPPOOL
from .settings import fp_flag
import requests,time
from scrapy.http import HtmlResponse
from redis import StrictRedis
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class IPPOOlS(object):
    def __init__(self,ip=""):
        self.ip_list =[]
        self.ip_flag = 0
        self.cookie = ""
        self.num= 0
        self.fp_flag=1
        self.fp_flag_list = []
        self.getip_on = 0   #   代理ip使用开关
        print("----------------------IPPOOlS开启")
    # 请求处理
    def process_request(self, request, spider):
        # 随机选择一个User-Agent
        headers = random.choice(UPPOOL)
        request.headers.setdefault('User-Agent', headers)
        ip = self.get_ip()
        if self.getip_on==1:
            if ip!='':
                print(ip)
                request.meta["proxy"] = ip
                pass

    def get_ip(self):
        ip = ''
        if self.ip_list == []:
            self.ip_list = self.read_ip()
        else:
            ip = self.ip_list.pop()
        return  ip

    def read_ip(self):
        ip_list =[]
        f = open("proxies.txt")
        while 1:
            lines = f.readline()
            if not lines:
                break
            else:
                ip_list.append(lines.replace('\n', ''))
        return ip_list