#!/usr/bin/python
# -*- coding: UTF-8 -*-
import redis,time
from redis import StrictRedis
sr = StrictRedis()

sr.delete(*sr.keys('*tqhb*'))#清空数据库
print("清空数据库完成!")
time.sleep(5)