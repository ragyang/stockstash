from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from stockstash.models import User
from stockstash.api.alphavantage import is_valid_ticker

# registration form
class RegistrationForm(FlaskForm):
    username = StringField('Email',
                           validators=[DataRequired(),Length(min=2, max=20), Email()])
    fname = StringField('First Name',
                            validators=[DataRequired(), Length(min=1, max=100)])
    lname = StringField('Last Name',
                            validators=[DataRequired(), Length(min=1, max=100)])
    password = PasswordField('Password',
                             validators=[DataRequired(), Length(min=6, max=20)])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    brokerage = StringField('Brokerage')
    submit = SubmitField('Sign Up')

    # validates the username is unique
    def validate_username(self, username):
        try:
            user = User.objects.get(username=username.data)
        except User.DoesNotExist:
            user = None
        if user:
            raise ValidationError('Username taken! Please try another...')

# account form
class AccountForm(FlaskForm):
    username = StringField('Email',
                           validators=[DataRequired(),Length(min=2, max=20), Email()])
    fname = StringField('First Name', validators=[Length(min=1, max=100)])
    lname = StringField('Last Name', validators=[Length(min=1, max=100)])
    brokerage = StringField('Brokerage')
    submit = SubmitField('Update')

    # validates the username is unique
    def validate_username(self, username):
        try:
            user = User.objects.get(username=username.data)
            print(user.username)
        except User.DoesNotExist:
            user = None
        if user and (user.username != username.data):
            raise ValidationError('Username taken! Please try another...')

# login form
class LoginForm(FlaskForm):
    username = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

    # validates the username is unique
    def validate_username(self, username):
        try:
            user = User.objects.get(username=username.data)
        except User.DoesNotExist:
            user = None
            raise ValidationError('Email does not exist')

# ticker form
class AddStockForm(FlaskForm):
    ticker = StringField('Ticker',
                           validators=[DataRequired()])
    price = StringField('Price Bought',
                            validators=[DataRequired(), Length(min=1, max=100)])
    #date = DateField('Date Bought', format='%Y-%m-%d')
    submit = SubmitField('Add Stock')

    def validate_ticker(self, ticker):
        if not is_valid_ticker(ticker.data):
            raise ValidationError('Error! Not a valid ticker.')

# ticker form
class AddStockFormWatchlist(FlaskForm):
    ticker = StringField('Ticker',
                           validators=[DataRequired()])
    lowprice = StringField('Low Price',
                            validators=[DataRequired(), Length(min=1, max=100)])
    highprice = StringField('High Price',
                            validators=[DataRequired(), Length(min=1, max=100)])
    submit = SubmitField('Add Stock')

    def validate_ticker(self, ticker):
        if not is_valid_ticker(ticker.data):
            raise ValidationError('Error! Not a valid ticker.')