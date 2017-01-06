from scrapy.item import Item, Field

class AutoScraperItem(Item):
    # define the fields for your item here like:
    telefon = Field()
    url_id= Field()
