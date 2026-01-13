from http import HTTPStatus


def test_root_deve_retornar_ok_e_ola_mundo(client):
    response = client.get("/")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "Olá Mundo!"}


def test_create_user(client):

    response = client.post(
        "/users/",
        json={
            "username": "João Mozelli",
            "email": "joaomozelli@gmail.com",
            "password": "secret",
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        "username": "João Mozelli",
        "email": "joaomozelli@gmail.com",
        "id": 1,
    }


def test_read_users(client):
    response = client.get("/users/")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "users": [
            {
                "username": "João Mozelli",
                "email": "joaomozelli@gmail.com",
                "id": 1,
            }
        ]
    }


def test_read_user_by_id(client):
    response = client.get("/users/1")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "username": "João Mozelli",
        "email": "joaomozelli@gmail.com",
        "id": 1,
    }


def test_error_read_user_by_id(client):
    response = client.get("/users/70")

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {"detail": "User not found"}


def test_update_user(client):
    response = client.put(
        "/users/1",
        json={
            "username": "João Mozelli Neto",
            "email": "joaomozelli@hotmail.com",
            "password": "mynewpassword",
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "username": "João Mozelli Neto",
        "email": "joaomozelli@hotmail.com",
        "id": 1,
    }


def test_error_update_user(client):
    response = client.put(
        "/users/-2",
        json={
            "username": "João Mozelli Neto",
            "email": "joaomozelli@gmail.com",
            "password": "mynewpassword",
        },
    )

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {"detail": "User not found"}


def test_delete_user(client):
    response = client.delete("/users/1")

    assert response.status_code == HTTPStatus.OK


def test_error_delete_user(client):
    response = client.delete("/users/30")

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {"detail": "User not found"}
