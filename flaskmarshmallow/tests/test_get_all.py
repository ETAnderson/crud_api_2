from flask import json


def test_get_all(test_client, init_database):
    response = test_client.get('/users')

    data = json.loads(response.data)

    assert response.status_code == 200
    assert data['users'][0]['name'] == 'Eric Anderson'
    assert data['users'][0]['password'] == 'testpass2'

    assert data['users'][1]['name'] == 'Rochelle Anderson'
    assert data['users'][1]['password'] == 'Rochellepass'
