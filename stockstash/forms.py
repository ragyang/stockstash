from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from stockstash.models import User

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
            user = User.objects.get(pk=username.data)
        except User.DoesNotExist:
            user = None
        if user:
            raise ValidationError('Username taken! Please try another...')

# login form
class LoginForm(FlaskForm):
    username = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')