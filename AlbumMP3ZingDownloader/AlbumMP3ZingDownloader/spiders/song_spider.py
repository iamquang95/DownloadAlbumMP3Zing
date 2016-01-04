import json

import scrapy
from AlbumMP3ZingDownloader.items import SongItem


class SongSpider(scrapy.Spider):
    name = "song"
    allowed_domains = ["mp3.zing.vn"]
    # Create a list of song link based on JSON file created by AlbumCrawler
    # Uncomment after crawl album
    with open("ListSong.json") as list_song_file:
        list_song = json.load(list_song_file)
    start_urls = []
    for i in xrange(0, len(list_song)):
        print list_song[i]['link'][0]
        start_urls.append(str(list_song[i]['link'][0]))

    def parse(self, response):
        for sel in response.xpath('//div[@id="_player"]'):
            item = SongItem()
            item['link'] = sel.xpath('div[@id="html5player"]/@data-xml').extract()
            yield item
