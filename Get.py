import requests
import json

f = open("pw.txt", "r+")
pw = f.read()

response = requests.get('https://api.github.com/', auth=('agianchandani2018', ""))

token = "b8a58e94ac70cb4f640d1b4d14901c55d4198b7e"


#print(response.text)

obj = json.JSONDecoder()
dict = obj.decode(response.text)

# print(dict)
# print("_________")
# print(dict["user_repositories_url"])

newt = dict["user_repositories_url"].replace("{user}", "agianchandani2018")
newton = dict["user_organizations_url"]
# print (newt)
newto = newt.replace("{?type,page,per_page,sort}", "")
#print(newton)

responso = requests.get(newton + "?access_token=" + token)  #for authentication
#print(responso.text)

obj = json.JSONDecoder()
arrrgh = obj.decode(responso.text)
print (arrrgh)

a = []
b = []
for object in arrrgh:
    a.append(object["login"]) #printing organization names
    b.append(object["repos_url"])

print(a)
print(b)


responsor = requests.get(b[1])
print("------------------------------")
print (responsor.text)


objecto = json.JSONDecoder()
ar = objecto.decode(responsor.text)

arr = []
for o in ar:
    arr.append(o["name"])

print(arr)

# want to get collaborators of repository or get all the repositories I am a collaborator to
# "https://api.github.com/repos/jennyafish/ChatBot/collaborators{/collaborator}
