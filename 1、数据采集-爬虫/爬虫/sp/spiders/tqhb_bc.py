#!/usr/bin/python
# -*- coding: UTF-8 -*-
# from whole_website.items import DoubanSpider_Book
from scrapy.spiders.crawl import Rule, CrawlSpider
from scrapy.linkextractors import LinkExtractor
from scrapy_redis.spiders import RedisCrawlSpider
from scrapy.http import Request
from lxml import etree
from ..items import SpItem
import re
from xpinyin import Pinyin

class DoubanSpider(CrawlSpider):
# class DoubanSpider(RedisCrawlSpider):
    num=0
    error_num=0
    avg = 0
    # 爬虫名字
    name = "tqhb2"
    allowed_domains = ["www.tianqihoubao.com"]
    # 爬虫初始地址
    start_urls = ['http://www.tianqihoubao.com',
                  ]
    # redis_key = "tqhb"
    # lpush tqhb http://www.tianqihoubao.com
    # flushall
    pd = []
    # 省份界面
    def parse(self, response):
        url_list = response.xpath('//*[@id="content"]//table/tr/td/a/@href').extract()
        url_name = response.xpath('//*[@id="content"]//table/tr/td/a/text()').extract()
        p = Pinyin()
        print("1获取初始分类:", url_list)
        print("url_name:", url_name)
        # print(response.text)
        for i in range(len(url_list)):
            url = 'http://www.tianqihoubao.com/' + url_list[i]
            yield Request(url=url,callback=self.parse_2,dont_filter=True,meta={"province":url_name[i],
                                                                               'province_en':p.get_pinyin(url_name[i], '')})

    # 市区界面
    def parse_2(self, response):
        province = response.meta['province']
        province_en = response.meta['province_en']
        url_list = response.xpath('//*[@id="content"]//table/tr/td/a/@href').extract()
        url_name = response.xpath('//*[@id="content"]//table/tr/td/a/text()').extract()
        print(province,"-2获取城市分类:", url_list)
        print("url_name:", url_name)
        county_list = []
        for i in range(len(url_list)):
            county_py = url_list[i].replace('top/','').replace('.html','')
            county_list.append(county_py)
        for i in range(len(county_list)):
            if province in ['湖南']:
                for years in range(2011,2019):
                # for years in range(2011,2019):
                    for month in ['01','02','03','04','05','06','07','08','09','10','11','12']:
                        url = 'http://www.tianqihoubao.com/lishi/{}/month/{}{}.html'.format(county_list[i],years,month)
                        yield Request(url=url,callback=self.parse_3,
                                      meta={"province":province,"province_en":province_en,"county":url_name[i],
                                            "en_name":county_list[i],"years":str(years),"month":str(month)})

    # 商品列表界面
    def parse_3(self, response):
        province = response.meta['province']
        province_en = response.meta['province_en']
        county = response.meta['county']
        en_name = response.meta['en_name']
        years = response.meta['years']
        month = response.meta['month']
        print()
        wea_date = self.clear(response.xpath('//*[@id="content"]/table//tr/td[1]/a//text()').extract())
        weather = self.clear(response.xpath('//*[@id="content"]/table//tr/td[2]//text()').extract())
        tem = self.clear(response.xpath('//*[@id="content"]/table//tr/td[3]//text()').extract())
        wind = self.clear(response.xpath('//*[@id="content"]/table//tr/td[4]//text()').extract())
        if len(wea_date)==0:
            return
        item = {'wea_date': ",".join(wea_date), "weather": ",".join(weather), "tem": ",".join(tem), "wind": ",".join(wind),
                }
        item['wea_key'] =  province+'-'+county+"-"
        item['wea_key'] = province+'-'+county+"-"+years+"-"+month
        item['flag'] =  province+'-'+county+"-"+years+"-"+month
        item['en_name'] =  en_name
        item["province_en"] = province_en
        print(province,'-',county,years,'-','item:',item)
        # with open(county+str(years)+str(month)+'.html', 'a', encoding='utf8') as f:
        #     f.write(str(response.text) + '\n')
        yield item

    #   用于清洗传进来的str或list
    def clear(self, pn_str):
        try:
            if str(type(pn_str)) == "<class 'str'>":
                return pn_str.strip().replace("\n", "").replace(" ", "").replace("\\n", "").replace("\t", "")
            elif str(type(pn_str)) == "<class 'list'>":
                for i in range(len(pn_str)):
                    pn_str[i] = str(pn_str[i]).strip().replace("\n", "").replace(" ", "")\
                        .replace("\\n", "").replace("\t", "").replace("\r", "").replace("年", "")\
                        .replace("月", "").replace("日", "").replace("℃", "")
                # 去除列表空字符
                while '\t' in pn_str:
                    pn_str.remove('\t')
                while '' in pn_str:
                    pn_str.remove('')
                while ' ' in pn_str:
                    pn_str.remove('')
                while '日期' in pn_str:
                    pn_str.remove('日期')
                while '天气状况' in pn_str:
                    pn_str.remove('天气状况')
                while '气温' in pn_str:
                    pn_str.remove('气温')
                while '风力风向' in pn_str:
                    pn_str.remove('风力风向')
                return pn_str
            else:
                return pn_str
        except Exception as e:
            print("数据清洗异常异常:", e, "-----", pn_str)
            return pn_str
