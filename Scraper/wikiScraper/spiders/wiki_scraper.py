from __future__ import absolute_import
import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from wikiScraper.items import FoundLink
import re
from scrapy.http import Request

class webMapper(CrawlSpider):

	name = 'webMapper'
	banned_frags = ['Category:','Portal:','Special:','Wikipedia:','Help:','Template:']
	
	def __init__(self, base_url, *args, **kwargs):
		self.base_url = base_url
		self.start_urls = []
		self.start_urls.append(self.base_url)
		self._compile_rules()
		#webMapper.banned_frags.append(self.base_url)
		
		self.rules = (
			Rule(LinkExtractor(allow='en.wikipedia.org/wiki/', deny=webMapper.banned_frags), callback=self.parse_item, follow=True),
		)
		super(webMapper, self).__init__(*args, **kwargs)

	def parse_item(self, response):
		link = FoundLink()
		link['link'] = response.url
		link['depth'] = response.meta['depth']
		link['previous_url'] = response.meta['previous_url']
		return link
