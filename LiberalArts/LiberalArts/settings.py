# -*- coding: utf-8 -*-

# Scrapy settings for LiberalArts project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'LiberalArts'

SPIDER_MODULES = ['LiberalArts.spiders']
NEWSPIDER_MODULE = 'LiberalArts.spiders'

ITEM_PIPELINES = {'scrapy.contrib.pipeline.images.ImagesPipeline':1}
IMAGES_STORE = '/home/saira/Desktop/LiberalArts'
IMAGES_EXPIRES = 90

DOWNLOAD_DELAY = 2
CONCURRENT_REQUESTS = 2
CONCURRENT_REQUESTS_PER_DOMAIN = 2

USER_AGENT = 'Googlebot/2.1 (+http://www.googlebot.com/bot.html)'
COOKIES_ENABLED = False

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'LiberalArts (+http://www.yourdomain.com)'
