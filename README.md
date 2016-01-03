DownloadAlbumMP3Zing
================================
## Describe
This application helps you to download all song in a playlist or an album from the page mp3.zing.vn

This application using scrapy framework to parse html and get link to download mp3 file

## Requirement
- Python 2.7 or higher
- Scrapy 1.0.4 or higher

## Instruction
- scrapy crawl album -o ListSong.json
- scrapy crawl song -o DownloadLink.json
