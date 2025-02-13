import requests
import json

# Base URL of the API
BASE_URL = "http://localhost:3000"  # Replace with the actual URL if different
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


def get_products():
    url = f"{BASE_URL}/produtos"
    response = requests.get(url, headers=HEADERS)
    return response


def get_products_list():
    url = f"{BASE_URL}/produtos"
    response = requests.get(url, headers=HEADERS)
    return response.json()["produtos"]


def get_product_by_id(product_id):
    url = f"{BASE_URL}/produtos/{product_id}"
    response = requests.get(url, headers=HEADERS)
    return response


# Getting product ID and name

def get_dynamic_product():
    url = f"{BASE_URL}/produtos"
    response = requests.get(url, headers=HEADERS)
    response_json = response.json()

    dynamic_id = response_json["produtos"][0]["_id"]  # if we don't have a static id
    dynamic_name = response_json["produtos"][0]["nome"]

    return dynamic_id, dynamic_name


def create_product(authorization_token, product_name, preco, descricao, quantidade):
    url = f"{BASE_URL}/produtos"
    HEADER_AUTHORIZATION = {"Authorization": f"{authorization_token}"}
    payload = {
        "nome": product_name,
        "preco": preco,
        "descricao": descricao,
        "quantidade": quantidade
    }

    response = requests.post(url, headers=HEADER_AUTHORIZATION, json=payload)

    return response


# Find product by name
def find_product_by_name(product_list, product_name):
    for product in product_list:
        if product['nome'] == product_name:
            return product
    return None


# Function to delete a product
def delete_product(authorization_token, product_id):
    url = f"{BASE_URL}/produtos/{product_id}"
    HEADER_AUTHORIZATION = {"Authorization": f"{authorization_token}"}
    response = requests.delete(url, headers=HEADER_AUTHORIZATION)
    return response
