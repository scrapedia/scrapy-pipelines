from scrapy.item import Field, Item


class BSONItem(Item):
    _id = Field()
