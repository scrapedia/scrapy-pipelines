"""
The utilities used in settings module
"""
from contextlib import contextmanager
from typing import Generator

from scrapy.settings import Settings


@contextmanager
def unfreeze_settings(settings: Settings) -> Generator[Settings, None, None]:
    """

    :param settings:
    :type settings: Settings
    :return:
    :rtype: Generator[Settings, None, None]
    """
    original_status, settings.frozen = settings.frozen, False
    try:
        yield settings
    finally:
        settings.frozen = original_status
