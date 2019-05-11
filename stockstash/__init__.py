from flask import Flask
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mongoengine import MongoEngine

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'db': 'REDACTED',
    'host': 'REDACTED'
}
app.config['SECRET_KEY'] = 'some_secret_here'

# password hashing with bcrypt
bcrypt = Bcrypt(app)
# init the database
mongo = MongoEngine(app)
# login manager
login_manager = LoginManager(app)

from stockstash import routes