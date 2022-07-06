import copy

produit = {
    "nom" : "<empty>",
    "prix" : 0,
    "quantite" : 0
}

product = []
currentProduct = [] 
currentProduct = copy.deepcopy(produit)

currentProduct ["nom"] =str(input("entrer le nom du produit: "))
currentProduct ["prix"] =int(input("entrer le prix: "))
currentProduct ["quantite"] =int(input("entrer la quantiter: "))
product.append(currentProduct)
addp = input("vouler vous ajouter un nouveau produit oui/non: ")

while addp == "oui":
    currentProduct = copy.deepcopy(produit)
    currentProduct ["nom"] =str(input("entrer le nom du produit: "))
    currentProduct ["prix"] =int(input("entrer le prix: "))
    currentProduct ["quantite"] =int(input("entrer la quantiter: "))
    product.append(currentProduct)
    addp = input("vouler vous ajouter un nouveau produit oui/non: ")

"""
name = input("entrer le nom du produit: ")
price = input("entrer le prix: ")
quantite = input("entrer la quantiter: ")

produit["nom"] = name
produit["prix"] = price
produit["quantite"] = quantite
"""
print(product)