#!/usr/bin/python3
"""
working on api using flask
"""
from flask import Flask
from models import storage
from api.v1.views import app_views  #type: ignore
from os import getenv

app = Flask(__name__)
app.register_blueprint(app_views)

@app.teardown_appcontext
def call():
    """ calls storage.close()"""
    storage.close()


HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
if not HBNB_MYSQL_HOST:
    HBNB_MYSQL_HOST = '0.0.0.0'
    

if __name__ == '__main__':
    app.run(HBNB_MYSQL_HOST, port=5000)