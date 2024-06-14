import csv

## PRODUCTS DICTIONARY ##
product_list = []

def productsMenu():
    print(product_list)

# Function to load products from CSV file
def loadProductsFromCSV():
    global product_list
    try:
        with open('products.csv', mode='r') as file:
            reader = csv.DictReader(file)
            product_list = [row for row in reader]
            # Convert price and quantity to correct types
            for product in product_list:
                product['price'] = float(product['price'])
                product['quantity'] = int(product['quantity'])
    except FileNotFoundError:
        print("No existing product file found. Starting with an empty product list.")

# Function to save products to CSV file
def saveProductsToCSV():
    with open('products.csv', mode='w', newline='') as file:
        fieldnames = ['name', 'price', 'quantity']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(product_list)

## -- Products Menu -- ##

## View all products
def viewProducts():  #Defining function
    print(product_list) # Printing function

## Creating New Product
def createProduct(): #Defining function
    print(product_list) #Printing function
    name = input("Enter Product Name:") #Take user input
    price = float(input("Enter Price:")) #Take user input
    quantity = int(input("Enter Quantity:")) #Take user input

    product = {
        "name": name,  ##Flavour of Ice cream
        "price": price,  ##Price per scoop
        "quantity": quantity ##How many scoops
    }
    product_list.append(product)
    saveProductsToCSV()

## Update Prodcuts ## 
def updateProduct():
    print(product_list)
    name = input("Enter product name:")  
    for product in product_list:
        if product['name'] == name:  ## Enter new product name
            price = float(input("Enter New Price:"))  ## New price
            quantity = int(input("Enter quantity:"))  ## Scoops of ice cream
            product['price'] = price
            product['quantity'] = quantity
            print("Product updated Successfully")
            print("Product not found!")
            saveProductsToCSV()
            return
        print("Products not found!")

## Delete Existing Product ##
def deleteProduct():
    print(product_list)
    name = input ("Enter name of product to remove:")  ## Selecting flavour to remove
    for product in product_list:
        if product['name'] == name:
            product_list.remove(product)
            print("Product successfully removed")
            saveProductsToCSV()
            print("Product not found")
            return
        print("Products not found")

