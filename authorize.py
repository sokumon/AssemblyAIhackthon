import requests

client_id = "T63_cl9HIPO0EUT5upBjyQ"
secret_key = "z0t1oiHadyAR7rmFWc2SnUkqVXZcZw"

auth = requests.auth.HTTPBasicAuth(client_id,secret_key)

data = {
    "grant_type" : "client_credentials"
}

headers = {
    "User-Agent":"my-api/0.0.1"
}
res = requests.post("https://www.reddit.com/api/v1/access_token",auth=auth,headers=headers,data=data)




def fetch_token():
    auth_token = res.json()['access_token']
    headers["Authorization"] = f"bearer {auth_token}"
    return headers
