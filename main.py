import requests
import hashlib
import time
import json

ts = str(time.time())

private = "19b1f441208b602d3d4d994c0fda917f83743fd3"
public = "9aac47d81d48c3c0fb4a6a30c1d48b5b"

hashcode = (ts+private+public).encode('utf-8')
hashcode = hashlib.md5(hashcode).hexdigest()

choice = input('1:Characters\n2:Comic\n3:Creator\n4:Event\n5:Series\n6:Stories\n')

match choice:
    case '1':
        choice = "characters"
    case '2':
        choice = "comics"
    case '3':
        choice = "creators"
    case '4':
        choice = "events"
    case '5':
        choice = "series"
    case '6':
        choice = "stories"


charname = input('Enter the '+ choice + '\n')

url = "https://gateway.marvel.com/v1/public/"+choice

querystring = {"name":charname,"apikey":public,"hash":hashcode,"ts":ts}

headers = {
    'Marvel-Key': "9aac47d81d48c3c0fb4a6a30c1d48b5b",
    'Marvel-Host': "gateway.marvel.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(json.dumps(response.json()))