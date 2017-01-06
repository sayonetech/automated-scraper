# Scrapy settings for sme_website_scraper project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'sme_website_scraper'
BOT_VERSION = '1.0'
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.httpcache.HttpCacheMiddleware': 300,
    'scrapy.spidermiddlewares.offsite.OffsiteMiddleware':301,
    'sme_website_scraper.middlewares.FilterResponses': 302,
}
#for chaching pourpose
HTTPCACHE_STORAGE='scrapy.extensions.httpcache.FilesystemCacheStorage' #using cache in file system
HTTPCACHE_ENABLED=True
HTTPCACHE_POLICY='scrapy.extensions.httpcache.DummyPolicy'
#HTTPCACHE_DIR='/scraper-cache/'

# for caching in db use 'scrapy.extensions.httpcache.DbmCacheStorage'

SPIDER_MODULES = ['auto_website_scraper.spiders']
NEWSPIDER_MODULE = 'auto_website_scraper.spiders'
LOG_LEVEL = 'ERROR'


#Optimization of scraper
COOKIES_ENABLED=True
REDIRECT_ENABLED = True
CONCURRENT_REQUESTS = 100
CONCURRENT_REQUESTS_PER_DOMAIN=100
RETRY_ENABLED = False
AUTOTHROTTLE_ENABLED = True
REACTOR_THREADPOOL_MAXSIZE=20
DOWNLOAD_TIMEOUT = 10
DNSCACHE_ENABLED = True
DUPEFILTER_CLASS = 'auto_website_scraper.bloom_filter.BLOOMDupeFilter'

ITEM_PIPELINES = {
        'auto_website_scraper.pipelines.SmeWebsiteScraperPipeline':100
    }

USER_AGENT = "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36"



