# import requests

# print(requests.get('http://127.0.0.1:5000/').json())
# requests.post('http://127.0.0.1:5000/', {'num':7})
# print(requests.get('http://127.0.0.1:5000/').text)

import pytest
import numSave

@pytest.fixture
def client():
    n = numSave.create_app()
    n.config['TESTING'] = True
    with n.test_client() as client:
        yield client

def test_first(client):
    rv = client.get('/')
    assert b'No entries here so far' in rv.data