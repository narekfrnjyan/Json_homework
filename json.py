import urllib
import json
address = "https://swapi.dev/api/people/1/"
r = urllib.request.urlopen(address)
data = json.loads(r.read())
with open("test_json.json","w") as file:
    json.dump(data,file)
