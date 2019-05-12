import logging
from unittest import TestCase

from scrapy.settings import Settings

from scrapy_pipelines.settings import unfreeze_settings
from scrapy_pipelines.settings import LOGGER


class TestSettings(TestCase):
    def setUp(self) -> None:
        self.settings = Settings()
        self.settings.freeze()

    def tearDown(self) -> None:
        pass

    def test_unfreeze_settings(self):
        self.assertEqual(self.settings.frozen, True)
        with unfreeze_settings(self.settings) as settings:
            self.assertEqual(self.settings.frozen, False)
        self.assertEqual(self.settings.frozen, True)

        with self.assertRaises(Exception), self.assertLogs(logger=LOGGER, level=logging.ERROR):
            with unfreeze_settings(self.settings) as settings:
                raise Exception
