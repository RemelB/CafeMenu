import csv ## Importing all CSV Files 
 

# Load data from a CSV file into a list of dictionaries
def load_csv_file(path, header):
    data = []
    try:
        with open(path, 'r', newline="") as file:
            reader = csv.DictReader(file, fieldnames=header)
            next(reader)  # Skip header row
            data = [dict(row) for row in reader]
    except Exception as e:
        print(e)
    return data
 
# Save data from a list of dictionaries to a CSV file
def save_data_to_csv(path, data, header):
    try:
        with open(path, 'w', newline="") as file:  # Use 'w' to overwrite the file
            writer = csv.DictWriter(file, fieldnames=header)
            writer.writeheader()
            for row in data:
                writer.writerow(row)
    except Exception as e:
        print(e)
 
# Headers for CSV files
couriers_header = ['name', 'phone']
product_header = ['Product name', 'Price', 'Quantity']
orders_header = ['name', 'address', 'nunber', 'status']

# Load couriers and products from CSV files
couriers_list = load_csv_file('couriers.csv', couriers_header)
my_product_list = load_csv_file('products.csv', product_header)
orders_list = load_csv_file('orders.csv', orders_header)
 
## Importing Files##  
from products import *
from orders import *
from couriers import *

## PRODUCTS DICTIONARY ##
product_list = {
        "name": "Chocolate",
        "price": 2,
        "quantity": 1
    }, {
        "name": "Strawberry",
        "price": 2,
        "quantity": 1
    }, {
        "name": "Mint",
        "price": 2,
        "quantity": 1
    }

## ORDERS DICTIONARY ##
orders_list = {
        "customer name": "customer_name",
        "customer address": "customer_address",
        "customer phone": "customer_phone",
        "status": "order_status"
    }

## COURIERS DICTIONARY ##
couriers_list = {
    "name": "Fedex",
    "phone": "123445670"
}, {
    "name": "UPS",
    "phone": "123445678"
}, {
    "name": "DPD",
    "phone": "123445671"
}, 


## Nested empty lists ##
orders = [] #Orders list
products = [] #Products list
couriers = [] #Couriers list



## MainMenu ##
def mainMenu():
    while True:
        print("\n-- Welcome to the IceCream Factory --")
        print("1. Orders Menu")
        print("2. Products Menu")
        print("3. Couriers")
        print("4. Exit")
        user_choice = input ("Enter please select between the two Menus:\n")
        
        if user_choice == '1':
            ordersMenu(orders)
        elif user_choice == '2':
            productMenu()
        elif user_choice == '3':
            couriermenu()
        elif user_choice == '4':
            print("Exiting App")
            break
        else:
            print("Invalid Choice. Please try again.")


## Orders Menu Choice ##
def ordersMenu():
    while True:
        print("Orders Menu")
        print("0. Customer Menu")
        print("1. Create Orders")
        print("2. Update Orders")
        print("3. Delete Orders")
        print("4. Return to Main Menu")
        user_choice = input("Please choose (0-4):")
        if user_choice == '0':
            customerMenu()
            print("Your order...\n")
        elif user_choice ==  '1':
            createOrders(orders)
            print("Please create new order...")
        elif user_choice == '2':
            updateOrders()
            print("Please update order... if needed")
        elif user_choice == '3':
            deleteOrders()
            print("Delete order to restart...")
        elif user_choice == '4':
            print("Returning to Main Menu")
            break
        else:
            print("Invalid choice. Please Select a valid option")
            user_choice = input("Please choose (1-4):")


## Couriers Menu
def couriermenu(couriers):
    # couriers = load_couriers()  # Load deliveries from file at the start
    while True:
        print("Courier Management System")
        print("1. Add a new delivery")
        print("2. View all deliveries")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            add_couriers(couriers)
        elif choice == '2':
            view_couriers(couriers)
        elif choice == '3':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.\n")



## Products Menu ##
def productMenu():
    print("Welcome to the IceCream Factory")
    print("1. View all IceCream Flavours")
    print("2. Create a Product to add to your Order")
    print("3. Update current Products")
    print("4. Delete Product from list")
    print("5. Exit Menu")

    while True:
        user_choice = input("Please choose (1-5):")
        if user_choice == "1":
            viewProducts()
            print(product_list)
        elif user_choice == "2":
            createProduct()
        elif user_choice == "3":
            updateProduct()
        elif user_choice == "4":
            deleteProduct()
            print(product_list)
        elif user_choice == "5":
            print("Return to main menu")
            break
        else:
            print("Invalid Choice")
mainMenu()


## git status | git add . | git status | git commit -m"add new files" | git status git push ##