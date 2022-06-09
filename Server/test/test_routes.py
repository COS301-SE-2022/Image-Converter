import json
from app import app
import pytest

client = app.test_client()


def test_base_route():
    url = '/'
    res = client.get(url)
    assert res.get_data() == b'Hello World!'
    assert res.status_code == 200


# @pytest.mark.xfail(reason="Still need to cater for the user tokens")
def test_picture_route():
    url = '/picture'
    res = client.post(url, content_type="application/json", data=json.dumps({'picture': 'Server/images/image1.jpg'}))
    assert res.status_code == 200
    assert res.content_type == "application/json"

# @pytest.mark.xfail(reason="Fix the database config for register")
def test_register():
    user = {
        'name': 'Neo',
        'surname': 'Seefane',
        'email': 'neoseefane13@gmail.com',
        'password': '1234@Neo'
    }
    url = '/register'
    res = client.post(url, data=json.dumps(user))
    # print(res.get_data)
    assert res.status_code == 200

# @pytest.mark.xfail(reason="Fix the database config for login")
def test_login():
    invalid_user = {
        'username': 'neoseefane13@gmail.com',
        'password': '1234@Neo'
    }
    url = '/login'
    res = client.post(url, data=json.dumps(invalid_user))
    assert res.status_code == 200
    

def test_render_template():
    url = '/template'
    res = client.get(url)
    assert res.status_code == 200
