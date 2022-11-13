#max request is approx 20/min

from urllib.request import urlopen
from colorama import Fore, Back, Style
import re
import csv
import time
import json
import linecache

import io


    



def getPrices(val):
    f = urlopen(val[2])
    myfile = f.read().decode('utf-8')
    f.close()
    myfile = json.loads(myfile) #sets information as json object
    time.sleep(4)
    return myfile

def readPrices(price, row):
    print("name: ", row[0])
    print("lowest price: ", price["lowest_price"])
    print("median price: ", price["median_price"])
    if(price["lowest_price"] > str(float(row[1])*1.35).replace(".", ",") + "€"):
        print(Back.GREEN + 'sell ', row[0] + Style.RESET_ALL)
        time.sleep(5)

#will allow for singular object query
#prints an empty line afterwards
def getSingularPrice(index, file):
    text = linecache.getline(file, index, module_globals=None)
    print(text)
 
def getFileContent(file):
    with open(file) as content:
        storer = content.read()
    return storer

def getPricesFromCSV(file):
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                price = getPrices(row)
                readPrices(price, row)
                line_count += 1

#add to file, item is an array containing, name, taxless price and link
def addItem(file, item): 
    with open(file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(item)

class gui():
    print("Options\n 1. Get prices from given file \n 2. Add new item\n")
    opt = int(input("Enter option"))

    if(opt == 1):
        getPricesFromCSV("test.csv")
    if(opt == 2):
        name = input("item name")
        price = input('sell price without tax')
        link = input("api link")
        array = {name, price, link}
        addItem("test.csv", array)

def main():
    getPricesFromCSV("test.csv")
    #print("hello")
    #getSingularPrice(1, "test.csv")
    #addItem("test2.csv", array)
  
if __name__== "__main__":
    gui()
    main()
    #app = TableApp()
    #app.run()
    