#auth needed to get non empty array
#https://stackoverflow.com/questions/71012005/price-history-extraction-from-steam-market

#for month price calc
#grab all from one month (use var to track for a particular month)
#compile into file per month
#process files individually and resave to stats file


import requests
import json
import datetime


url = "https://steamcommunity.com/market/pricehistory/?appid=730&market_hash_name=P90%20%7C%20Blind%20Spot%20(Field-Tested)"

headers = {
    "Cookie": "steamLoginSecure=76561198157952830%7C%7CeyAidHlwIjogIkpXVCIsICJhbGciOiAiRWREU0EiIH0.eyAiaXNzIjogInI6MEM5OV8yMTZGOUNENV9DNzE5NCIsICJzdWIiOiAiNzY1NjExOTgxNTc5NTI4MzAiLCAiYXVkIjogWyAid2ViIiBdLCAiZXhwIjogMTY2NjA5NTM4NywgIm5iZiI6IDE2NTczNjc4ODMsICJpYXQiOiAxNjY2MDA3ODgzLCAianRpIjogIjBDOTdfMjE2RjlERjVfMzIxOUYiLCAib2F0IjogMTY2NTU5Njk4MSwgInJ0X2V4cCI6IDE2ODM4MDE0NjcsICJwZXIiOiAwLCAiaXBfc3ViamVjdCI6ICIxOTUuODMuMjExLjEzOCIsICJpcF9jb25maXJtZXIiOiAiMTk1LjgzLjIxMS4xMzgiIH0.bG8ufhZPuylPra-KIhsQCfPDuYHKpmvLPMOh6SLcpxuqK7j9vf5lKrwsfQLlLUMpAa1atGAKl4uywdd2WX_rDw"
}

#response = requests.get(url, headers=headers)
#response=response.json()

def write_file():
    f = open("tmp.txt", "a")
    f.write(json.dumps(response, indent=4))
    f.close()

#retrieves price from array
#print(len(response["prices"]))

#string retrieval to pos
teststr = 'Oct 17 2022 18: +0'
usable_str =  teststr[:11]
print(usable_str.replace(" ", ""))

#date parsing
#Oct 17 2022 18: +0
date = datetime.datetime.strptime(usable_str.replace(" ", ""), "%b%d%Y").date()
print(date)
print(date.year)

#read retrieved values
f = open("tmp.txt", "r")
myfile = f.read()
f.close()
myfile = json.loads(myfile)

tmpstr = myfile["prices"][0][0][:11]
date = datetime.datetime.strptime(tmpstr.replace(" ", ""), "%b%d%Y").date()
print(date.year)

f2 = open("price.txt", "a")
f2.write(json.dumps(myfile["prices"][0]))
f2.close()

year_prices = open("prices.txt", "a")

#write last year prices into file for saving
for i in range(0, len(myfile["prices"])):
    #print(myfile["prices"][i][0])
    tmpstr = myfile["prices"][i][0][:11]
    date = datetime.datetime.strptime(tmpstr.replace(" ", ""), "%b%d%Y").date()
    if(date.year>=2021):
        #print(date.year)
        year_prices.write(json.dumps(myfile["prices"][i])+ "\n")
        
year_prices.close()

prices = []
for line in open('prices.txt', 'r'):
    prices.append(json.loads(line))

print(prices[0][1])

current_month = "01"

#get month name as string
#mydate = datetime.datetime.now()
#print(mydate.strftime("%b"))