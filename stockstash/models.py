from datetime import datetime
from flask import Flask
from flask_mongoengine import MongoEngine
from flask_mongoengine.wtf import model_form
from wtforms import StringField, DateTimeField, PasswordField
from stockstash import app, mongo, login_manager
from flask_login import UserMixin
from bson.objectid import ObjectId
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
# reloading user from userid in session


@login_manager.user_loader
def load_user(user_id):
    return User.objects.get(pk=user_id)

class Portfolio(mongo.EmbeddedDocument):
    ticker = mongo.StringField()
    price = mongo.StringField()
    date = mongo.StringField()
    quantity = mongo.IntField()

class Watchlist(mongo.EmbeddedDocument):
    ticker = mongo.StringField()
    lowprice = mongo.StringField()
    highprice = mongo.StringField()

class User(mongo.Document, UserMixin):
    username = mongo.StringField(required=True)
    password = mongo.StringField(requred=True)
    fname = mongo.StringField(required=True)
    lname = mongo.StringField(required=True)
    brokerage = mongo.StringField()
    admin = mongo.BooleanField(default=False)
    portfolio = mongo.EmbeddedDocumentListField(Portfolio)
    watchlist = mongo.EmbeddedDocumentListField(Watchlist)

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'username': self.username}).decode('utf-8')
    
    @staticmethod
    def verify_reset_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            u = s.loads(token)['username']
        except:
            return None
        return User.objects.get(username=u)
