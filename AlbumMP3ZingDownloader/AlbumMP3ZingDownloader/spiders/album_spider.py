import scrapy
from AlbumMP3ZingDownloader.items import AlbumItem


class AlbumSpider(scrapy.Spider):
    name = "album"
    allowed_domains = ["mp3.zing.vn"]
    with open("link_album.txt", "r") as f:
        start_urls = f.read().split()

    def parse(self, response):
        album_name = response.xpath('//div[@class="info-content"]/h1/text()')
        album_name = album_name[0].extract()
        for sel in response.xpath('//ul/li/div[@class="item-song"]'):
            item = AlbumItem()
            item['link'] = sel.xpath('h3/a/@href').extract()
            item['album'] = album_name
            yield item
