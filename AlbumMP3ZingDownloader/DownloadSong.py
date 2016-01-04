import json
import urllib

with open("Songs.json") as songs_file:
    try:
        songs = json.load(songs_file)
        print songs
    except ValueError:
        songs = []

for song in songs:
    mp3_link = song['link'][0]
    title = song['title'][0]
    author = song['author'][0]

    filename = title + " " + author + ".mp3"
    # Download file using urllib (can upgrade using urllib2)
    f = open(filename, "wb")
    print "Downloading " + filename
    f.write(urllib.urlopen(mp3_link).read())
    f.close()
    print "     Downloaded"
    print "----------------------------------------"
