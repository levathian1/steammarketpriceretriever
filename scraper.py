#max request is approx 20/min

from urllib.request import urlopen
from colorama import Fore, Back, Style
import re
import csv
import time
import json


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
    if(price["lowest_price"] > str(float(row[1])*1.3).replace(".", ",") + "€"):
        print(Back.GREEN + 'sell ', row[0])
        time.sleep(5)
    


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
        print(f'Processed {line_count} lines.')


def main():
    getPricesFromCSV('test.csv')
  
if __name__== "__main__":
    main()