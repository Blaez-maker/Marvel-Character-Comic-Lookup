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

charname = "Rogue" #input('Enter the character\n')

url = "https://gateway.marvel.com/v1/public/characters"
url = url + "?name=" + charname

querystring = {"limit": 100, "apikey": public, "hash": hashcode, "ts": ts}

headers = {
    'Marvel-Key': "9aac47d81d48c3c0fb4a6a30c1d48b5b",
    'Marvel-Host': "gateway.marvel.com"
}

response = requests.get(url, headers=headers, params=querystring)

data = json.loads(json.dumps(response.json()))

characterId = data['data']['results'][0]['id'] #id of character used to get the full list of comics

url = "https://gateway.marvel.com/v1/public/characters/" + str(characterId) + "/comics"

response = requests.get(url, headers=headers, params=querystring)
data = json.loads(json.dumps(response.json()))

#print(url)

jsonResults = data['data']['results']

#print(jsonResults)
for x in jsonResults:
     print(x['title'])





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