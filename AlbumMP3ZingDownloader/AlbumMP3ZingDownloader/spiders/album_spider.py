import scrapy
from AlbumMP3ZingDownloader.items import AlbumItem


class AlbumSpider(scrapy.Spider):
    name = "album"
    allowed_domains = ["mp3.zing.vn"]
    start_urls = [
        "http://mp3.zing.vn/album/Really-Love-You-Single-Noo-Phuoc-Thinh/ZWZCWOUO.html",
    ]

    def parse(self, response):
        for sel in response.xpath('//ul/li/div[@class="item-song"]'):
            item = AlbumItem()
            item['link'] = sel.xpath('h3/a/@href').extract()
            yield item
