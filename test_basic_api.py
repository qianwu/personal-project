import json

import pytest
import requests


def test_status_code():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    assert response.status_code == 200


def test_response_body():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    assert len(response.json()) == 100


@pytest.mark.parametrize("post_id", [1, 2, 3, 4, 5])
def test_response_body(post_id):
    response = requests.get("https://jsonplaceholder.typicode.com/posts/{}".format(post_id))
    assert response.json()['id'] == post_id


def test_post_request():
    payload = {'title': 'foo', 'body': 'bar', 'userId': 1}
    response = requests.post("https://jsonplaceholder.typicode.com/posts", data=payload)
    assert response.status_code == 201
    assert response.json()['title'] == 'foo'
    assert response.json()['body'] == 'bar'
    assert response.json()['userId'] == "1"
    assert 'id' in response.json()
    assert response.json()['id'] == 101


data_set = [
    ("us", "90201", "Bell Gardens"),
    ("it", "50123", "Beverly Hills")
]


@pytest.mark.parametrize("country_code, zip_code, expected_place_name", data_set)
def test_for_place_name(country_code, zip_code, expected_place_name):
    response = requests.get(f"https://api.zippopotam.us/{country_code}/{zip_code}")
    body = response.json()
    assert body['places'][0]['place name'] == expected_place_name


data_set1 = [("1", "Leanne Graham", "Romaguera-Crona"), ("2", "Ervin Howell", "Deckow-Crist"), ("3", "Clementine Bauch", "Romaguera-Jacobson")]

@pytest.mark.parametrize("id, name, company_name", data_set1)
def test_for_parametrize(id,name,company_name):
    response = requests.get(f"https://jsonplaceholder.typicode.com//users/{id}")
    body = response.json()
    assert body['name'] == name
    assert body['company']['name'] == company_name

# test logged_session fixture
def test_logged_session(logged_session):
    response = logged_session.get("https://jsonplaceholder.typicode.com/posts")
    assert response.status_code == 200
    assert len(response.json()) == 100
    response = logged_session.get("https://jsonplaceholder.typicode.com/posts/1")
    assert response.json()['id'] == 1

    response = logged_session.get("https://api.zippopotam.us/us/90201")
    body = response.json()
    assert body['places'][0]['place name'] == "Bell Gardens"
    response = logged_session.get("https://jsonplaceholder.typicode.com//users/1")
    body = response.json()
    assert body['name'] == "Leanne Graham"
    assert body['company']['name'] == "Romaguera-Crona"

def test_logged_session_post(logged_session):
    payload = {'title': 'foo', 'body': 'bar', 'userId': 1}
    response = logged_session.post("https://jsonplaceholder.typicode.com/posts", data=payload)
    assert response.status_code == 201
    assert response.json()['title'] == 'foo'
    assert response.json()['body'] == 'bar'
    assert response.json()['userId'] == "1"
    assert 'id' in response.json()
    assert response.json()['id'] == 101