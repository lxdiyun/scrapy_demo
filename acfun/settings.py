# -*- coding: utf-8 -*-

# Scrapy settings for acfun project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'acfun'

SPIDER_MODULES = ['acfun.spiders']
NEWSPIDER_MODULE = 'acfun.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'acfun (+http://www.yourdomain.com)'

DEPTH_LIMIT = 2
#LOG_FILE = "acfun.log"
LOG_LEVEL = "INFO"

# pip line
ITEM_PIPELINES = {
    #'scrapycouchdb.CouchDBPipeline': 900,
    'scrapyelasticsearch.ElasticSearchPipeline': 901
}


# CouchDB
COUCHDB_SERVER = 'http://172.17.8.2:5984/'
COUCHDB_DB = 'acfun'
COUCHDB_UNIQ_KEY = 'id'
COUCHDB_IGNORE_FIELDS = ['visit_id', 'visit_status']

# ElasticSearch
ELASTICSEARCH_SERVER = '172.17.8.2' # If not 'localhost' prepend 'http://'
ELASTICSEARCH_PORT = 9200 # If port 80 leave blank
ELASTICSEARCH_USERNAME = ''
ELASTICSEARCH_PASSWORD = ''
ELASTICSEARCH_INDEX = 'acfun'
ELASTICSEARCH_TYPE = 'wenzhang'
ELASTICSEARCH_UNIQ_KEY = 'id'
