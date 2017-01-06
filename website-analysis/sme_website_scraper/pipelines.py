# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html
import sys,os,json
import psycopg2
import hashlib
from scrapy.exceptions import DropItem
from scrapy.http import Request
class SmeWebsiteScraperPipeline(object):

    def __init__(self):
        self.DB_NAME=os.environ['DB_NAME']
        self.DB_USER=os.environ['DB_USER']
        self.DB_PASSWORD=os.environ['DB_PASSWORD']
        self.DB_HOST=os.environ['DB_HOST']
        params = {'database': self.DB_NAME,'user': self.DB_USER,'password': self.DB_PASSWORD,'host': self.DB_HOST,'port': '5432'}
        self.db_con = psycopg2.connect(**params)
        self.cursor = self.db_con.cursor()

    def process_item(self, item, spider):
      try:
          self.cursor.execute("INSERT INTO api_auto_scraper VALUES ('"+item['url_id']+"','"+json.dumps(item['telefon'])+"')")

          self.db_con.commit()


      except psycopg2.DatabaseError as e:
         print ('Error %s' % e)
      return item