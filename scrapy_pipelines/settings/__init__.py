"""
The utilities used in settings module
"""
import logging
from contextlib import contextmanager
from typing import Generator

from scrapy.settings import Settings

LOGGER = logging.getLogger(__name__)


@contextmanager
def unfreeze_settings(settings: Settings) -> Generator[Settings, None, None]:
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
    except Exception as err:
        LOGGER.error(err, exc_info=True)
        raise err
    finally:
        settings.frozen = original_status
