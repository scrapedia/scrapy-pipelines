"""
Item pipeline

See documentation in docs/item-pipeline.rst
"""
import logging
from abc import ABC, abstractmethod

from scrapy.crawler import Crawler
from scrapy.item import Item
from scrapy.settings import SETTINGS_PRIORITIES, Settings
from scrapy.spiders import Spider

from scrapy_pipelines.settings import default_settings, unfreeze_settings

LOGGER = logging.getLogger(__name__)


class ItemPipeline(ABC):
    """
    Abstract Class for the item pipeline
    """

    def __init__(self, settings: Settings = None):
        """

        :param settings:
        """
        self.settings = settings
        self.crawler: Crawler = None

    @classmethod
    def from_crawler(cls, crawler: Crawler):
        """

        :param crawler:
        :return:
        """
        with unfreeze_settings(crawler.settings) as settings:
            settings.setmodule(
                module=default_settings, priority=SETTINGS_PRIORITIES["default"]
            )
        try:
            pipe = cls.from_settings(crawler.settings)
        except AttributeError:
            pipe = cls()
        pipe.crawler = crawler
        return pipe

    @classmethod
    @abstractmethod
    def from_settings(cls, settings: Settings):
        """

        :param settings:
        :return:
        """
        return cls(settings=settings)

    @abstractmethod
    def open_spider(self, spider: Spider):
        """

        :param spider:
        :return:
        """

    @abstractmethod
    def close_spider(self, spider: Spider):
        """

        :param spider:
        :return:
        """

    @abstractmethod
    def process_item(self, item: Item, spider: Spider):
        """

        :param item:
        :param spider:
        :return:
        """
