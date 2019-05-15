from datetime import datetime
from flask import Flask
from flask_mongoengine import MongoEngine
from flask_mongoengine.wtf import model_form
from wtforms import StringField, DateTimeField, PasswordField
from stockstash import app, mongo, login_manager
from flask_login import UserMixin

# reloading user from userid in session
@login_manager.user_loader
def load_user(user_id):
    return User.objects.get(pk=user_id)
class Portfolio(mongo.EmbeddedDocument):
    ticker = StringField()
    price = StringField()
    date = StringField()

class User(mongo.Document, UserMixin):
    #_id is our username
    _id = mongo.StringField(primary_key=True, required=True)
    password = mongo.StringField(requred=True)
    fname = mongo.StringField(required=True)
    lname = mongo.StringField(required=True)
    brokerage = mongo.StringField()
    portfolio = mongo.EmbeddedDocumentField(Portfolio)
    #account_created = mongo.DateTimeField(default=datetime.now)