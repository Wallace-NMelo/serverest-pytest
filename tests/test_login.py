from aux_serverest import *

wrong_email = "jao_test_login@example.com"
wrong_password = "senha"


def test_login_success():
    # Payload Elements
    name = "João Login da Silva"
    email = "joao_test_login@exemplo.com"
    password = "senha123"
    administrator = "true"

    create_user(name, email, password, administrator)

    response, token = login(email, password)
    assert response.status_code == 200
    assert response.json()["message"] == 'Login realizado com sucesso'
    print(">>>>>>>>>>>>>>>>>>>>>> TOKEEEEEEEN " + token)


def test_login_email_failed():
    # Payload Elements
    name = "João Login da Silva"
    email = "joao_test_login@example.com"
    password = "senha123"
    administrator = "true"

    create_user(name, email, password, administrator)

    response, token = login(wrong_email, password)
    assert response.status_code == 401
    assert response.json()["message"] == 'Email e/ou senha inválidos'


def test_login_password_failed():
    # Payload Elements
    name = "João Login da Silva"
    email = "joao_test_login@example.com"
    password = "senha123"
    administrator = "true"

    create_user(name, email, password, administrator)

    response, token = login(email, wrong_password)
    assert response.status_code == 401
    assert response.json()["message"] == 'Email e/ou senha inválidos'


def test_login_email_password_failed():
    # Payload Elements
    name = "João Login da Silva"
    email = "joao_test_login@example.com"
    password = "senha123"
    administrator = "true"

    create_user(name, email, password, administrator)

    response, token = login(wrong_email, wrong_email)
    assert response.status_code == 401
    assert response.json()["message"] == 'Email e/ou senha inválidos'
