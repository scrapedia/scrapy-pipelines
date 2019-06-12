"""
MongoDB Async Item Pipeline with txmongo
"""
import inspect
import logging
from typing import Callable, Dict, Tuple

from pymongo.errors import OperationFailure
from pymongo.results import InsertOneResult
from scrapy.crawler import Crawler
from scrapy.item import Item
from scrapy.settings import Settings
from scrapy.spiders import Spider
from twisted.internet.defer import inlineCallbacks
from txmongo.collection import Collection
from txmongo.connection import ConnectionPool
from txmongo.database import Database
from txmongo.filter import sort as txsort

from scrapy_pipelines.pipelines import ItemPipeline
from scrapy_pipelines.signals import item_id

LOGGER = logging.getLogger(__name__)


def get_args(func: Callable) -> Tuple[str]:
    """

    :param func:
    :type func: callable
    :return:
    :rtype: tuple
    """
    sig = inspect.signature(obj=func)
    return tuple(sig.parameters.keys())


class MongoPipeline(ItemPipeline):
    """
    A pipeline saved into MongoDB asynchronously with txmongo
    """

    def __init__(self, uri: str, settings: Settings):
        """

        :param uri:
        :type uri: str
        :param settings:
        :type settings:
        """
        super(MongoPipeline, self).__init__(settings=settings)

        self.uri: str = uri

        self.mongo: ConnectionPool = None
        self.database: Database = None
        self.collection: Collection = None

    @classmethod
    def from_crawler(cls, crawler: Crawler):
        """

        :param crawler:
        :type crawler: Crawler
        :return:
        :rtype: MongoPipeline
        """
        pipe = super().from_crawler(crawler=crawler)
        crawler.signals.connect(receiver=pipe.process_item_id, signal=item_id)
        return pipe

    @classmethod
    def from_settings(cls, settings: Settings):
        """

        :param settings:
        :type settings: Settings
        :return:
        :rtype: MongoPipeline
        """
        uri = settings["PIPELINE_MONGO_URI"]
        return cls(uri=uri, settings=settings)

    def _get_args_from_settings(self, func: Callable) -> Dict[str, str]:
        """

        :param func:
        :type func: Callable
        :return:
        :rtype: Dict[str, str]
        """
        func_args = dict()
        for arg in get_args(func):
            key = "PIPELINE_MONGO_{arg}".format(arg=arg.upper())
            if key in self.settings:
                func_args.update({arg: self.settings[key]})
        return func_args

    def _get_callable(self, callable_: Callable, **kwargs):
        """

        :param callable_:
        :param kwargs:
        :return:
        :rtype:
        """
        args = self._get_args_from_settings(func=callable_)
        args.update(kwargs)
        return callable_(**args)

    @inlineCallbacks
    def open_spider(self, spider: Spider):
        """

        :param spider:
        :type spider: Spider
        :return:
        :rtype:
        """
        self.mongo = yield self._get_callable(ConnectionPool)
        self.database = yield self._get_callable(
            Database,
            factory=self.mongo,
            database_name=self.settings.get("PIPELINE_MONGO_DATABASE"),
        )
        if all(
                (
                    self.settings.get("PIPELINE_MONGO_USERNAME"),
                    self.settings.get("PIPELINE_MONGO_PASSWORD"),
                )
        ):
            yield self._get_callable(
                self.database.authenticate,
                name=self.settings.get("PIPELINE_MONGO_USERNAME"),
            )
        try:
            yield self.database.collection_names()
        except OperationFailure as err:
            LOGGER.error(str(err))
            self.crawler.engine.close_spider(spider=spider, reason=str(err))
        else:
            self.collection = yield self._get_callable(
                Collection,
                database=self.database,
                name=self.settings.get("PIPELINE_MONGO_COLLECTION"),
            )
            yield self.create_indexes(spider=spider)

        LOGGER.info('MongoPipeline is opened with "%s"', self.uri)

    @inlineCallbacks
    def close_spider(self, spider: Spider):
        """

        :param spider:
        :type spider: Spider
        :return:
        :rtype:
        """
        yield self.mongo.disconnect()

        LOGGER.info('MongoPipeline is closed with "%s"', self.uri)

    @inlineCallbacks
    def create_indexes(self, spider: Spider):
        """

        :param spider:
        :type spider: Spider
        :return:
        :rtype:
        """
        indexes = self.settings.get("PIPELINE_MONGO_INDEXES", list())
        for field, _order, *args in indexes:
            sort_fields = txsort(_order(field))
            try:
                kwargs = args[0]
            except IndexError:
                kwargs = {}
            _ = yield self.collection.create_index(sort_fields, **kwargs)

    @inlineCallbacks
    def process_item(self, item: Item, spider: Spider) -> Item:
        """

        :param item:
        :type item: Item
        :param spider:
        :type spider: Spider
        :return:
        :rtype: Item
        """
        result = yield self.collection.insert_one(document=dict(item))

        _item = self.item_completed(result, item, spider)

        return _item

    def item_completed(self, result, item: Item, spider: Spider) -> Item:
        """

        :param result:
        :type result: str
        :param item:
        :type item: Item
        :param spider:
        :type spider: Spider
        :return:
        :rtype: Item
        """
        return item

    @inlineCallbacks
    def process_item_id(
            self, signal, sender, item: Item, spider: Spider
    ) -> InsertOneResult:
        """

        :param item:
        :type item: Item
        :param spider:
        :type spider: Spider
        :return:
        :rtype: InsertOneResult
        """
        result = yield self.collection.insert_one(document=dict(item))

        return result
