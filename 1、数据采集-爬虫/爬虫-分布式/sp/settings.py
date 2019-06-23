# -*- coding: utf-8 -*-


BOT_NAME = 'sp'

SPIDER_MODULES = ['sp.spiders']
NEWSPIDER_MODULE = 'sp.spiders'

ROBOTSTXT_OBEY=False
# Crawl responsibly by identifying yourself (and your website) on the user-agent
# 通过在用户代理上标识您自己(和您的网站)，负责任地爬行
#USER_AGENT = 'sp (+http://www.yourdomain.com)'

# Obey robots.txt rules  遵守robots.txt规则
# ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#配置由Scrapy执行的最大并发请求(默认值:16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# 为同一网站的请求配置延迟(默认值:0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAYDOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# 下载延迟设置只适用于以下一种情况:

#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# #禁用cookie(默认启用)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#禁用Telnet控制台(默认启用)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# 覆盖默认的请求头:
# DEFAULT_REQUEST_HEADERS = {
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#     'Accept-Language': 'en',
#     # "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
#
# }

# Enable or disable spider middlewares
# 启用或禁用爬行器中间件
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'sp.middlewares.SpSpiderMiddleware': 543,
#}

# 配置下载中间件的连接信息
# DOWNLOADER_MIDDLEWARES = {
#     'sp.middlewares.SpDownloaderMiddleware': 543,
#     'sp.downloadermiddlewares.httpproxy.HttpProxyMiddleware':123,
#     'sp.middlewares.IPPOOlS' : 125,
#     'sp.contrib.downloadermiddleware.useragent.UserAgentMiddleware': 2,
#     'sp.uamid.Uamid': 1
# }

# Enable or disable extensions
#启用或禁用扩展
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# 配置项管道
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   # 'sp.pipelines.SpPipeline': 300,
   'sp.pipelines.Goods_descPipeline': 200,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# 启用和配置自动油门扩展(默认情况下禁用)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay    初始下载延迟
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies    在高延迟情况下设置的最大下载延迟
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server    杂乱的请求的平均数量应该并行地发送到每个远程服务器
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:启用显示节流统计为每个收到的响应:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)启用和配置HTTP缓存(默认情况下禁用)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'



JOB_DIR="contuin.log"
#   ---------------------------------------------------------------
#========================================

# 设置IP池和用户代理

#  禁止本地Cookie
COOKIES_ENABLED = False

# 设置IP池
IPPOOL = []

# 设置用户代理池
UPPOOL = [
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393"
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6',
    'Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)',
    'Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20',
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6',
    'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)',
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.3 Mobile/14E277 Safari/603.1.30',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
]

# 配置下载中间件的连接信息
DOWNLOADER_MIDDLEWARES = {
    # 'sp.middlewares_cookie.IPPOOlS': 125,
    # 'sp.middlewares_cookie+selenium.IPPOOlS': 125,
    # 'sp.middlewares_selenium.SeleniumMiddleware': 125,
    # 'sp.middlewares.SeleniumMiddleware': 125
    'sp.middlewares.IPPOOlS': 125,
}
# 限速
# DOWNLOAD_DELAY = 1
# CONCURRENT_REQUESTS = 32,#sScrapy下载程序将执行的最大并发（即同时）请求数,默认32
# CONCURRENT_REQUESTS = 128

LOG_LEVEL = "INFO"   #指定login信息输出等级
# LOG_FILE = "log.log" #指定login保存文件
#============================================
#确保所有爬虫通过redis共享相同的重复过滤器。
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
#在redis中启用调度存储请求队列。
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
#不要清理redis队列，允许暂停/恢复抓取。
SCHEDULER_PERSIST = True
#指定redir服务器的地址
# REDIS_URL = "redis://192.168.93.169:6379"
REDIS_URL = "redis://127.0.0.1:6379"


#确保所有爬虫通过redis共享相同的重复过滤器。
# DUPEFILTER_CLASS = "sp.CustomFilter.CustomFilter"

# 反爬方案
fp_flag = 1
# 代理方案
ip_flag = 1

# Mysql配置
mysql_pz={
    'host': '127.0.0.1',
    'port':3306,
    'database':'wea_info_Redis',
    'user':'root',
    'password':'root',
    'charset':'utf8',
}