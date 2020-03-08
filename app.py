from flask import Flask,jsonify,request
from flask_cors import CORS
import requests
import json


app = Flask(__name__)
CORS(app)

@app.route('/base64',methods=['POST'])
def base64_to_binary():
    request_data = request.get_json()
    base64str = request_data['url']
    url = 'https://api.imgur.com/3/image'
    myobj = {
        'image': base64str}
    headers = {'Content-Type': 'application/x-www-form-urlencoded',
               'Authorization': 'Client-ID 641970866dba431', }
    x = requests.post(url, headers=headers, data=myobj)
    y = json.loads(x.text)
    return y['data']['link']






if __name__ == '__main__':
    app.run()
