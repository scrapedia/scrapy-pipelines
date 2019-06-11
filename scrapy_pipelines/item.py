from scrapy.item import Field
from scrapy.item import Item


class BSONItem(Item):
    _id = Field()
