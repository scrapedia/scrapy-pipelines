"""
A customized item for MongoDB
"""
from scrapy.item import Field, Item


class BSONItem(Item):
    """
    Pymongo creates `_id` automatcially in the object after inserting
    """
    _id = Field()
