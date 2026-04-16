from flask import Flask, jsonify, request
from models import inventory

app = Flask(__name__)

# GET all products
@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(inventory)

# GET one product
@app.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    for product in inventory:
        if product["id"] == id:
            return jsonify(product)
    return {"error": "Not found"}, 404

# POST (add product)
@app.route('/products', methods=['POST'])
def add_product():
    data = request.json
    new_product = {
        "id": len(inventory) + 1,
        "product_name": data["product_name"],
        "brand": data["brand"],
        "ingredients": data["ingredients"],
        "quantity": data["quantity"]
    }
    inventory.append(new_product)
    return jsonify(new_product), 201

# PATCH (update)
@app.route('/products/<int:id>', methods=['PATCH'])
def update_product(id):
    data = request.json
    for product in inventory:
        if product["id"] == id:
            product["quantity"] = data.get("quantity", product["quantity"])
            return jsonify(product)
    return {"error": "Not found"}, 404

# DELETE
@app.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    for product in inventory:
        if product["id"] == id:
            inventory.remove(product)
            return {"message": "Deleted"}
    return {"error": "Not found"}, 404

if __name__ == '__main__':
    app.run(port=5555, debug=True)
