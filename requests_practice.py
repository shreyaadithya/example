import requests

response = requests.get("https://api.github.com")
print(response.status_code)
#print(response.text)
data = response.json()
print(type(data))   # dict or list

#################################################
import requests

res = requests.get("https://api.github.com/users/octocat")
data = res.json()

print(data["login"])
print(data["public_repos"])

###########################################################
#sending query parameters like queries we see in the urls
params = {
    "q": "python",
    "sort": "stars"
}

res = requests.get(
    "https://api.github.com/search/repositories",
    params=params
)

print(res.url)

############################################################
#post request like sending data to server 
payload = {
    "name": "devops",
    "active": True
}

res = requests.post(
    "https://example.com/api",
    json=payload
)

print(res.status_code)

################################################################
#Headers (VERY IMPORTANT) == Headers carry authentication and metadata.
"""
headers = {
    "Authorization": "Bearer TOKEN",
    "Content-Type": "application/json"
}

res = requests.get(url, headers=headers)

requests.get(url, auth=("user", "password")) #basic authentication

headers = {
    "Authorization": "Bearer TOKEN"
}
"""
try:
    requests.get("https://example.com/api", timeout=3)
except requests.exceptions.Timeout:
    print("Request timed out")

#######################################################
#Error Handling (INTERVIEW GOLD ⭐)
try:
    res = requests.get("https://sample.com")
    res.raise_for_status()
except requests.exceptions.HTTPError as e:
    print("HTTP error", e)
#####################################################
#file downloading using requests
res = requests.get("https://india.info/")

with open("file.zip", "wb") as f:
    f.write(res.content)
#############################################
#file upload to server 
files = {
    "file": open("a.txt", "r")
}

requests.post("https://india.info/", files=files)
   
################################################
"""#server health check
res = requests.get("https://service/health")

if res.status_code == 200:
    print("Service is UP")
else:
    print("Service is DOWN")

#this is to trigger jenkins job
requests.post(
    "http://jenkins/job/build",
    auth=("user", "token")
)
"""








