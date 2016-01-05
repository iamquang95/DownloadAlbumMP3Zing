DownloadAlbumMP3Zing
================================
## Describe
This application helps you to download all song in a playlist or an album from the page mp3.zing.vn

This application using scrapy framework to parse html and get link to download mp3 file

## Requirement
- Python 2.7 or higher
- Scrapy 1.0.4 or higher

## Instruction
### Installation
- You should install pip

#### Linux
- pip install -r requirements.txt

#### Windows
- pip install lxml-3.4.4-cp27-none-win_amd64.whl
- pip install -r requirements.txt

### Running
- cd AlbumMp3ZingDownloader
- Add all album link you want to download into link_album.txt

#### For Linux user
- Just run the ./DownloadAlbum.sh

#### Other OS user
- python create_json_file.py
- scrapy crawl album -o json_files/LinkSongs.json --nolog
- scrapy crawl song -o json_files/Songs.json --nolog
- python download_song.py


## Update
### Version 0.1
- Can only download from an album

### Version 0.2
- Put all album link to link_album.txt then run the code. The application will download all album and split into foldes
