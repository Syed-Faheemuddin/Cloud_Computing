from flask import Flask, jsonify, request


class Product:
    def __init__(self, id, name, description, price):
        self.id = id
        self.name = name
        self.description = description
        self.price = price

    def __repr__(self):
        return f"Product(id={self.id}, name={self.name}, description={self.description}, price={self.price})"


class User:
    def __init__(self, id, name, email, password):
        self.id = id
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, email={self.email}, password={self.password})"


app = Flask(__name__)

products = [
    {
        "id": 1,
        "name": "Product 1",
        "description": "This is a product.",
        "price": 10.00,
    },
    {
        "id": 2,
        "name": "Product 2",
        "description": "This is another product.",
        "price": 20.00,
    },
]

users = [
    {
        "id": 1,
        "name": "User 1",
        "email": "user1@example.com",
        "password": "password"
    },
    {
        "id": 2,
        "name": "User 2",
        "email": "user2@example.com",
        "password": "password"
    },
    {
        "id": 3,
        "name": "User 3",
        "email": "user3@example.com",
        "password": "password"
    }
]


@app.route("/products")
def get_all_products():
    return jsonify(products)


@app.route("/products/<product_id>")
def get_product(product_id):
    for product in products:
        if product["id"] == int(product_id):
            return jsonify(product)
    return jsonify({"message": "product not found"})


@app.route("/products/<product_id>/purchase", methods=["POST"])
def purchase_product(product_id):
    user = request.json["user"]
    for product in products:
        if product["id"] == int(product_id):
            product["purchased_by"] = user
            return jsonify({"message": "Product purchased successfully"})
    return jsonify({"message": "Product Not available"})


@app.route("/products", methods=["POST"])
def add_product():
    admin = request.json["admin"]
    product = request.json["product"]
    products.append(product)
    return jsonify({"message": "Product added successfully"})


@app.route("/users")
def get_all_users():
    return jsonify(users)


@app.route("/users/<user_id>")
def get_user(user_id):
    for user in users:
        if user["id"] == int(user_id):
            return jsonify(user)
    return jsonify({"message": "User not found"})

#{"user":{ "id":1, "name":"Syed", "email":"syed@gmail.com","password":"syed"}}
@app.route("/users", methods=["POST"])
def create_user():
    user = request.json["user"]
    users.append(user)
    return jsonify({"message": "User created successfully"})


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8004,debug=True)
