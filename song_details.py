#import move_file
import urllib2
import json
#track_id = move_file.get_trackId()

track_id = "693488530"

url = "https://itunes.apple.com/lookup?id=" + track_id
print (url)
res = urllib2.urlopen(url)
res = json.dumps(res)

print(res)