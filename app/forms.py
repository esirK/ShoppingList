from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired, length, Email, EqualTo


class SignUpForm(Form):
    username = StringField("Username", validators=[DataRequired(), length(min=4)])
    email = StringField("Email", validators=[DataRequired(), Email(message="Invalid Email Address"), length(min=4)])
    password = PasswordField('New Password', validators=[DataRequired(), EqualTo('confirm', message='Passwords must '
                                                                                                    'match')])
    confirm = PasswordField('Confirm Password')


class LoginForm(Form):
    email = StringField("Email", validators=[DataRequired(), length(min=4)])
    password = PasswordField('Password', validators=[DataRequired(), length(min=4, max=80)])
    # remember = BooleanField('remember me')