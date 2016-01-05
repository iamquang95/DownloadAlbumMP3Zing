import json
import urllib
import os


with open("Songs.json") as songs_file:
    try:
        songs = json.load(songs_file)
    except ValueError:
        songs = []


print "Finish crawling download links"
print "There are " + str(len(songs)) + " songs in this album"
print "----------------------------------------"

count_downloaded_song = 0


for song in songs:
    folder_path = song['album']
    print folder_path
    if not os.path.exists(folder_path):
        original_umask = os.umask(0)
        os.makedirs(folder_path, 0777)

    mp3_link = song['link'][0]
    title = song['title'][0]
    author = song['author'][0]

    filename = folder_path + "/" + title + " " + author + ".mp3"
    # Download file using urllib (can upgrade using urllib2)
    f = open(filename, "wb")
    print "Downloading " + filename
    f.write(urllib.urlopen(mp3_link).read())
    f.close()
    count_downloaded_song += 1
    print "     Downloaded %s/%s" % (count_downloaded_song, len(songs))
    print "----------------------------------------"
