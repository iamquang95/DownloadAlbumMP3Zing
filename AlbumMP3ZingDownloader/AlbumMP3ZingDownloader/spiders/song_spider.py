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
            for song_uml in sel.xpath(SongSpider.TAB_CONTAIN_XML):
                url = song_uml.extract()
                yield scrapy.Request(url, callback=self.parse_dir_song)

    def parse_dir_song(self, response):
        item = SongItem()
        item['title'] = response.xpath("//title/text()").extract()
        item['author'] = response.xpath("//performer/text()").extract()
        item['link'] = response.xpath("//source/text()").extract()
        yield item
