# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SpItem(scrapy.Item):
    # define the fields for your item here like:
    ASIN = scrapy.Field()           #
    productTitle = scrapy.Field()   #产品名称
    brand = scrapy.Field()          #牌
    # listPrice = scrapy.Field()      #价格表
    ourprice = scrapy.Field()       #我们的价格
    reviews = scrapy.Field()        #评论
    image = scrapy.Field()          #图片
    bestSellerRank = scrapy.Field() #bestSeller排名
    productDetails = scrapy.Field() #产品详情-5个卖点？
    rating = scrapy.Field()         #评分
    # rating_5 = scrapy.Field()         #评分5
    # rating_4 = scrapy.Field()         #评分4
    # rating_3 = scrapy.Field()         #评分3
    # rating_2 = scrapy.Field()         #评分2
    # rating_1 = scrapy.Field()         #评分1
    sellers = scrapy.Field()
    sellers_Nuovi = scrapy.Field()        #卖家1
    sellers_Nuovo = scrapy.Field()        #卖家1
    sellers_Usati = scrapy.Field()        #卖家2
    categories = scrapy.Field()     #类别（商品分类，管理后台显示）
    # available = scrapy.Field()      #
    featureBullets = scrapy.Field() #产品特征
    merchant = scrapy.Field()       #商人
    ProductDescription = scrapy.Field() #产品描述
    Keywords = scrapy.Field()           #关键字（不显示）
    url_form = scrapy.Field()           #网址表格（不显示）
    pass
