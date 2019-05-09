from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'stockstash'
app.config['MONGO_URI'] = 'mongodb://admin:ZQTymqcbB6aZgtRY@ds149056.mlab.com:49056/stockstash'

#init the database
mongo = PyMongo(app)

from stockstash import routes