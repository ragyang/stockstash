from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'REDACTED'
app.config['MONGO_URI'] = 'REDACTED'

#init the database
mongo = PyMongo(app)

from stockstash import routes