# TXT File
my_file = open("INTERMEDIO/fichero.txt", "w+")
print(my_file.read())  
print(my_file.read(5))  
print(my_file.readline())  
print(my_file.readlines())  

my_file.write("\nEs mejor Angular")
my_file.close()

# import os
# os.remove("INTERMEDIO/fichero.txt")

# JSON 

import json

json_file = open("INTERMEDIO/json_file.json", "w+")

json_test = {
    "Nombre": "Juan",
    "Apellido": "Diego",
    "Edad": 29,
    "lenguajes": ["JavaScript", "Python", 2]
}

json.dump(json_test, json_file, indent=2)

json_file.close()

#with open("INTERMEDIO/json_file.json") as a:
    #for line in a.readlines():
        #print(line)

json_dict = json.load(open("INTERMEDIO/json_file.json"))
print(json_dict)
print(type(json_dict))

# CSV
import csv

csv_file = open("INTERMEDIO/csv_file.csv", "w+")

writer = csv.writer(csv_file)

writer.writerow(["Nombre", "Apellido"])
writer.writerow(["Juan Diego", "Osorio"])

csv_file.close()

# XLSX
    # import xlrd # Instalar 
# XML
import xml