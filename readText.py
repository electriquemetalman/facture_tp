"""
import csv

with open('text.csv') as csvFile:
    new_list = []
    csvReader = csv.reader(csvFile, delimiter=' ')
    for row in csvReader:
        #print(row)
        new_list.append(row)
print(new_list)
"""
import copy

motEtNombre = {
    "mot" : "<empty>",
    "nombre" : 0
}

tousLesMots = []
tableMot = []
file = open("text.txt" , 'r')
listUnique = []
content = file.read()
listMots = content.split()
file.close()
for mot in listMots:
    if mot not in listUnique:
        listUnique.append(mot)
        tableMot = copy.deepcopy(motEtNombre)
        tableMot["mot"] = mot
        tableMot["nombre"] = listMots.count(mot)
        tousLesMots.append(tableMot)
print((tousLesMots))
     
        #print("le mot: " + mot , listMots.count(mot))
