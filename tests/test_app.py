from http import HTTPStatus

from fastapi.testclient import TestClient


def test_root_deve_retornar_ola_mundo(client: TestClient):
    """
    - Arrange: cria client de teste
    - Act: faz GET na rota '/'
    - Assert: valida JSON e status code
    """

    # Arrange

    # Act
    response = client.get('/')

    # Assert
    assert response.json() == {'message': 'Olá mundo!'}
    assert response.status_code == HTTPStatus.OK


def test_create_user(client):

    response = client.post(
        '/users/',
        json={
            'username': 'testusername',
            'password': 'password',
            'email': 'teste@gmail.com',
        },
    )

    # status esta correto?
    assert response.status_code == HTTPStatus.CREATED

    # conteúdo retornado usuário público
    assert response.json() == {
        'username': 'testusername',
        'email': 'teste@gmail.com',
        'id': 1,
    }


def teste_read_users(client: TestClient):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'username': 'testusername',
                'email': 'teste@gmail.com',
                'id': 1,
            }
        ]
    }


def test_uptade_user(client):

    response = client.put(
        '/users/1',
        json={
            'password': '123',
            'username': 'testusername2',
            'email': 'teste@gmail.com',
            'id': 1,
        },
    )
    assert response.json() == {
        'username': 'testusername2',
        'email': 'teste@gmail.com',
        'id': 1,
    }

    def test_delete_user(client):
        response = client.delete('/users/1')

        assert response.json() == {'massage': 'User deleted'}
