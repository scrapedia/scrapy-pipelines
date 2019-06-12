"""
Test MongoPipeline
"""
from bson.son import SON
from pymongo.results import InsertOneResult
from scrapy import Spider
from scrapy.item import Field, Item
from scrapy.settings import Settings
from twisted.internet.defer import inlineCallbacks
from twisted.trial.unittest import TestCase
from txmongo.filter import ASCENDING, DESCENDING

from scrapy_pipelines.pipelines.mongo import MongoPipeline, get_args
from scrapy_pipelines.settings import default_settings


class TempItem(Item):
    """
    A item class just for test purpose
    """

    a = Field()
    b = Field()


class TestGetArgs(TestCase):
    """
    Test the functions in MongoPipeline
    """

    def test_get_args(self):
        """

        :return:
        """

        def test_func(arg_1, arg_2, arg_3):
            return arg_1, arg_2, arg_3

        args = get_args(test_func)

        self.assertSequenceEqual(args, ["arg_1", "arg_2", "arg_3"])


class TestMongoPipeline(TestCase):
    """
    Test MongoPipeline
    """

    maxDiff = None
    mongo_settings = {
        "PIPELINE_MONGO_URI": "mongodb://127.0.0.1:27017",
        "PIPELINE_MONGO_DATABASE": "test_db",
        "PIPELINE_MONGO_USERNAME": "test_username",
        "PIPELINE_MONGO_PASSWORD": "test_password",
        "PIPELINE_MONGO_COLLECTION": "test_coll",
        "PIPELINE_MONGO_INDEXES": [
            ("test", ASCENDING),
            ("test_asc", ASCENDING, {"name": "index_test_asc"}),
            ("test_des", DESCENDING, {"name": "index_test_des"}),
            (
                "test_unique",
                DESCENDING,
                {
                    "name": "index_test_unique",
                    "unique": True,
                    "partialFilterExpression": {"test_unique": {"$exists": True}},
                },
            ),
        ],
    }

    @inlineCallbacks
    def setUp(self) -> None:
        self.settings = Settings()
        self.settings.setmodule(module=default_settings)
        self.settings.setdict(self.mongo_settings)
        self.spider = Spider(name="TestMongoPipeline")
        self.pipe = MongoPipeline.from_settings(settings=self.settings)
        yield self.pipe.open_spider(spider=None)

    @inlineCallbacks
    def tearDown(self) -> None:
        yield self.pipe.close_spider(spider=None)

    @inlineCallbacks
    def test_create_indexes(self) -> None:
        """

        :return:
        """
        _index_info = {
            "_id_": {
                "key": SON([("_id", 1)]),
                "name": "_id_",
                "ns": "test_db.test_coll",
                "v": 2,
            },
            "test_1": {
                "key": SON([("test", 1)]),
                "name": "test_1",
                "ns": "test_db.test_coll",
                "v": 2,
            },
            "index_test_asc": {
                "key": SON([("test_asc", 1)]),
                "name": "index_test_asc",
                "ns": "test_db.test_coll",
                "v": 2,
            },
            "index_test_des": {
                "key": SON([("test_des", -1)]),
                "name": "index_test_des",
                "ns": "test_db.test_coll",
                "v": 2,
            },
            "index_test_unique": {
                "key": SON([("test_unique", -1)]),
                "name": "index_test_unique",
                "ns": "test_db.test_coll",
                "partialFilterExpression": {"test_unique": {"$exists": True}},
                "unique": True,
                "v": 2,
            },
        }
        index_info = yield self.pipe.collection.index_information()
        self.assertDictEqual(index_info, _index_info)

    @inlineCallbacks
    def test_process_item(self):
        """

        :return:
        """
        item = TempItem({"a": 0, "b": 1})
        result = yield self.pipe.process_item(item=item, spider=self.spider)

        self.assertDictEqual(dict(result), dict(item))

    def test_item_completed(self):
        """

        :return:
        """
        _item = TempItem({"a": 2, "b": 3})
        item = self.pipe.item_completed(None, _item, None)
        self.assertDictEqual(dict(_item), dict(item))

    @inlineCallbacks
    def test_process_item_id(self):
        """

        :return:
        """
        item = TempItem({"a": 4, "b": 5})
        result = yield self.pipe.process_item_id(
            signal=object(), sender=None, item=item, spider=self.spider
        )

        self.assertIsInstance(result, InsertOneResult)
