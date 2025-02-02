import requests
import json

# Base URL of the API
BASE_URL = "http://localhost:3000"  # Replace with the actual URL if different
TOKEN = "your_token_here"  # Replace with your JWT token

# Headers for authentication
# HEADERS = {
#     "Authorization": f"Bearer {TOKEN}",
#     "Content-Type": "application/json"
# }

HEADERS = {}


# Function to create a user
def create_user(name, email, password, administrator):
    url = f"{BASE_URL}/usuarios"
    payload = {
        "nome": name,
        "email": email,
        "password": password,
        "administrador": administrator
    }
    response = requests.post(url, headers=HEADERS, json=payload)
    return response


# Function to get all users
def get_users():
    url = f"{BASE_URL}/usuarios"
    response = requests.get(url, headers=HEADERS)
    return response


# Function to get the list of users
def get_user_list():
    url = f"{BASE_URL}/usuarios"
    response = requests.get(url, headers=HEADERS)
    return response.json()["usuarios"]


# Function to get a user by ID
def get_user_by_id(user_id):
    url = f"{BASE_URL}/usuarios/{user_id}"
    response = requests.get(url, headers=HEADERS)
    return response


# Function to update a user
def update_user(user_id, name=None, email=None, password=None, administrator=None):
    url = f"{BASE_URL}/usuarios/{user_id}"
    payload = {}
    if name:
        payload["nome"] = name
    if email:
        payload["email"] = email
    if password:
        payload["password"] = password
    if administrator is not None:
        payload["administrador"] = administrator

    response = requests.put(url, headers=HEADERS, json=payload)
    return response


# Function to delete a user
def delete_user(user_id):
    url = f"{BASE_URL}/usuarios/{user_id}"
    response = requests.delete(url, headers=HEADERS)
    return response


# Function to log in
def login(email, password):
    login_endpoint = f"{BASE_URL}/login"
    login_data = {
        "email": email,
        "password": password
    }
    response = requests.post(login_endpoint, json=login_data)
    response_json = response.json()
    authorization_token = response_json.get('authorization')
    return response, authorization_token


# Function to search for a user by email
def find_user_by_email(user_list, target_email):
    for user in user_list:
        if user['email'] == target_email:
            return user
    return None
