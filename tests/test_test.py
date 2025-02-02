import pytest

from aux_serverest import *


def test_get_users():
    response = get_users()
    assert response.status_code == 200
    response_json = get_user_list()
    assert isinstance(response_json, list)


def test_create_user():
    # Payload Elements
    name = "John"
    email = "john_test223@example.com"
    password = "password123"
    administrator = "true"

    # Create user
    response = create_user(name, email, password, administrator)
    assert response.status_code == 201

    # Validate Created User Content
    user_data = find_user_by_email(get_user_list(), email)
    assert user_data["nome"] == name
    assert user_data["email"] == email
    assert user_data["password"] == password
    assert user_data["administrador"] == administrator
    user_id = response.json()["_id"]
    delete_user(user_id)


def test_delete_user():
    # Test User Creation
    name = "Test"
    email = "john_test777@example.com"
    password = "password123"
    administrator = "true"

    response = create_user(name, email, password, administrator)
    user_id = response.json()["_id"]

    delete_response = delete_user(user_id)
    assert delete_response.status_code == 200
    get_response = get_user_by_id(user_id)
    assert get_response.status_code == 400


# def test_update_user():
#     # Creating the case
#     create_response = create_user("Carlos", "carlos@example.com", "password789", "false")
#     user_id = create_response.json()["_id"]
#     # Updating the case
#     update_response = update_user(user_id, name="Carlos Silva")
#     assert update_response.status_code == 200
#     response_json = update_response.json()
#     assert response_json["name"] == "Carlos Silva"


def test_clear_created_users():
    response_json = get_user_list()
    for user in response_json[1:]:
        delete_user(user["_id"])
    assert len(get_user_list()) == 1
