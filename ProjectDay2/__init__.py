import requests
from flask import Flask, render_template
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app)


@app.route('/')
def hello_world():
    return '<h1 style="text-align: center;">Hello Mas Wawan Ridwan yang Ganteng<h1>'

#def index():
   # categories = requests.get('http://127.0.0.1:8000/categories/')
    #categories = categories.json()

#    return render_template('index.html', categories=categories)

#   return render_template('index.html')
