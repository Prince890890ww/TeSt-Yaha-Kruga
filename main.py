from flask import Flask, render_template, request, redirect, url_for
import requests
import re
import time
import os

app = Flask(__name__)

def make_request(url, headers, cookies):
    try:
        response = requests.get(url, headers=headers, cookies=cookies).text
        return response
    except requests.RequestException as e:
        return str(e)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        password = request.form['password']
        if password == "PRINCE":
            return redirect(url_for('dashboard'))
        else:
            return render_template('index.html', error="Incorrect Password! Try again.")
    return render_template('index.html')
