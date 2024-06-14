import csv #Importing to CSV File 


# Function to load deliveries from a CSV file
def load_couriers(filename="couriers.csv"):
    couriers = []
    try:
        with open("couriers.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                couriers.append(row)
        return couriers
    except FileNotFoundError:
        print("No existing deliveries found. Starting fresh.\n")

# Function to save deliveries to a CSV file
def save_deliveries(couriers,filename="couriers.csv"):
    with open(filename, mode='w', newline='') as file:
        fieldnames = ['sender', 'receiver', 'address']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        writer.writeheader()
        # for courier in couriers:
        writer.writerow(couriers)

# Function to add a new delivery
def add_couriers(couriers):
    sender = input("Enter sender's name: ")
    receiver = input("Enter receiver's name: ")
    address = input("Enter delivery address: ")
    courier = {
        'sender': sender,
        'receiver': receiver,
        'address': address
    }
    couriers.append(courier)
    print("Delivery added successfully!\n")
    save_deliveries(courier)  # Save to file after adding a delivery

# Function to view all deliveries
def view_couriers(couriers):
    if not couriers:
        print("No deliveries available.\n")
    else:
        for i, delivery in enumerate(couriers, 1):
            print(f"Delivery {i}:")
            print(f"  Sender: {delivery['sender']}")
            print(f"  Receiver: {delivery['receiver']}")
            print(f"  Address: {delivery['address']}\n")
