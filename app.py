from flask import Flask, jsonify, request
from models import inventory
import requests

app = Flask(__name__)

#all routes for inventory management
@app.route('/inventory', methods=['GET'])
def get_inventory():
    return jsonify(inventory)

#route to get item by id
@app.route('/inventory/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in inventory if item['id'] == item_id), None)
    if item:
        return jsonify(item)
    else:
        return jsonify({'message': 'Item not found'}), 

#route to add new item to inventory
@app.route('/inventory', methods=['POST'])
def add_item():
    new_item = request.get_json()
    inventory.append(new_item)
    return jsonify(new_item), 

#update item in inventory
@app.route('/inventory/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in inventory if item['id'] == item_id), None)
    if item:
        updated_data = request.get_json()
        item.update(updated_data)
        return jsonify(item)
    else:
        return jsonify({'message': 'Item not found'}), 

#delete item from inventory
@app.route('/inventory/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    item = next((item for item in inventory if item['id'] == item_id), None)
    if item:
        inventory.remove(item)
        return jsonify({'message': 'Item deleted'})
    else:
        return jsonify({'message': 'Item not found'}),  

#route to fetch external data
@app.route('/external-data', methods=['GET'])
def fetch_external_data():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({'message': 'Failed to fetch external data'}),



if __name__ == '__main__':
    app.run(debug=True)