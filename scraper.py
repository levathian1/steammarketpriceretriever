from urllib.request import urlopen
import re
import json
import time


_9z_antwerp = {
    "name" : "9z Antwerp",
    "link" : "https://steamcommunity.com/market/priceoverview/?appid=730&currency=3&market_hash_name=Sticker%20|%209z%20Team%20|%20Antwerp%202022",
    "sell_price" : str(0.06*1.3).replace(".", ",") + "€"
}

navi_antwerp = {
    "name" : "navi Antwerp",
    "link" : "https://steamcommunity.com/market/priceoverview/?appid=730&currency=3&market_hash_name=Sticker%20|%20Natus%20Vincere%20|%20Antwerp%202022",
    "sell_price" : str(0.06*1.3).replace(".", ",") + "€"
}

eternal_fire_antwerp = {
    "name" : "Eternal Fire Antwerp",
    "link" : "https://steamcommunity.com/market/priceoverview/?appid=730&currency=3&market_hash_name=Sticker%20|%20Eternal%20Fire%20|%20Antwerp%202022",
    "sell_price" : str(0.06*1.3).replace(".", ",") + "€"
}

outsiders_antwerp = {
    "name" : "Outsiders Antwerp",
    "link" : "https://steamcommunity.com/market/priceoverview/?appid=730&currency=3&market_hash_name=Sticker%20|%20Outsiders%20|%20Antwerp%202022",
    "sell_price" : str(0.06*1.3).replace(".", ",") + "€"
}

g2_antwerp = {
    "name" : "G2 Antwerp",
    "link" : "https://steamcommunity.com/market/priceoverview/?appid=730&currency=3&market_hash_name=Sticker%20|%20G2%20Esports%20|%20Antwerp%202022",
    "sell_price" : str(0.06*1.3).replace(".", ",") + "€"
}

spirit_antwerp = {
    "name" : "Team Spirit Antwerp",
    "link" : "https://steamcommunity.com/market/priceoverview/?appid=730&currency=3&market_hash_name=Sticker%20|%20Team%20Spirit%20|%20Antwerp%202022",
    "sell_price" : str(0.06*1.3).replace(".", ",") + "€"
}

ence_antwerp = {
    "name" : "ENCE Antwerp",
    "link" : "https://steamcommunity.com/market/priceoverview/?appid=730&currency=3&market_hash_name=Sticker%20|%20ENCE%20|%20Antwerp%202022",
    "sell_price" : str(0.06*1.3).replace(".", ",") + "€"
}

mibr_antwerp = {
    "name" : "MIBR Antwerp",
    "link" : "https://steamcommunity.com/market/priceoverview/?appid=730&currency=3&market_hash_name=Sticker%20|%20MIBR%20|%20Antwerp%202022",
    "sell_price" : str(0.06*1.3).replace(".", ",") + "€"
}

ihc_antwerp = {
    "name" : "IHC Antwerp",
    "link" : "https://steamcommunity.com/market/priceoverview/?appid=730&currency=3&market_hash_name=Sticker%20|%20IHC%20Esports%20|%20Antwerp%202022",
    "sell_price" : str(0.06*1.3).replace(".", ",") + "€"
}

heroic_antwerp = {
    "name" : "Heroic Antwerp",
    "link" : "https://steamcommunity.com/market/priceoverview/?appid=730&currency=3&market_hash_name=Sticker%20|%20Heroic%20|%20Antwerp%202022",
    "sell_price" : str(0.06*1.3).replace(".", ",") + "€"
}

cpflames_antwerp = {
    "name" : "Copenhagen Flames Antwerp",
    "link" : "https://steamcommunity.com/market/priceoverview/?appid=730&currency=3&market_hash_name=Sticker%20|%20Copenhagen%20Flames%20|%20Antwerp%202022",
    "sell_price" : str(0.06*1.3).replace(".", ",") + "€"
}

big_antwerp = {
    "name" : "BIG Antwerp",
    "link" : "https://steamcommunity.com/market/priceoverview/?appid=730&currency=3&market_hash_name=Sticker%20|%20BIG%20|%20Antwerp%202022",
    "sell_price" : str(0.06*1.3).replace(".", ",") + "€"
}

furia_antwerp = {
    "name" : "Furia Antwerp",
    "link" : "https://steamcommunity.com/market/priceoverview/?appid=730&currency=3&market_hash_name=Sticker%20|%20FURIA%20|%20Antwerp%202022",
    "sell_price" : str(0.06*1.3).replace(".", ",") + "€"
}

nip_antwerp = {
    "name" : "NIP Antwerp",
    "link" : "https://steamcommunity.com/market/priceoverview/?appid=730&currency=3&market_hash_name=Sticker%20|%20Ninjas%20in%20Pyjamas%20|%20Antwerp%202022",
    "sell_price" : str(0.06*1.3).replace(".", ",") + "€"
}

liquid_antwerp = {
    "name" : "Team Liquid Antwerp",
    "link" : "https://steamcommunity.com/market/priceoverview/?appid=730&currency=3&market_hash_name=Sticker%20|%20Team%20Liquid%20|%20Antwerp%202022",
    "sell_price" : str(0.06*1.3).replace(".", ",") + "€"
}

renegades_antwerp = {
    "name" : "Renegades Antwerp",
    "link" : "https://steamcommunity.com/market/priceoverview/?appid=730&currency=3&market_hash_name=Sticker%20|%20Renegades%20|%20Antwerp%202022",
    "sell_price" : str(0.06*1.3).replace(".", ",") + "€"
}

forze_antwerp = {
    "name" : "Forze Antwerp",
    "link" : "https://steamcommunity.com/market/priceoverview/?appid=730&currency=3&market_hash_name=Sticker%20|%20forZe%20eSports%20|%20Antwerp%202022",
    "sell_price" : str(0.06*1.3).replace(".", ",") + "€"
}

vitality_antwerp = {
    "name" : "Vitality Antwerp",
    "link" : "https://steamcommunity.com/market/priceoverview/?appid=730&currency=3&market_hash_name=Sticker%20|%20Vitality%20|%20Antwerp%202022",
    "sell_price" : str(0.06*1.3).replace(".", ",") + "€"
}

json_array = [_9z_antwerp, navi_antwerp, eternal_fire_antwerp, outsiders_antwerp, g2_antwerp, spirit_antwerp, ence_antwerp, mibr_antwerp, ihc_antwerp, heroic_antwerp,
cpflames_antwerp, big_antwerp, furia_antwerp, nip_antwerp, liquid_antwerp, renegades_antwerp, forze_antwerp, vitality_antwerp
]

def getPrices(val):
    f = urlopen(val["link"])
    myfile = f.read().decode('utf-8')
    f.close()
    myfile = json.loads(myfile)
    time.sleep(10)
    return myfile

def readPrices(price, json):
    print("name: ", json["name"])
    print("lowest price: ", price["lowest_price"])
    print("median price: ", price["median_price"])
    if(price["lowest_price"] > json["sell_price"]):
        print(json["sell_price"])
        print ("sell ", json["name"])
        time.sleep(5)

def getPricesFromArray(array):
    for val in array:
        price = getPrices(val)
        readPrices(price, val)

getPricesFromArray(json_array)
#print(_9z_antwerp["sell_price"])
#print("0,01€"<_9z_antwerp["sell_price"])