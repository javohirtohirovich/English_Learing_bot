import requests


app_id = "668656f1"
app_key = "a9351e6a1c3a3679a335d7fcb6b2d30f"
language="en-gb"

def get_defination(word_id):
    url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word_id.lower()
    r = requests.get(url, headers={"app_id": app_id, "app_key": app_key})
    res = r.json()
    if  'error' in res.keys():
        return False

    output={}
    senses=res['results'][0]['lexicalEntries'][0]['entries'][0]['senses']
    defenations=[]
    for sense in senses:
        defenations.append(f"👉 {sense['definitions'][0]}")
    output['definitions']='\n'.join(defenations)
    if res['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0].get('audioFile'):
        output['audioFile']=res['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0]['audioFile']
    return output
if __name__=='__main__':
    from pprint import pprint as print

    print(get_defination("Uzbekistan"))
