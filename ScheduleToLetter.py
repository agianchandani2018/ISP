#python program that takes in a schedule and tells you what letter day it is
import json
import requests

url = "http://compsci.pingry.k12.nj.us:3000/v1/letter?api_key=kVO7gq7ppDezm43J67WiiGsOU1OhW3PNk9lhCUSk"

response = requests.request("GET", url)

#print(response.text)
#json parse

count = 0
for day in response.text:
    count += 1
print (count)

obj = json.JSONDecoder()
cal = obj.decode(response.text)

match = [4, 5, 6, 7]
for day in cal:
    if(day['schedule'] == match):
        print(day['letter'])

#date = "20180508"
date = input("What date would you like the schedule for? YYYYMMDD")
for day in cal:
    if(date in day['dates']):
        print(day['letter'])
        print(day['schedule'])
