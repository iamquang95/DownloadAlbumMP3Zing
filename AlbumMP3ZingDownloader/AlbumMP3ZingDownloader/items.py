# -*- coding: utf-8 -*-

import scrapy


class AlbumItem(scrapy.Item):
    link = scrapy.Field()
    album = scrapy.Field()


class SongItem(AlbumItem):
    title = scrapy.Field()
    author = scrapy.Field()
    link = scrapy.Field()
    album = scrapy.Field()
