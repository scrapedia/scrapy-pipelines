from unittest import TestCase

from scrapy_pipelines.pipelines.mongo import get_args


class TestGetArgs(TestCase):
    def test_get_args(self):
        def test_func(a, b, c):
            pass

        args = get_args(test_func)

        self.assertSequenceEqual(args, ['a', 'b', 'c'])


class TestMongoPipeline(TestCase):
    pass
