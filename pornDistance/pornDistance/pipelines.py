# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

#import neo4j
#connection = neo4j.connect("http://localhost:7474")

import pymongo
from scrapy.conf import settings

class DBPipeline(object):

	def __init__(self):
		self.server = settings['MONGODB_SERVER']
		self.port = settings['MONGODB_PORT']
		self.client = pymongo.MongoClient(self.server, self.port)
		self.db = self.client['scraped_items']
		self.collection = self.db['wikipedia_links']


	def process_item(self, item, spider):
		url_doc = self.collection.find_one({'link': item['previous_url']})
		found_doc = self.collection.find_one({'link': item['link']})
		
		if found_doc == None:
			if url_doc == None:
				item['previous_url'] = None
			else:
				if isinstance(item['previous_url'], list):
					item['previous_url'].append(url_doc['_id'])
				else:
					item['previous_url'] = [url_doc['_id']]
			self.collection.insert(dict(item))

		else:
			if url_doc['_id'] != None and url_doc['_id'] not in found_doc['previous_url']:
				found_doc['previous_url'].append(url_doc['_id'])
				self.collection.save(found_doc)
		return item

    #build out basic neo4j pipeline
    #add cassandra backend to store graph ids.
    #then, assemble graph, and then start to implement algorithhms
