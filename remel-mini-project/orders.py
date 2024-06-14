import csv #Import into Csv File
orders = [] #Empty list


# Function to load orders from CSV file
def loadOrdersFromCSV():
    global orders
    try:
        with open('orders.csv', mode='r') as file:
            reader = csv.DictReader(file)
            orders = [row for row in reader]
    except FileNotFoundError:
        print("No existing orders file found. Starting with an empty orders list.")

# Function to save orders to CSV file
def saveOrdersToCSV():
    with open('orders.csv', mode='w', newline='') as file:
        fieldnames = ['Name', 'Address', 'Contact Number', 'Status']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(orders)


## - ORDERS MENU - ##
def customerMenu():
    print("1. Create Orders\n2. Update Orders Menu\n3. Delete Order\n4. Return to Main Menu")
    return


 ## Capture user input and Create an order##
def createOrders(orders):
    customer_name = input("Please Enter fullname: \n")  ## Take name, address and contact number.
    customer_address = input("Please enter Email: \n")
    customer_phone = input("Please enter your contact number: \n")
    order_status = input("Pending!!!")


    order = {
        "Name": customer_name,
        "Address": customer_address,
        "Contact Number": customer_phone,
        "Status": order_status,
    }
    
    orders.append(order)  ## Take order 
    print(order)  ## Print order
    print("Order added successfully!") ##Confirmation message  
    saveOrdersToCSV()  ## Store in Orders.csv file
        


##Update Orders ##
def updateOrders(): 
    print("Current Orders:")  ##Print current Order
    for index, order in enumerate(orders):
        print(f"{index + 1}. {order}")
    try:
        order_index = int(input("Enter the order to update: ")) ##Update Orders in csv file
        if 0 <= order_index < len(orders):
            custommer_name = input("Please enter your full name: \n")
            customer_address = input("Please enter your email: \n")
            customer_number = input("Please add you contact number: \n")
            orders_status = input("Enter new status: \n")
            
            orders[order_index] = {
                "name": custommer_name,
                "address": customer_address,
                "Contact Number": customer_number,
                "Status": orders_status,
            }

            print("Order updated successfully :)")
            saveOrdersToCSV()   ##Save changes of orders csv file.
        else:
            print("|Invalid order number")
    except ValueError:
        print("Please enter a vild order number. \n")
                


## Delete Orders
def deleteOrders():
    if not orders:
        print("No orders to delete")
        return
    
    print("Current Orders: ")
    for index, order in enumerate(orders):
        print(f"{index + 1}. {order}")

    try:
        order_index = int(input("Enter the order number to delete: ")) - 1
        if 0 <= order_index < len(orders):
            orders.pop(order_index)   
            print("Order successfully deleted :)")
            saveOrdersToCSV()
        else:
            print("Invalid order number.")
    except ValueError:
        print("Please enter a valid order number. \n")