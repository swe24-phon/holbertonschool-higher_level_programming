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

@app.route('/users/<username>')
def show_user_profile(username):
    """ Show the profile for that user """
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User  not found"}), 404

@app.route('/add_user', methods=['POST'])
def add_user():
    """ Add a new user """
    try:
        username = request.json['username']
        name = request.json['name']
        age = request.json['age']
        city = request.json['city']
        
        if username in users:
            return jsonify({"error": "User  already exists"}), 400
        
        user = {
            "username": username,
            "name": name,
            "age": age,
            "city": city
        }
        users[username] = user  # Add user to the users dictionary
        return jsonify({"message": "User  added", "user": user}), 201
    
    except KeyError as e:
        return jsonify({"error": f"{str(e).capitalize()} is required"}), 400

if __name__ == "__main__":
    app.run(debug=True, port=5000)