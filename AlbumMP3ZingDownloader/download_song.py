import json
import urllib
import os


with open("json_files/Songs.json") as songs_file:
    try:
        songs = json.load(songs_file)
    except ValueError:
        print "Error when read json file after crawling"
        songs = []


print "Finish crawling download links"
print "There are " + str(len(songs)) + " songs in this album"
print "----------------------------------------"

download_song_count = 0

for song in songs:
    folder_path = song['album']
    print folder_path
    if not os.path.exists(folder_path):
        original_umask = os.umask(0)
        os.makedirs(folder_path, 0777)

    mp3_link = song['link'][0]
    title = song['title'][0]
    author = song['author'][0]

    # filename = folder_path + "/" + title + " " + author + ".mp3"
    filename = ("%s/%s-%s.mp3") % (folder_path, title, author)
    # Download file using urllib (can upgrade using urllib2)
    # f = open(filename, "wb")
    # print "Downloading " + filename
    # f.write(urllib.urlopen(mp3_link).read())
    # f.close()
    with open(filename, "wb") as f:
        print "Downloading " + filename
        f.write(urllib.urlopen(mp3_link).read())
    download_song_count += 1
    print "     Downloaded %s/%s" % (download_song_count, len(songs))
    print "----------------------------------------"
