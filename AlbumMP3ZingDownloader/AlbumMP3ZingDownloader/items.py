# -*- coding: utf-8 -*-

import scrapy


class DmozItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()


class AlbumItem(scrapy.Item):
    link = scrapy.Field()


class SongItem(AlbumItem):
    title = scrapy.Field()
    author = scrapy.Field()
    link = scrapy.Field()
