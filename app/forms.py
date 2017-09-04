from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, length, Email, EqualTo
from wtforms.widgets import TextArea


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


class CreateShoppingList(Form):
    name = StringField("Name", validators=[DataRequired(), length(min=4)])
    # description = StringField("Description", validators=[DataRequired(), length(min=4)])
    body = StringField("Description", widget=TextArea())


class AddItem(Form):
    item_name = StringField("Item Name", validators=[DataRequired(), length(min=4)])
    category = StringField("Category('General' by Default)", validators=[length(min=1)])
    item_price = StringField("Item Price", validators=[DataRequired(), length(min=1)])
    item_quantity = StringField("Item Quantity", validators=[DataRequired(), length(min=1)])

