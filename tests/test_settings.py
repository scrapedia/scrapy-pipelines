"""
test the functions in settings
"""
from unittest import TestCase

from scrapy.settings import Settings

from scrapy_pipelines.settings import unfreeze_settings


class TestSettings(TestCase):
    """
    Test the functions in default settings
    """

    def setUp(self) -> None:
        self.settings = Settings()
        self.settings.freeze()

    def test_unfreeze_settings_succeed(self):
        """

        :return:
        """
        self.assertEqual(self.settings.frozen, True)
        with unfreeze_settings(self.settings):
            self.assertEqual(self.settings.frozen, False)
        self.assertEqual(self.settings.frozen, True)

    def test_unfreeze_settings_failed(self):
        """

        :return:
        """
        with self.assertRaises(Exception):
            with unfreeze_settings(self.settings):
                raise Exception
