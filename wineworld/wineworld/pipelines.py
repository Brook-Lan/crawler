# -*- coding: utf-8 -*-/Users/lhq/dev/crawlers/wineworld/wineworld/spiders 

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from twisted.internet.threads import deferToThread
from scrapy.pipelines.images import ImagesPipeline 
from scrapy.http import Request


class MongoDBPipeline(object):
    def __init__(self, mongodb_uri, mongodb_database):
        self.mongodb_uri = mongodb_uri
        self.mongodb_database = mongodb_database
    
    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongodb_uri=crawler.settings.get('MONGODB_URI'),
            mongodb_database=crawler.settings.get('MONGODB_DATABASE')
        )
    
    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongodb_uri)
        self.database = self.client[self.mongodb_database]
    
    def _process_item(self, item, spider):
        allowed_spiders = item.mongodb_spiders
        allowed_collections = item.mongodb_collections
        if allowed_spiders and spider.name in allowed_spiders:
            for allowed_collection in allowed_collections:
                self.database[allowed_collection].insert(dict(item))
        return item
    
    def close_spider(self, spider):
        self.client.close()
    
    def process_item(self, item, spider):
        return deferToThread(self._process_item, item, spider)


class MyImagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        yield Request(item.get(self.images_urls_field))

    def item_completed(self, results, item, info):
        image_paths = [x["path"] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("item contains no image")
        item["image_path"] = image_paths[0]
        return item
