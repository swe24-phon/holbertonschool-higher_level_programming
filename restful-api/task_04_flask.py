#!/usr/bin/python3
""" This module fetches posts from the API and prints them to the console """
from flask import Flask
from flask import jsonify, request

app = Flask(__name__)

# Initialize an empty users dictionary to store user data
users = {}

@app.route('/')
def home():
    """ Home endpoint """
    return "Welcome to the Flask API!"

@app.route('/data')
def data():
    """ Data endpoint """
    return jsonify(list(users.keys()))  # Return a list of usernames

@app.route('/status')
def status():
    """ Status endpoint """
    return "OK"

@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_json()
    username = data.get("username")

    # Check if the user already exists
    if username in users:
        return jsonify({"error": "User  already exists"}), 400

    # Add the new user
    users[username] = {
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city"),
    }

    # Return the added user information
    return jsonify(users[username]), 201  # Return the user data instead of a message

@app.route("/users/<username>")
def get_username(username):
    if username not in users:
        return jsonify({"error": "User  not found"}), 404

    user_info = users[username]
    user_info["username"] = username

    return jsonify(user_info)
# @app.route('/users/<username>')
# def show_user_profile(username):
#     """ Show the profile for that user """
#     user = users.get(username)
#     if user:
#         return jsonify(user)
#     else:
#         return jsonify({"error": "User  not found"}), 404

# @app.route('/add_user', methods=['POST'])
# def add_user():
#     """ Add a new user """
#     try:
#         # Attempt to get the username from the incoming JSON request
#         username = request.json['username']  # This will raise KeyError if username is not present
#         name = request.json['name']
#         age = request.json['age']
#         city = request.json['city']
        
#         # Check if the user already exists
#         if username in users:
#             return jsonify({"error": "User  already exists"}), 400
        
#         # Create a new user object
#         user = {
#             "username": username,
#             "name": name,
#             "age": age,
#             "city": city
#         }
#         users[username] = user  # Add user to the users dictionary
#         return jsonify({"message": "User  added", "user": user}), 201
    
#     except KeyError as e:
#         # Handle the case where a required field is missing
#         return jsonify({"error": f"{str(e).capitalize()} is required"}), 400

if __name__ == "__main__":
    app.run(debug=True, port=5000)