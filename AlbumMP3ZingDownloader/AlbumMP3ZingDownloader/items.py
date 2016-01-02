# -*- coding: utf-8 -*-

import scrapy


class DmozItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()


class AlbumItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    author = scrapy.Field()


# class SongItem(scrapy.Item):
#     link = scrapy.Field()
