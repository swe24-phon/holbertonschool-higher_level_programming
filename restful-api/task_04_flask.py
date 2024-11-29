#!/usr/bin/python3
""" This module fetches posts from the API and prints them to the console """
from flask import Flask
from flask import jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    """ Home endpoint """
    return "Welcome to the Flask API!"

@app.route('/data')
def data():
    """ Data endpoint """
    users = {
        "jane": {"name": "Jane",
                 "age": 28, "city": "Los Angeles"}}
    return jsonify(users)

@app.route('/status')
def status():
    """ Status endpoint """
    return "OK"

@app.route('/info')
def info():
    """ Info endpoint """
    info_data = {
        "version": "1.0",
        "description": "A simple API built with Flask"
    }
    return jsonify(info_data)

@app.route('/users/<username>')
def show_user_profile(username):
    """ Show the profile for that user """
    return f'User {username}'

@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    """ Add a new user """
    if request.method == 'POST':
        # create a new user
        username = {"username": request.form['username'],
                    "user": request.form['user'],
                    "age": request.form['age'],
                    "city": request.form['city']}
        users = {username['username']: username}
        return jsonify(username)
    else:
        return "Add a user"
    

if __name__ == "__main__":
    app.run(debug=True, port=5000)