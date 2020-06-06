# forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

class LoginForm(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')
    submit = SubmitField('Log In')

class RegistrationForm(FlaskForm):
    name = StringField('Name')
    email = StringField('Email')
    username = StringField('Username')
    password = PasswordField('Password')
    pass_confirm = PasswordField('Confirm Password')
    submit = SubmitField('Register!')

    def check_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Your email has been already registered')

    def check_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username is taken!')