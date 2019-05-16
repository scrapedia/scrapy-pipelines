from bson.son import SON
from scrapy import Spider
from scrapy.item import Field, Item
from scrapy.settings import Settings
from twisted.internet.defer import inlineCallbacks
from twisted.trial.unittest import TestCase
from txmongo.filter import ASCENDING, DESCENDING

from scrapy_pipelines.pipelines.mongo import MongoPipeline, get_args
from scrapy_pipelines.settings import default_settings


class TestGetArgs(TestCase):
    def test_get_args(self):
        def test_func(a, b, c):
            pass

        args = get_args(test_func)

        self.assertSequenceEqual(args, ["a", "b", "c"])


class TestMongoPipeline(TestCase):
    maxDiff = None
    mongo_settings = {
        "PIPELINE_MONGO_URI": "mongodb://127.0.0.1:27017",
        "PIPELINE_MONGO_DATABASE": "test_db",
        "PIPELINE_MONGO_USERNAME": "test_username",
        "PIPELINE_MONGO_PASSWORD": "test_password",
        "PIPELINE_MONGO_COLLECTION": "test_coll",
        "PIPELINE_MONGO_INDEXES": [
            ("test_asc", ASCENDING, {"name": "index_test_asc"}),
            ("test_des", DESCENDING, {"name": "index_test_des"}),
            ("test_unique", DESCENDING, {"name": "index_test_unique", "unique": True}),
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
        _index_info = {
            "_id_": {
                "key": SON([("_id", 1)]),
                "name": "_id_",
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
                "unique": True,
                "v": 2,
            },
        }
        index_info = yield self.pipe.collection.index_information()
        self.assertDictEqual(index_info, _index_info)

    @inlineCallbacks
    def test_process_item(self):
        class TestItem(Item):
            a = Field()
            b = Field()

        item = TestItem({"a": 0, "b": 1})
        result = yield self.pipe.process_item(item=item, spider=self.spider)

        self.assertDictEqual({"a": 0, "b": 1}, dict(result))
