
import json
import requests as rq

URL='http://127.0.0.1:8000/'
def post_data():
    data={
        'name':'dsfkl',
        'email':'13@gmail.com',
        'password':'2342',
        'phone':'2343243243'
    }
    json_data=json.dumps(data)
    req= rq.post(url=URL,data=json_data)
    data=req.json()
    print(data)
post_data()