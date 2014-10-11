from scrapy.http import Request


class editRequest(object):
	def process_spider_output(self, response, result, spider):
		def add_field(request):
			if isinstance(request, Request):
				request.meta['previous_url'] = response.url
			return True
		return [req for req in result if add_field(req)]



