DownloadAlbumMP3Zing
================================
## Describe
This application helps you to download all song in a playlist or an album from the page mp3.zing.vn

This application using scrapy framework to parse html and get link to download mp3 file

## Requirement
- Python 2.7 or higher
- Scrapy 1.0.4 or higher

## Instruction
### For Linux user
- Just run the DownloadAlbum.sh

### Other OS user
- python CreateJsonFile.py
- scrapy crawl album -o LinkSongs.json
- scrapy crawl song -o Songs.json
- python DownloadSong.py

## Update
### Version 0.1
- Can only download from an album

### Version 0.2
- Put all album link to link_album.txt then run the code. The application will download all album and split into foldes
