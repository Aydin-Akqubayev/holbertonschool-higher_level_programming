from flask import Flask, jsonify, request
from collections import OrderedDict

app = Flask(__name__)

# Sample users (ordered)
users = {
    "jane": OrderedDict([
        ("username", "jane"),
        ("name", "Jane"),
        ("age", 28),
        ("city", "Los Angeles")
    ]),
    "john": OrderedDict([
        ("username", "john"),
        ("name", "John"),
        ("age", 30),
        ("city", "New York")
    ])
}


@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.route("/data")
def data():
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    return jsonify({"status": "OK"})


@app.route("/users/<username>")
def get_user(username):
    user = users.get(username)
    if not user:
        return jsonify({"message": "User not found"}), 404
    return jsonify(user)


@app.route("/users", methods=["POST"])
def add_user():
    user_data = request.get_json(silent=True) or {}

    # Validation
    required_fields = {"username", "name", "age", "city"}
    if not all(user_data.get(field) for field in required_fields):
        return jsonify({"message": "Missing required fields"}), 400

    username = user_data["username"]

    if username in users:
        return jsonify({"message": "User already exists"}), 409

    new_user = OrderedDict({
        "username": username,
        "name": user_data["name"],
        "age": user_data["age"],
        "city": user_data["city"]
    })

    users[username] = new_user
    return jsonify({"message": "User added", "user": new_user}), 201


if __name__ == "__main__":
    app.run(debug=False)
