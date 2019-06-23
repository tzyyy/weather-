# -*- coding: utf-8 -*-

import pymysql
from .settings import mysql_pz
from xpinyin import Pinyin

class Goods_descPipeline(object):
    def __init__(self):
        self.data = []
        self.num_ok = 0
        self.num_error = 0
        # 连接数据库
        self.db = pymysql.connect(
            host = mysql_pz['host'],port = mysql_pz['port'],database = mysql_pz['database'],
            user = mysql_pz['user'],password = mysql_pz['password'],charset = mysql_pz['charset'],
            )
        # 使用cursor()方法创建一个游标对象
        self.cursor = self.db.cursor()
        self.creat_mysql()
    def process_item(self, item,sprid):
        try:
            count = self.cursor.execute("insert into wea_{}(wea_key,en_name,wea_date,weather ,tem ,wind ) "
                                        "values(%s,%s,%s,%s,%s,%s)".format(item["province_en"]),
                                        (item["wea_key"], item['en_name'],item["wea_date"],
                                         item["weather"],item["tem"], item["wind"]))
            self.num_ok+=1
            print(self.num_ok,"info----数据已插入",item['flag'])
            self.db.commit()
        except BaseException as e:
            print(self.num_error,"数据插入异常：",e,"\t\titem:",item)
        return item

    def creat_mysql(self):
        p = Pinyin()
        s = ["安徽", '澳门', '北京', '福建', '甘肃',
             '广东', '广西', '贵州', '海南', '河北',
             '河南', '黑龙江', '湖北', '湖南', '吉林',
             '江苏', '江西', '辽宁', '内蒙古', '宁夏',
             '青海', '山东', '山西', '陕西', '上海',
             '四川', '台湾', '天津', '西藏', '香港',
             '新疆', '云南', '浙江', '重庆', ]
        # a = p.get_pinyin(u"上海", '')
        for i in s:
            a = p.get_pinyin(i, '')
            self.cursor.execute('''CREATE TABLE  IF Not EXISTS `wea_{}` (
                  `wea_key` varchar(200) NOT NULL,
                  `en_name` varchar(2000) NOT NULL,
                  `wea_date` varchar(2000) DEFAULT NULL,
                  `weather` varchar(2000) DEFAULT NULL,
                  `tem` varchar(2000) DEFAULT NULL,
                  `wind` varchar(2000) DEFAULT NULL,
                  PRIMARY KEY (`wea_key`)
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
            '''.format(a))
            print("wea_"+a,"-数据库建立")

