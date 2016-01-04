import json
import urllib


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
    mp3_link = song['link'][0]
    title = song['title'][0]
    author = song['author'][0]

    filename = title + " " + author + ".mp3"
    # Download file using urllib (can upgrade using urllib2)
    f = open(filename, "wb")
    print "Downloading " + filename
    f.write(urllib.urlopen(mp3_link).read())
    f.close()
    count_downloaded_song += 1
    print "     Downloaded %s/%s" % (count_downloaded_song, len(songs))
    print "----------------------------------------"
