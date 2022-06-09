# import json
# from app import app

# def test_base_route():
#     client = app.test_client()
#     url = '/'
#     res = client.get(url)
#     assert res.get_data() == b'Hello World!'
#     assert res.status_code == 200

# def test_picture_route():
#     client = app.test_client()
#     url = '/picture'
#     res = client.post(url, content_type = "application/json", data = json.dumps({'picture': 'Server/images/image1.jpg'}))
#     assert res.status_code == 200
#     assert res.content_type == "application/json"
