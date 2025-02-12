from aux_serverest import *


def test_get_products():
    response = get_products()
    assert response.status_code == 200
    response_json = get_products_list()
    assert isinstance(response_json, list)


def test_get_product_by_id():
    product_id = get_dynamic_product_id()
    response = get_product_by_id(product_id)
    response_json = response.json()

    assert response.status_code == 200
    assert response_json['_id'] == product_id


def test_create_products():
    # Payload User Elements
    name = "Mary"
    email = "mary_test223@example.com"
    password = "password123"
    administrator = "true"
    response_user = create_user(name, email, password, administrator)

    # Get Login Token
    authorization_token = login(email, password)[1]
    # Payload Product Elements
    product_name = 'iPhone 14'
    preco = 4500
    descricao = 'Cell phone'
    quantidade = 100

    # Create product
    response_product = create_product(authorization_token, product_name, preco, descricao, quantidade)
    assert response_product.status_code == 201

    # Validate Created Product Content
    print(">>>>>>>>>>>>>>>>> get_products_list()" + str(get_products_list()))
    product_data = find_product_by_name(get_products_list(), product_name)
    assert product_data["nome"] == product_name
    assert product_data["preco"] == preco
    assert product_data["descricao"] == descricao
    assert product_data["quantidade"] == quantidade
    # product_id = response_product.json()["_id"]
    # user_id = response_user.json()["_id"]
    # delete_user(user_id)
    # delete_product(product_id)
