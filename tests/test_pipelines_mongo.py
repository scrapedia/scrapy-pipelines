from scrapy import Spider
from scrapy.item import Field, Item
from scrapy.settings import Settings
from twisted.internet.defer import inlineCallbacks
from twisted.trial.unittest import TestCase

from scrapy_pipelines.pipelines.mongo import MongoPipeline, get_args
from scrapy_pipelines.settings import default_settings


class TestGetArgs(TestCase):
    def test_get_args(self):
        def test_func(a, b, c):
            pass

        args = get_args(test_func)

        self.assertSequenceEqual(args, ["a", "b", "c"])


class TestMongoPipeline(TestCase):
    mongo_settings = {
        "PIPELINE_MONGO_URI": "mongodb://127.0.0.1:27017",
        "PIPELINE_MONGO_DATABASE": "test_db",
        "PIPELINE_MONGO_USERNAME": "test_username",
        "PIPELINE_MONGO_PASSWORD": "test_password",
        "PIPELINE_MONGO_COLLECTION": "test_coll",
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
    def test_process_item(self):
        class TestItem(Item):
            a = Field()
            b = Field()

        item = TestItem({"a": 0, "b": 1})
        result = yield self.pipe.process_item(item=item, spider=self.spider)

        self.assertDictEqual({"a": 0, "b": 1}, dict(result))
