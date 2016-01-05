python create_json_file.py
scrapy crawl album -o json_files/LinkSongs.json --nolog
scrapy crawl song -o json_files/Songs.json --nolog
python download_song.py
