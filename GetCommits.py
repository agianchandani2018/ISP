import requests
import json

response = requests.get('https://api.github.com/', auth=('agianchandani2018', ""))

# creates json object from response.text
obj = json.JSONDecoder()
dict = obj.decode(response.text)

print (dict)

# gets all user's repositories url
user_repos_url = dict["repository_url"].replace("{owner}", "agianchandani2018").replace("{repo}", "PrintNumbersRecursive")

print("-------")
print (user_repos_url)

commito = requests.get(user_repos_url, "")

commito = obj.decode(commito.text)

commitsUrl = commito["commits_url"].replace("{/sha}", "")
print (commitsUrl)

commitList = requests.get(commitsUrl)

objecto = json.JSONDecoder()
dictionary = objecto.decode(commitList.text)
print (dictionary)

name = dictionary[0]["commit"]["author"]["name"]
print (name)

date = dictionary[0]["commit"]["author"]["date"]
print (date)

for k in dictionary:
     print(k["sha"])

print (len(dictionary))

#https://api.github.com/users/agianchandani2018/repos{?type,page,per_page,sort}


# gets rid of the filtering
#unfiltered_user_repos = user_repos.replace("{?type,page,per_page,sort}", "")

#print(unfiltered_user_repos)
