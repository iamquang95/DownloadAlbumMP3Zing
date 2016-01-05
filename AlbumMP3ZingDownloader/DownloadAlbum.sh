python create_json_file.py
scrapy crawl album -o LinkSongs.json --nolog
scrapy crawl song -o Songs.json --nolog
python download_song.py
