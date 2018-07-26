from flask import Flask, jsonify, abort, request
from app.models import theDatabase

app = Flask(__name__)


#List to hold the Entry data

entries = [
    {
        "id": 0,
        "title": "My Name",
        "description": "Weep not child for I am with you"
    },
    {
        "id": 1,
        "title": "His Word",
        "description": "And His word was made flesh"
    },
    {
        "id": 2,
        "title": "The World",
        "description": "No matter what happens, keep moving forward"
    }
]

users = [
    {
        "id": 1,
        "username": "ramon",
        "email": "ramonomondi@gmail.com",
        "password": "1234"
    }
]

@app.route('/api/v1/entries', methods=['GET'])
def get_all_entries():
    """Gets all the entries by the user"""

    return theDatabase().get_all_entries()

@app.route('/api/v1/entries/<int:entry_id>', methods=['GET'])
def get_single_entry(entry_id):
    """Gets a single entry from the user"""

    return theDatabase().get_one_entry(entry_id)

@app.route('/api/v1/entries', methods=['POST'])
def create_entry():
    """Creates a single entry"""
    
    if not request.json:
        abort(400)
    elif not 'title' in request.json:
        return jsonify({'message' : 'Title is required'}), 400
    elif not 'description' in request.json:
        return jsonify({'message' : 'Description is required'}), 400

    title = request.json['title']
    description = request.json['description']
    
    entry_data = {
        'title' : title,
        'description' : description,
    }

    # theDatabase().create_entry_table()
    return theDatabase().add_entry(entry_data)

@app.route('/api/v1/entries/<int:entry_id>', methods=['PUT'])
def update_entry(entry_id):
    """Updates a single entry"""

    title = request.json['title']
    description = request.json['description']
    
    entry_data = {
        'title' : title,
        'description' : description,
    }

    return theDatabase().update_entry(entry_id, entry_data)

@app.route('/api/v1/entries/<int:entry_id>', methods=['DELETE'])
def delete_entry(entry_id):
    """Deletes a single entry"""

    return theDatabase().delete_entry(entry_id)
    
@app.route('/auth/signup', methods=['POST'])
def signup():
    """Creates a user"""

    if not request.json:
        abort(400)
    elif not 'username' in request.json:
        return jsonify({'message' : 'Username is required'}), 400
    elif not 'email' in request.json:
        return jsonify({'message' : 'Email is required'}), 400
    elif not 'password' in request.json:
        return jsonify({'message' : 'Password is required'}), 401

    username = request.json['username']
    password = request.json['password']
    email = request.json['email']
  
    
    user_data = {
        'username': username,
        'password': password,
        'email': email,         
    }

    
    # theDatabase().create_user_table()
    return theDatabase().signup(user_data)


@app.route('/auth/login', methods=['POST'])
def login():
    """Logs a user into the system"""
    
    if not request.json:
        abort(400)
    elif not 'username' in request.json:
        return jsonify({'message' : 'Username is required'}), 400
    elif not 'password' in request.json:
        return jsonify({'message' : 'Password is required'}), 401

    username = request.json['username']
    password = request.json['password']
  
    
    return theDatabase().login(password, username)
   