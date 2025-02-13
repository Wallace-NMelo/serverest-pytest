from aux_serverest import *

wrong_email = "jao_test_login@example.com"
wrong_password = "senha"


def test_login_success():
    # Payload Elements
    name = "João Login da Silva"
    email = "joao_test_login@example.com"
    password = "senha123"
    administrator = "true"

    response_user = create_user(name, email, password, administrator)
    # print(">>>>>>>>>>>>>>>> response_user.json() " + str(response_user.json()))
    response, token = login(email, password)
    assert response.status_code == 200
    assert response.json()["message"] == 'Login realizado com sucesso'

    user_id = response_user.json()['_id']
    delete_user(user_id)


def test_login_email_failed():
    # Payload Elements
    name = "João Login da Silva"
    email = "joao_test_login@example.com"
    password = "senha123"
    administrator = "true"

    response_user = create_user(name, email, password, administrator)

    response, token = login(wrong_email, password)

    assert response.status_code == 401
    assert response.json()["message"] == 'Email e/ou senha inválidos'

    user_id = response_user.json()['_id']
    delete_user(user_id)


def test_login_password_failed():
    # Payload Elements
    name = "João Login da Silva"
    email = "joao_test_login@example.com"
    password = "senha123"
    administrator = "true"

    response_user = create_user(name, email, password, administrator)

    response, token = login(email, wrong_password)
    assert response.status_code == 401
    assert response.json()["message"] == 'Email e/ou senha inválidos'

    user_id = response_user.json()['_id']
    delete_user(user_id)


def test_login_email_password_failed():
    # Payload Elements
    name = "João Login da Silva"
    email = "joao_test_login@example.com"
    password = "senha123"
    administrator = "true"

    response_user = create_user(name, email, password, administrator)

    response, token = login(wrong_email, wrong_email)
    assert response.status_code == 401
    assert response.json()["message"] == 'Email e/ou senha inválidos'

    user_id = response_user.json()['_id']
    delete_user(user_id)
