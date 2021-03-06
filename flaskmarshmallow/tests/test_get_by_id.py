from flask import json


def test_get_by_id(test_client, init_database):
    response = test_client.get('/users/1')

    data = json.loads(response.data)

    assert response.status_code == 200
    assert data['user']['name'] == 'Eric Anderson'
    assert data['user']['password'] == 'testpass2'
