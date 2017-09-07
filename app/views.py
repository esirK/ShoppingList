import os

from flask import Flask, render_template, url_for, flash
from flask_bootstrap import Bootstrap
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
from werkzeug.utils import redirect

from app.Exceptions import ShoppingListAlreadyExist, ItemAlreadyExist, ShoppingListDoesNotExist, ItemDoesNotExist
from app.forms import SignUpForm, LoginForm, CreateShoppingList, AddItem
from app.models.ShoppingList import ShoppingList
from app.models.accounts import Accounts
from app.models.item import Item
from app.models.user import User

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
accounts = Accounts()
login_manager = LoginManager()
bootstrap = Bootstrap(app)
login_manager.login_view = "/login"
login_manager.login_message_category = "info"
login_manager.init_app(app)


@login_manager.user_loader
def load_user(email):
    """ Load user object using supplied email"""
    return accounts.check_user(email)


@app.route("/", methods=['GET', 'POST'])
def index():
    """The root Of The App"""
    if current_user.is_authenticated:
        # User authenticated
        return render_template("userdashboard.html")
    else:
        return redirect(url_for("login"))


@app.route("/login", methods=['GET', 'POST'])
def login():
    """
    Login endpoint for registered users
    :return: 
    """
    form = LoginForm()

    if current_user.is_authenticated:
        return redirect(url_for('index'))
    else:
        if form.validate_on_submit():
            user = accounts.check_user(form.email.data)
            if user:
                # A User Exist with that Email now check password
                if user.verify_password(form.password.data):
                    login_user(user)
                    return redirect(url_for('index'))
                else:
                    flash("Invalid Username Or Password", 'danger')
            else:
                flash("User Does Not Exist", 'danger')

    return render_template("login.html", form=form)


@app.route("/signup", methods=['GET', 'POST'])
def signup():
    global accounts
    form = SignUpForm()

    if current_user.is_authenticated:
        return redirect(url_for('index'))
    else:
        if form.validate_on_submit():
            if accounts.check_user(form.email.data):
                # User Exist
                flash("User Already Exists", "info")
            else:
                accounts.add_user(
                    User(form.username.data, form.email.data, form.password.data))
                flash("User Created Successfully", "success")
                return redirect("login")

    return render_template("signup.html", form=form)


@app.route("/logout")
@login_required
def logout():
    """Logs Out A Currently LoggedIn User"""
    logout_user()
    flash("Logged Out Successfully", "success")
    return redirect(url_for("login"))


@app.route("/create_shoppinglist", methods=['GET', 'POST'])
@login_required
def create_shopping_lst():
    form = CreateShoppingList()
    if form.validate_on_submit():
        shopping_list = ShoppingList(form.name.data, form.body.data)

        try:
            current_user.create_shopping_lst(shopping_list)
        except ShoppingListAlreadyExist:
            flash("Shopping List " + form.name.data + " Already Exists", "warning")
            return render_template("create_shoppinglist.html",
                                   form=form)

        flash("Created Shopping List " + form.name.data + " You Now Have "
              + str(len(current_user.shopping_lists)) + " Shopping Lists", "info")

        return redirect(url_for('index'))

    return render_template("create_shoppinglist.html", form=form)


@app.route("/update_shoppinglist/<shopping_list_name>/<description>/",
           methods=['GET', 'POST'])
@login_required
def update_shoppinglist(shopping_list_name, description):
    form = CreateShoppingList()
    shopping_list_to_update = ShoppingList(name=shopping_list_name,
                                           description=description)

    if form.validate_on_submit():
        shopping_list = ShoppingList(form.name.data, form.body.data)
        try:
            current_user.update_shopping_list(shopping_list)
        except ShoppingListDoesNotExist:
            flash("Shopping List " + shopping_list_name + " Does not Exist ", "info")
        return redirect(url_for('index'))
    else:
        return render_template("update_shoppinglist.html",
                               form=form,
                               shopping_list=shopping_list_to_update,
                               shopping_list_name=shopping_list_name)


@app.route("/add_item/<shopping_list_name>", methods=['GET', 'POST'])
@login_required
def add_item(shopping_list_name):
    form = AddItem()
    if form.validate_on_submit():
        """ 
        Instantiate an Item Object from the 
        form data submitted by the current_user
        """
        item = Item(form.item_name.data, form.item_price.data,
                    form.item_quantity.data, form.category.data)
        try:
            shopping_list = current_user.get_shopping_lst(shopping_list_name)
            shopping_list.add_item(item)
            current_user.update_shopping_list(shopping_list)
            flash(" " + item.name +
                  " Successfully Added into Shopping List " +
                  shopping_list_name, "info")

            return redirect(url_for('index'))

        except ItemAlreadyExist:
            flash(item.name + " Already Exists Try updating it instead", "info")
            return redirect(url_for('index'))
    else:
        return render_template("add_item.html", form=form,
                               shopping_list_name=shopping_list_name)


@app.route("/update_item/<shopping_list_name>/<name>/<price>/<quantity>/<category>",
           methods=['GET', 'POST'])
@login_required
def update_item(shopping_list_name, name, price, quantity, category):
    form = AddItem()
    """ 
    Item that we wish to update is created from parameters passed in the URL 
    """
    item_to_update = Item(name=name, price=price, category=category,
                          quantity=quantity)

    item = Item(name=form.item_name.data, price=form.item_price.data,
                quantity=form.item_quantity.data,
                category=form.category.data)

    if form.validate_on_submit():
        try:
            shopping_list = current_user.get_shopping_lst(shopping_list_name)
            shopping_list.update_item(item)
            flash(item.name + "Has been Successfully Updated", "success")
        except ShoppingListDoesNotExist:
            flash("No Shopping List With name " + shopping_list_name +
                  " Try Adding it instead", "warning")
        except ItemDoesNotExist:
            flash("Sorry Item " + item.name +
                  " Cannot Be Updated. Make sure you have such item first",
                  "warning")
        return redirect(url_for('index'))
    else:
        return render_template("update_item.html", form=form,
                               shopping_list_name=shopping_list_name,
                               item=item_to_update)


@app.route("/delete_shopping_list/<shopping_list_name>", methods=['GET', 'POST'])
@login_required
def delete_shopping_list(shopping_list_name):
    try:
        """
        Uses delete_shopping_list from user class to delete a shopping list
        """
        current_user.delete_shopping_list(shopping_list_name)
        flash(shopping_list_name + " Deleted Successfully ", "success")
    except ShoppingListDoesNotExist:
        flash(shopping_list_name + " Does not Exist ", "warning")
    return redirect(url_for('index'))


@app.route("/delete_item/<shopping_list_name>/<name>/<price>/<quantity>/"
           "<category>", methods=['GET', 'POST'])
@login_required
def delete_item(shopping_list_name, name, price, quantity, category):
    """
    Deletes an item from a shopping_list. Creates a the item to delete from the 
    url supplied parameters 
    """
    item = Item(name=name, price=price, category=category, quantity=quantity)
    if current_user.is_authenticated:
        try:
            current_user.get_shopping_lst(shopping_list_name).remove_item(item)
            flash(item.name + " Deleted Successfully ", "success")
        except ShoppingListDoesNotExist:
            flash("Shopping List " + shopping_list_name + " Does Not Exist", "warning")
        except ItemDoesNotExist:
            flash("The Item " + item.name + "That You Wish To Delete Does Not Exist",
                  "warning")

        return redirect(url_for('index'))


@app.route("/invalid")
def invalid():
    return render_template("invalid_creds.html")


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
