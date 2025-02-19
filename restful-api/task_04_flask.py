#!/usr/bin/python3
"""Ceci est une description"""


from flask import Flask, jsonify, request

app = Flask(__name__)

users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}

@app.route("/")
def home():
    """Ceci est une description"""
    return "Welcome to the Flask API!"

@app.route("/data")
def get_users():
    """Ceci est une description"""
    return jsonify(list(users.keys()))

@app.route("/status")
def status():
    """Ceci est une description"""
    return "OK"

@app.route("/users/<username>")
def get_user(username):
    """Ceci est une description"""
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=["POST"])
def add_user():
    """Ceci est une description"""
    data = request.get_json()
    if "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data["username"]
    if username in users:
        return jsonify({"error": "User already exists"}), 400

    users[username] = {
        "username": username,
        "name": data.get("name", ""),
        "age": data.get("age", 0),
        "city": data.get("city", "")
    }

    return jsonify({"message": "User added", "user": users[username]}), 201

if __name__ == "__main__":
    app.run(debug=True)
