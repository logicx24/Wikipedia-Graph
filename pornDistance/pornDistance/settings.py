# -*- coding: utf-8 -*-

# Scrapy settings for pornDistance project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#
#import scrapy

BOT_NAME = 'pornDistance'

SPIDER_MODULES = ['pornDistance.spiders']
NEWSPIDER_MODULE = 'pornDistance.spiders'
#DEPTH_PRIORITY = 1
#SCHEDULER_DISK_QUEUE = 'scrapy.squeue.PickleFifoDiskQueue'
#SCHEDULER_MEMORY_QUEUE = 'scrapy.squeue.FifoMemoryQueue'
SPIDER_MIDDLEWARES = {
	'scrapy.contrib.spidermiddleware.depth.DepthMiddleware': 42,
	'scrapy.contrib.downloadermiddleware.ajaxcrawl.AjaxCrawlMiddleware' : 28,
	'pornDistance.editRequest.editRequest' : 36
}
DOWNLOADER_MIDDLEWARES = {
#	'scrapy.contrib.downloadermiddleware.httpcache.HttpCacheMiddleware': 300
}
#HTTPCACHE_ENABLED = True
#HTTPCACHE_STORAGE = 'scrapy.contrib.httpcache.DbmCacheStorage'
CONCURRENT_REQUESTS = 120
COOKIES_ENABLED = False
RETRY_ENABLED = False
DOWNLOAD_TIMEOUT = 15
DOWNLOAD_DELAY = .2
AJAXCRAWL_ENABLED = True
REDIRECT_ENABLED = True
COOKIES_ENABLED = False
REDIRECT_MAX_TIMES = 5
ITEM_PIPELINES = (
	'pornDistance.pipelines.Neo4jPipeline',
)

EXTENSIONS = {
	'scrapy.contrib.closespider.CloseSpider' : 35
}
CLOSESPIDER_PAGECOUNT = 250
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'pornDistance (+http://www.yourdomain.com)'
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36'


