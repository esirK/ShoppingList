from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, length, Email, EqualTo, ValidationError

from wtforms.widgets import TextArea


def validate_names(form, field):
    if field.data.isdigit():
        raise ValidationError(u'Must Contain Letters')


class SignUpForm(Form):
    username = StringField("Username",
                           validators=[
                               DataRequired(),
                               length(min=4), validate_names
                           ])
    email = StringField("Email",
                        validators=[
                            DataRequired(),
                            Email(message="Invalid Email Address"),
                            length(min=4), validate_names])
    password = PasswordField('New Password',
                             validators=[DataRequired(),
                                         EqualTo('confirm',
                                                 message='Passwords must match'),
                                         length(min=4, max=80)])
    confirm = PasswordField('Confirm Password')


class LoginForm(Form):
    email = StringField("Email",
                        validators=[DataRequired(), length(min=4),
                                    validate_names])
    password = PasswordField('Password',
                             validators=[DataRequired(),
                                         length(min=4, max=80)])
    # remember = BooleanField('remember me')


class CreateShoppingList(Form):
    name = StringField("Name", validators=[DataRequired(), length(min=4),
                                           validate_names])
    body = StringField("Description", widget=TextArea(),
                       validators=[validate_names])


class AddItem(Form):
    item_name = StringField("Item Name",
                            validators=[DataRequired(), length(min=4),
                                        validate_names])
    category = StringField("Category('General' by Default)",
                           validators=[length(min=1), validate_names])
    item_price = StringField("Item Price",
                             validators=[DataRequired(),
                                         length(min=1)])
    item_quantity = StringField("Item Quantity", validators=[DataRequired(),
                                                             length(min=1)])
