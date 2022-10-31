#max request is approx 20/min

from urllib.request import urlopen
from colorama import Fore, Back, Style
import re
import csv
import time
import json
import linecache
from textual.app import App, ComposeResult
from textual.widgets import DataTable

import io

from textual.app import App, ComposeResult
from textual.widgets import DataTable

CSV = """lane,swimmer,country,time
4,Joseph Schooling,Singapore,50.39
2,Michael Phelps,United States,51.14
5,Chad le Clos,South Africa,51.14
6,László Cseh,Hungary,51.14
3,Li Zhuhao,China,51.26
8,Mehdy Metella,France,51.58
7,Tom Shields,United States,51.73
1,Aleksandr Sadovnikov,Russia,51.84"""


class TableApp(App):
    def compose(self) -> ComposeResult:
        yield DataTable()

    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        rows = csv.reader(io.StringIO(getFileContent('test.csv')))
        table.add_columns(*next(rows))
        table.add_rows(rows)


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

def main():
    #getPricesFromCSV("test.csv")
    print("hello")
    #getSingularPrice(1, "test.csv")
    #addItem("test2.csv", array)
  
if __name__== "__main__":
    main()
    app = TableApp()
    app.run()
    