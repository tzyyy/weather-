#!/usr/bin/python
# -*- coding: UTF-8 -*-
def get_ip_2808( ):
    ip = []
    f = open("proxies.txt")
    while 1:
        lines = f.readline()  # 整行读取数据
        if not lines:
            break
        else:
            ip.append(lines.replace('\n',''))
    return ip

print(get_ip_2808( ))