#!/usr/bin/python3
"""
working on api using flask
"""
from flask import Flask
from models import storage
from api.v1.views import app_views
from os import getenv

app = Flask(__name__)
app.register_blueprint(app_views)

@app.teardown_appcontext
def call(self):
    """ calls storage.close()"""
    storage.close()

if __name__ == '__main__':
    if getenv('HBNB_API_HOST') is None:
        HBNB_MYSQL_HOST = '0.0.0.0'
    else:
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_API')
    if getenv('HBNB_MYSQL_PORT') is None:
        HBNB_MYSQL_PORT = 5000
    else:
        HBNB_MYSQL_PORT = getenv('HBNB_MYSQL_PORT')
    app.run(host=HBNB_MYSQL_HOST,port=HBNB_MYSQL_PORT, threaded=True)
    