from datetime import datetime
from flask import Flask
from flask_mongoengine import MongoEngine
from wtforms import StringField, DateTimeField, PasswordField
from stockstash import app, mongo, login_manager
from flask_login import UserMixin

# reloading user from userid in session
@login_manager.user_loader
def load_user(user_id):
    return User.objects.get(pk=user_id)

class User(mongo.Document, UserMixin):
    #_id is our username
    _id = mongo.StringField(primary_key=True, required=True)
    password = mongo.StringField(requred=True)
    fname = mongo.StringField(required=True)
    lname = mongo.StringField(required=True)
    brokerage = mongo.StringField()
    #account_created = mongo.DateTimeField(default=datetime.now)