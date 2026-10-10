import json
import os

FileName = "inventory.json"

def load_inventory():
    if not os.path.exists("inventory.json"):
        return []
    
    try:
        with open("inventory.json","r") as file:
            return json.load(file)

    except(OSError):
        print("Could not read inventory.json")
        return []


def save_inventory(items):
    try:
        with open("inventory.json","w") as file:
            json.dump(items, file, indent=4)

    except OSError:
        print("Error Cous not save inventory")



def find_item(items, item_id):
    for item in items:
        if item["id"]==item_id:
            return item
    return None

def check_low_stock(items):
    for item in items:
        if item["quantity"] <item["recorderlevel"]:
            print(f'{item["name"]} only {item["quantity"]} left !!')


def add_item(items):
    try:
        item_id = int(input("Enter item id:"))

        if find_item(items,item_id):
            print("Item Id already exists")
            return

        name = input("Enter item name")

        if not name:
            print("Name cannot be empty")
            return

        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price: "))
        recorderlevel = int(input("Enter recorder level"))

        if quantity<0 or price<0 or recorderlevel<0:
            print("Values cannot be nagative")
            return

        item ={
            "id": item_id,
            "name":name,
            "quantity":quantity,
            "price":price,
            "recorderlevel":recorderlevel
        }
        items.append(item)
        save_inventory(items)
        check_low_stock(items)
        print("Item added successfully")

    except ValueError:
        print("Invalid input. Enter numbers where required")


def search_item(items):
    results=[]
    word=input("Enter item Id or Name: ").strip()
    for item in items:
        if (word.lower()==str(item["id"]).lower() or 
            word.lower() in item["name"].lower()):
            results.append(item)

    if results:
        for item in results:
            print_item(item)
    else:
        print("Item not found")

def update_stock(items):
    try:
        item_id = int(input("Enter item ID to update: "))
        item = find_item(items, item_id)

        if item is None:
            print("Item not found.")
            return
        
        quantity=int(input("Enter new quantity: "))
        if quantity<0:
            print("Quantity cannot be negative")
            return

        item["quantity"] = quantity
        save_inventory(items)
        print("Stock Updatesd")

    except ValueError:
        print("Please enter a valid integer")

# remove by id
def remove_item(items):
    try:
        item_id = int(input("Enter item ID to remove: "))
        item = find_item(items, item_id)

        if item is None:
            print("Item not found.")
            return

        items.remove(item)
        save_inventory(items)
        print("Item removed successfully.")

    except ValueError:
        print("Please enter a valid item ID.")


# Display one itwwm
def print_item(item):
    print()
    print(f'ID: {item["id"]}')
    print(f'Name: {item["name"]}')
    print(f'Quantity: {item["quantity"]}')
    print(f'Price: Rs. {item["price"]:.2f}')
    print(f'Recorder Level: {item["recorderlevel"]}')

# Display all items
def display_items(items):
    if not items:
        print("Inventory is empty.")
        return

    for item in items:
        print_item(item)


def display_menu():
    print("Choice 1: Add Item")
    print("Choice 2: Search Item")
    print("Choice 3: Update Stock")
    print("Choice 4: Remove Item")
    print("Choice 5: Display all Item")
    print("Choice 6: Show low stock items")

def Menu():
    items = load_inventory()

    display_menu()

    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            add_item(items)
        case 2:
            search_item(items)
        case 3:
            update_stock(items)
        case 4:
            remove_item(items)
        case 5:
            display_items(items)
        case 6:
            check_low_stock(items)
        case _:
            print("Invalid choice")

Menu()




