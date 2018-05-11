import requests
import json

response = requests.get('https://api.github.com/', auth=('jennyafish', ""))

print(response.text)

# get token for developers in settings, bypass entering password
# DO NOT COMMIT TO PUBLIC REPO
token = ""

# creates json object from response.text
obj = json.JSONDecoder()
dict = obj.decode(response.text)

# gets all user's repositories
user_repos = dict["user_repositories_url"].replace("{user}", "jennyafish")

#url for orgo repos
orgo_repos = dict["user_organizations_url"]
print (user_repos)

# gets rid of the filtering
unfiltered_user_repos = user_repos.replace("{?type,page,per_page,sort}", "")
print(orgo_repos)

# we want to get the organizations that we are a part of, so we need authentication
list_of_orgo_repos = requests.get(orgo_repos + "?access_token=" + token)  #for authentication

# convert to a json object
list_of_orgo_repos = obj.decode(list_of_orgo_repos.text)

# create list of tuples for organization names and urls
organizations = []
for o in list_of_orgo_repos:
	organizations.append((o["login"], o["repos_url"]))
	
