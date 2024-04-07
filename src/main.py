import requests
import hashlib
import time
import json

ts = str(time.time())
limit = 600
f = open('actual_key.txt', 'r')

private = f.read()
public = "9aac47d81d48c3c0fb4a6a30c1d48b5b"

hashcode = (ts+private+public).encode('utf-8')
hashcode = hashlib.md5(hashcode).hexdigest()

charname = input('Enter the character name\n')

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
data = response.json()

data = response.json()

jsonResults = data['data']['results']

total_record = data['data']['total'] #total of all comics returned

fullComicList = open("organiazedcomiclist.txt", "w") #outputs the list in the text file

for offset in range(0, total_record, 100):

    url = "https://gateway.marvel.com/v1/public/characters/" + str(characterId) + "/comics?offset=" +str(offset)
    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()
    jsonResults = data['data']['results']

    offset = offset + 100

    for x in jsonResults:
        fullComicList = open("organiazedcomiclist.txt", "a")
        fullComicList.write(x['title'])
        fullComicList.write("\n")
        fullComicList.close()
        print(x['title'])

#order by year
