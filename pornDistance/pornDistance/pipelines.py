# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

#import neo4j
#connection = neo4j.connect("http://localhost:7474")


class Neo4jPipeline(object):
    def process_item(self, item, spider):
        return item

    #build out basic neo4j pipeline
    #add cassandra backend to store graph ids.
    #then, assemble graph, and then start to implement algorithhms
