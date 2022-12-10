import requests
from requests.models import PreparedRequest
import json 


from authorize import *

auth_headers = fetch_token()

oauth_link = "https://oauth.reddit.com/r/apple/search"

params = {'q':'Tim Cook'}
req = PreparedRequest()
req.prepare_url(oauth_link, params)
print(req.url)

res = requests.get(req.url,headers=auth_headers)
f = open("test.txt","w")
res_write = json.dumps(res.json())
f.write(res_write)
f.close()
