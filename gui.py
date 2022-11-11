from tksheet import Sheet
import tkinter as tk
import csv

def getFileContent(file):
    with open(file) as content:
        storer = content.read()
    return storer

def dataToArray(file):
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        array = [[]]
        for row in csv_reader:
           # print(row[0])
            array[line_count].append(row[0])
            array[line_count].append(row[1])
            array[line_count].append(row[2])
            line_count+=1
            array.append([])
    return array
 

class demo(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.grid_columnconfigure(0, weight = 1)
        self.grid_rowconfigure(0, weight = 1)
        self.frame = tk.Frame(self)
        self.frame.grid_columnconfigure(0, weight = 1)
        self.frame.grid_rowconfigure(0, weight = 1)
        self.sheet = Sheet(self.frame,
                           data = dataToArray("test.csv"))
        self.sheet.enable_bindings()
        self.frame.grid(row = 0, column = 0, sticky = "nswe")
        self.sheet.grid(row = 0, column = 0, sticky = "nswe")



dataToArray("test.csv")
app = demo()
app.mainloop()