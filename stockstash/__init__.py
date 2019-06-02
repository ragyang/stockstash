from flask import Flask
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mongoengine import MongoEngine
from flask_mail import Mail

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'db': 'stockstash',
    'host': 'mongodb://admin:ZQTymqcbB6aZgtRY@ds149056.mlab.com:49056/stockstash'
}
app.config['SECRET_KEY'] = 'some_secret_here'

# email config
app.config['MAIL_SERVER'] = 'smtp-mail.outlook.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'stockstash@outlook.com'
app.config['MAIL_PASSWORD'] = 'Codingiscool'
mail = Mail(app)

# password hashing with bcrypt
bcrypt = Bcrypt(app)
# init the database
mongo = MongoEngine(app)
# login manager
login_manager = LoginManager(app)

from stockstash import routes