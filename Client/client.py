import os
import json
import socket
from flask import Flask
from werkzeug.datastructures import FileStorage
from flask import render_template, request
import time
import requests
from werkzeug.utils import secure_filename
from flask import request, redirect, url_for, Flask, render_template, flash

max_len = 1024

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST', 'GET'])
def sendFiles():
    if request.method == 'POST':
        file = request.files['img']
        print('file_name:' + file.name)
        file.save(secure_filename(file.filename))
        remote_IP = '192.122.236.106'
#         remote_IP = 'http://127.0.0.1'
        remote_PORT = '5000'
        remote_Sub = 'predict'
        remote_add = remote_IP + ':' + remote_PORT + '/' + remote_Sub

        files = {'image': open(secure_filename(file.filename), 'rb')}
        start_time = time.time()
        r = requests.post(remote_add, files=files)

    return r.text


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
