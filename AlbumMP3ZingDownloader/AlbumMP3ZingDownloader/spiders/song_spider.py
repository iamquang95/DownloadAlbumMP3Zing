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
    with open("LinkSongs.json") as list_song_file:
        try:
            link_songs = json.load(list_song_file)
        except ValueError:
            link_songs = []
    start_urls = []
    for i in xrange(0, len(link_songs)):
        start_urls.append(str(link_songs[i]['link'][0]))

    i_url = 0

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
        item['album'] = SongSpider.link_songs[SongSpider.i_url]['album']
        SongSpider.i_url += 1
        print "Number of link songs crawled: " + str(SongSpider.i_url)
        yield item
