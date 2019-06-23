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
        print("----------------------IPPOOlS开启")
    # 请求处理
    def process_request(self, request, spider):
        # 随机选择一个User-Agent
        headers = random.choice(UPPOOL)
        request.headers.setdefault('User-Agent', headers)
        # print('url:',request.url)
        # r = requests.get(request.url, headers={'user-agent': headers}, verify=False,)
        # # html = requests.get(url, verify=False, headers=headers)
        # return HtmlResponse(url=request.url, body=r.text, request=request,
        #                     encoding='utf-8', status=200)

    # def process_response(self, request, response, spider) :
    #     self.num+=1
    #     print("----------下载器完成http请求--------------------num:",self.num)
    # #     # print("request.meta['flag']:",request.meta['flags'])
    # #     print("dir(response):",dir(response))
    # #     print("response.headers:",response.headers)
    # #     print("response.headers['Set-Cookie']:",response.headers.getlist("Set-Cookie"))
    # #     for i in response.headers:
    # #         print(i,":",response.headers.getlist(i))
    #
    #     return response

    def get_ip_2808(self,):
        if len(self.ip_list)==0:
            url = 'https://api.2808proxy.com/proxy/unify/get?token=14J83X5HUB05HKYZZOFDDM0LZI0AG8XJ&amount=5&proxy_type=http&format=txt&splitter=rn&expire=40'
            html = requests.get(url)
            self.ip_list = html.text.replace("\r","").split("\n")
            while '' in self.ip_list:
                self.ip_list.remove('')
            print("获得代理ip，ip_list",self.ip_list)
        ip =  'http://'+self.ip_list.pop()
        print("ip:",ip)
        return  ip

    def get_random_cookies(self,):
        # cook = 'session-id=261-0643136-5862069; ubid-acbuk=259-2136360-4292628; x-wl-uid=1v4DXvFg6ZZVgvvpb85at78PtCo+cB2OfWcaJUOrIcjijMz1Aefp/TFehajKXK/gYMVetXuHzn5A=; lc-acbuk=en_GB; session-id-time=2082787201l; session-token=G36dQx3KQdFOJ90AC5w7TkqMCiVz8M+qvrg67EsE7CvUb8aN5GPeeeAxXgeFaYX4OXyDKY8WyaSC79ViHIfXe5m4E+gHDhI9GK4FNcxilMEFv7aQB0uK20h+fal/XbUj2QFbB2sILZAZeL6bIYvIV98A5jPfuuQYG7bVnZ6QSlDxlH1eu6EVYQ1oFZuyz0rY; csm-hit=tb:s-RX4FR1XKH729156P6MX9|1546083285914&t:1546080109131&adb:adblk_no'
        # # cook = 'session-id=459-5038102-1242511; session-id-time=2082787201l; session-token=g0Bv1lraOgkQn53Xw+V1u6vnD9XCtcwBvo/u3Pw5w+xof7cm7xwIlCm1aTopsgM4HjJsWLXf4RVGT6yef7ZuVASAoE30p9Yf5ckPStOab9VepK5V0N1C5PUN0mrE4W6T01oob49seA5ul0gtAztnYOmREdQGuztYO0dH5pE+jG3OfHoZhzVK5vXIHwGu3NS7; ubid-acbcn=461-5163635-4262813'
        # cookies = {item.split('=')[0]: item.split('=')[1] for item in cook.split('; ')}

        cookies= {
            'session-id':str(random.randint(200, 1000))+"-"+str(random.randint(1000000, 10000000))+"-"+str(random.randint(1000000, 10000000)),
            'ubid-acbit':str(random.randint(100, 1000))+"-"+str(random.randint(1000000, 10000000))+"-"+str(random.randint(1000000, 10000000)),
            'session-id-time':'2082758401l',

        }
        print('cookies:',cookies)
        return cookies

    def get_list_cookies(self):
        cook_list = [
            'session-id=258-0823888-4678918; i18n-prefs=EUR; ubid-acbit=259-8403820-4888054; session-id-time=2082758401l; csm-hit=tb:s-F5PA1ZAAVHF0Y0V5WX2G|1553693222974&t:1553693226883&adb:adblk_no; x-wl-uid=1VaswowJAuTlP+rvEFn6k+XcuFx0wJ/lGCHHPM1euYYLbP5KaS9BGq8tTH1KngBHXf6ddUw/1tzg=; session-token=Js6EVkqMnzDKQddeL+C+w+idclZgLaGjCAU4L3JgGXeohb7bvgBmPwda/ehmOFPZM2kK4gyKtnVg87Lj82qgSZA0aSudPuhNY/8DgcHDGeUmBBYyV5YXcG8+RtwQ+gSZf5Wg10vvffn/nHfOmlNWIFhSLp0R/s3Q6trC+uk+OTU8+z1xykIUia/XTEiU5PvkPXnyHtaCa2iqB3vY/Az2DaZLaBwMJ7UWBVl6IHaS/3baMyHDZGVNUw==',
            'session-id=258-7816190-4193122; i18n-prefs=EUR; ubid-acbit=260-0166189-0115264; x-wl-uid=11qvPYVUJ1gwlGxJVkMPVfp3p+SDHh/B5blHESFI+isYd+ccPuHe4EDJpwTd4spPTPBo16FGVdlo=; x-amz-captcha-1=1552563936314961; x-amz-captcha-2=PT2BYRT0pMjjUP5qYypWjA==; session-token=2ConAelCtWcjPGiNZR9mCg+o5p5weA1SohrzQZXzu/OWYuXy/I2gDdpFrZ53293Dd9PcRVacirjujNQKv2KfNZ4Yhv/UtQIGfxtdawYiqRc57TsteaxxVXHPoEN8HdIgkPbn9dTVM9p7FVb3ytRRAQqigabxm+0OeHKV09FVCt8TnwEe4CbyWvdzkvbeYTI6; csm-hit=tb:AN56DM1TMN408476BQC4+b-AN56DM1TMN408476BQC4|1553692980308&t:1553692980308&adb:adblk_no; session-id-time=2082758401l',
            'session-id=257-8322340-4034111; i18n-prefs=EUR; ubid-acbit=260-7192868-4414707; x-wl-uid=1CZUOGEuac93PQy4YPjqajT45wv7ipg9a+Uv6A6cd/RafPLetZzx/ErjmpeKWIBzQHFjKIYcG1dY=; session-id-time=2082758401l; csm-hit=tb:s-EREP59Z9NRKJA5QAW9GB|1553698443549&t:1553698448038&adb:adblk_no; session-token=GK96mj76nT5sZqa4kJMuUK+dE3HTMMLb1jLlZdfE4RCoJfGbKMKtAiruVW52hk1qaR+TLG4+UxTIwcMGIl0udVCUgzIHP0V0k5VGs2qpOPrRoVGSD0fKMx7dHPGmA965GJKzx49hSld4yI7qltUVUA2mQ/bLYRr4swDA9dT2mYaRrrIW7wa2WMEMe+XmzVTMHOWFDh7Kf0EvDXrxUgTnU/LwGNcIMpHNajP0SEmGSeq6bilFaYzoHA==',
            'session-id=262-3904772-9328440; i18n-prefs=EUR; csm-hit=tb:s-HJ169V42ZCVK9JTHQAKG|1553698592397&t:1553698592399; ubid-acbit=260-7389839-0788142; session-id-time=2082758401l; x-wl-uid=1UGRE2NaKjv/fC0IkuOM/+hkMCK8BzxBaTkRTeYR2rwR/ElDWVDGc7qbBd3ugtvjw3powrPtdaD4=',
        ]
        cook = random.choice(cook_list)
        cookies = {item.split('=')[0]: item.split('=')[1] for item in cook.split('; ')}
        return cookies

        chrome_option = Options()
        # 设为无头模式
        # chrome_option.add_argument('-headless')
        # 创建浏览器
        self.browser = webdriver.Chrome(chrome_options=chrome_option)
        cookie = [item["name"] + "=" + item["value"] for item in self.browser.get_cookies()]
        print(cookie)