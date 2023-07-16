import requests
import hashlib
import time

ts = str(time.time())

private = "19b1f441208b602d3d4d994c0fda917f83743fd3"
public = "9aac47d81d48c3c0fb4a6a30c1d48b5b"

hashcode = ts+private+public.encode('utf-8')
hashcode = hashlib.md5(hashcode).hexdigest()

charname = "Wolverine" #input('Enter the Marvel character:\n')

url = "https://gateway.marvel.com/v1/public/characters"

querystring = {"apikey":public,"hash":hashcode,"ts":ts}

headers = {
    'Marvel-Key': "9aac47d81d48c3c0fb4a6a30c1d48b5b",
    'Marvel-Host': "gateway.marvel.com"
}

response = requests.get(url, headers=headers, params=querystring)

#print(response.json())