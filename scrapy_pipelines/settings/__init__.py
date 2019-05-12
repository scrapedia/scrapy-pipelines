from contextlib import contextmanager

from scrapy.settings import Settings


@contextmanager
def unfreeze_settings(settings: Settings):
    """

    :param settings:
    :type settings:
    :return:
    :rtype:
    """
    original_status: bool = settings.frozen
    settings.frozen = False
    try:
        yield settings
    finally:
        settings.frozen = original_status
