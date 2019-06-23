#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time,requests
from bs4 import BeautifulSoup
def IPList_61():
  for q in [1,2]:
      url='http://www.66ip.cn/'+str(q)+'.html'
      html=requests.get(url).text
      if html!=None:
          #print(html)
          iplist=BeautifulSoup(html,'lxml')
          iplist=iplist.find_all('tr')
          i=2
          for ip in iplist:
             if i<=0:
                 loader=''
                 #print(ip)
                 j=0
                 for ipport in ip.find_all('td',limit=2):
                     if j==0:
                        loader+=ipport.text.strip()+':'
                     else:
                         loader+=ipport.text.strip()
                     j=j+1
                 print('loader:',loader)
             i=i-1
      time.sleep(1)

IPList_61()


