import json

import scrapy
from AlbumMP3ZingDownloader.items import SongItem


class SongSpider(scrapy.Spider):
    # Const value
    HOST = "mp3.zing.vn"
    TAB_CONTAIN_XML = 'div[@id="html5player"]/@data-xml'

    name = "song"
    allowed_domains = [HOST]
    # Create a list of song link based on JSON file created by AlbumCrawler
    # Uncomment after crawl album
    with open("ListSong.json") as list_song_file:
        try:
            list_song = json.load(list_song_file)
        except ValueError:
            list_song = []
    start_urls = []
    for i in xrange(0, len(list_song)):
        print list_song[i]['link'][0]
        start_urls.append(str(list_song[i]['link'][0]))

    def parse(self, response):
        for sel in response.xpath('//div[@id="_player"]'):
            item = SongItem()
            item['link'] = sel.xpath(SongSpider.TAB_CONTAIN_XML).extract()
            yield item
