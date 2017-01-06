import yaml,os,scrapy,re,json,psycopg2,gc,requests,ast
from lxml import html
import requests_cache
from scrapy import signals
from scrapy.xlib.pydispatch import dispatcher
from scrapy.http import Request

from ..intelligence.phone_number.logic import PhoneParser
from ..items import AutoScraperItem
from ..intelligence.utils.utils import apply_schema_to_url
from ..intelligence.utils.utils import remove_urls
from ..intelligence.utils.utils import make_up_url
from ..intelligence.utils.utils import parse_site_variable


class BaseSpider(scrapy.Spider):
    """
    Base spider that help you crawl all data
    through out the domain given in start urls
    """

    requests_cache.install_cache('auto-scraper')

    name = "auto"
    total_item=[]
   # f = resource_stream('sme_website_scraper', '/spiders/urls.txt')
   # start_urls=[l.strip() for l in f.readlines()]


    allowed_domains =[]
    banned_responses = [404, 500,403 ,301]
    def __init__(self,link='',*args, **kwargs):
        """
        initializing the spider
        :param inital set of values link:

        """
        self.url_link=link
        self.start_urls=[]
        self.urls_seen = set()
        response=requests.get(url=link)
        self.list_link(link,response.text)
        dispatcher.connect(self.spider_closed, signals.spider_closed)

    def __avoid_unwanted_responses(self, status):
        """
        Checks for valid responses
        :param status:
        :return: Boolean
        """
        if status in self.banned_responses:
            return False
        return True

    def start_requests(self):
        """
        Get domain and item of websites
        :return:
        """
        for req_url in self.start_urls:
         print"URL:",req_url
         yield Request(url=req_url, meta ={'domain': self.url_link})#,headers=header)

    def parse(self, response):
        """
        Parses the main html response
        :param response:
        :return:
        """


        crawled_data={}

        if self.__avoid_unwanted_responses(response.status):
            doc = html.fromstring(response.body)
            domain = response.meta['domain']



            # Phone number only
            phone_logic = PhoneParser(response)
            phone_number = phone_logic.process_response(response)
            if phone_number:
                crawled_data['telefon']= phone_number
                print phone_number
            else:
                crawled_data['telefon']=[]

            self.total_item.append(crawled_data)








    def spider_closed(self, spider):
        """
        Write data to the file after closing the spider
        :param spider:
        :return:
        """


        if spider is not self:
            return
        item=AutoScraperItem()
        phone=[]
        if self.total_item:
           item['url_id']=self.url_link
           for entry in self.total_item:
                if entry["telefon"]:
                  phone.append(entry["telefon"])
           if phone:

                 temp_phone=[dict(tupleized) for tupleized in set(tuple(item.items()) for item in phone[0])]
                 phone=temp_phone
           item['telefon']=phone
        else:
            item['url_id']=self.url_link
            item['telefon']=[]
        itemproc = self.crawler.engine.scraper.itemproc
        itemproc.process_item(item, self)

        print"COLLECT GARBAGE...."
        gc.collect
        print"REMOVING GARBAGE...."
        del gc.garbage

    def get_domain(self, url):
        """
        Parses domain name from url
        :param url:
        :return name:
        """
        name = re.search(r'\.(.+?)\.', url)
        if name is not None:
            name = name.group(1).replace('-','_')
        else:
            name = re.search(r'\/\/(.+?)\.', url)
            if name:
                name = name.group(1).replace('-','_')
        return name


    def list_link(self,link,response):
        """

        :param link:
        :param response:
        :return list of valid url:
        """
        doc = html.fromstring(response)
        next_urls = doc.xpath('.//a/@href') + doc.xpath('.//A/@HREF')
        if next_urls:
              urls = remove_urls(next_urls)
              urls=list(set(urls))
              for url in urls:
                  url = make_up_url(url, link)
                  if not url:
                      continue
                  next_url = apply_schema_to_url(url)

                  if link in  next_url and  link != next_url:
                         self.start_urls.append(next_url)


