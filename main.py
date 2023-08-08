import requests
import hashlib
import time
import json

ts = str(time.time())
limit = 600

private = "19b1f441208b602d3d4d994c0fda917f83743fd3"
public = "9aac47d81d48c3c0fb4a6a30c1d48b5b"

hashcode = (ts+private+public).encode('utf-8')
hashcode = hashlib.md5(hashcode).hexdigest()

#choice = input('1:Characters\n2:Comic\n3:Creator\n4:Event\n5:Series\n6:Stories\n')

charname = "Rogue" #input('Enter the character\n')

url = "https://gateway.marvel.com/v1/public/characters"

querystring = {"name": charname, "apikey": public, "hash": hashcode, "ts": ts}

headers = {
    'Marvel-Key': "9aac47d81d48c3c0fb4a6a30c1d48b5b",
    'Marvel-Host': "gateway.marvel.com"
}

response = requests.get(url, headers=headers, params=querystring)

data = json.loads(json.dumps(response.json()))

characterId = data['data']['results'][0]['id'] #id used to get the full list of comics

url = url + characterId

jsonResults = data['data']['results'][0]['comics']

for x in jsonResults['items']:
     print(x['name'])
"""
jsonResults = data['data']['results'][0]['events']

for x in jsonResults['items']:
     print(x['name'])

jsonResults = data['data']['results'][0]['series']

for x in jsonResults['items']:
     print(x['name'])

jsonResults = data['data']['results'][0]['stories']

for x in jsonResults['items']:
     print(x['name'])
"""
#remember to update offset and limit to return the following data
#order by year