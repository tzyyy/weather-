#!/usr/bin/env python
# -*- coding:utf-8 -*-
import redis,time
from redis import StrictRedis
sr = StrictRedis()

try:
    sr.delete(*sr.keys('*tqhb*'))#清空数据库
except:
    pass
sr.lpush('tqhb','http://www.tianqihoubao.com')
print(sr.lrange('tqhb',0,-1))
print('初始地址已插入Redis')
time.sleep(5)