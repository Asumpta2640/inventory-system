import requests

BASE_URL = "http://127.0.0.1:5000"


def get_inventory():
    response = requests.get(f'{BASE_URL}/products')
    if response.status_code == 200:
        inventory = response.json()
        print("Inventory:")
        for item in inventory:
            print(f"ID: {item['id']}, Name: {item['name']}, Quantity: {item['quantity']}, Price: {item['price']}")
    else:
        print("Failed to fetch inventory")      

if __name__ == '__main__':
    get_inventory()
    
