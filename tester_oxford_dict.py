import requests
from pprint import pprint as print
import googletrans
import json
app_id = "668656f1"
app_key = "a9351e6a1c3a3679a335d7fcb6b2d30f"
language = "en-gb"
word_id = "car"
url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word_id.lower()
r = requests.get(url, headers={"app_id": app_id, "app_key": app_key})
res=r.json()
#print(res['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0]['audioFile'])
#print(res['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0])
#print(res['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][1]['definitions'][0])
print(googletrans.LANGUAGES)