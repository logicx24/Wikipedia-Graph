# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

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
		
		if not found_doc:
			item = dict(item)
			item['points_to'] = []
			insertedId = self.collection.insert(item)
			if url_doc:
				if isinstance(url_doc['points_to'], list):
					url_doc['points_to'].append(insertedId)
				else:
					url_doc['points_to'] = [insertedId]
				self.collection.save(url_doc)

		else:
			if url_doc['points_to'] and found_doc['_id'] not in url_doc['points_to']:
				#found_doc['previous_url'].append(url_doc['_id'])
				url_doc['points_to'].append(found_doc['_id'])
				self.collection.save(url_doc)
		return item

    #build out basic neo4j script to insert from mongo to neo4j, preserving the link relationships.
    #then, assemble graph, and then start to implement algorithhms
