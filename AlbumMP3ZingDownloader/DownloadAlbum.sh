python CreateJsonFile.py
scrapy crawl album -o LinkSongs.json --nolog
scrapy crawl song -o Songs.json --nolog
python DownloadSong.py
