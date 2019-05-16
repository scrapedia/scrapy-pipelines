"""
This module contains the default values for all settings used by this item
pipeline.

For more information about these settings you can read the settings
documentation in docs/topics/settings.rst

Scrapy developers, if you add a setting here remember to:

* add it in alphabetical order
* group similar settings without leaving blank lines
* add its documentation to the available settings documentation
  (docs/topics/settings.rst)

"""
PIPELINE_MONGO_URI = "mongodb://127.0.0.1:27017"
# PIPELINE_MONGO_POOL_SIZE = 1
# PIPELINE_MONGO_SSL_CONTEXT_FACTORY = None
# PIPELINE_MONGO_PING_INTERVAL = 10
# PIPELINE_MONGO_PING_TIMEOUT = 10

PIPELINE_MONGO_DATABASE = "scrapy_project_database"
# PIPELINE_MONGO_WRITE_CONCERN = None
# PIPELINE_MONGO_CODEC_OPTION = None

PIPELINE_MONGO_USERNAME = "USERNAME"
PIPELINE_MONGO_PASSWORD = "PASSWORD"
# PIPELINE_MONGO_MECHANISM = "DEFAULT"

PIPELINE_MONGO_COLLECTION = "scrapy_project_collection"

# PIPELINE_MONGO_OPTIONS_ = "OPTIONS_"

# PIPELINE_MONGO_INDEXES = "INDEXES"

# PIPELINE_MONGO_PROCESS_ITEM = "PROCESS_ITEM"

# from txmongo.filter import ASCENDING, DESCENDING
#
# PIPELINE_MONGO_INDEXES = [
#     ("key_asc", ASCENDING, {"name": "index_key_asc"}),
#     ("key_des", DESCENDING, {"name": "index_key_des"}),
#     ("key_unique", DESCENDING, {"name": "index_key_unique", "unique": True}),
# ]
