from flask import Flask, render_template, url_for, flash
from flask_bootstrap import Bootstrap
from flask_login import LoginManager, login_user, current_user, logout_user
from werkzeug.utils import redirect

from app.Exceptions import ShoppingListAlreadyExist
from app.forms import SignUpForm, LoginForm, CreateShoppingList
from app.models.ShoppingList import ShoppingList
from app.models.account import Account
from app.models.user import User

app = Flask(__name__)
app.config['SECRET_KEY'] = "wireless"
account = Account()
login_manager = LoginManager()
bootstrap = Bootstrap(app)
login_manager.init_app(app)


@login_manager.user_loader
def load_user(email):
    """Load user object using supplied email"""
    return account.check_user(email)


@app.route("/", methods=['GET', 'POST'])
def index():
    """The root Of The App"""
    if current_user.is_authenticated:
        return render_template("userdashboard.html", name=current_user)
    else:
        return redirect("login")


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if current_user.is_authenticated:
        return redirect(url_for('index'))
    else:
        if form.validate_on_submit():
            user = account.check_user(form.email.data)
            if user:
                # A User Exist with that Email now check password
                if form.password.data == user.password:
                    login_user(user)
                    return redirect(url_for('index'))
                else:
                    flash("Invalid Username Or Password")
            else:
                flash("User Does Not Exist")

    return render_template("login.html", form=form)


@app.route("/signup", methods=['GET', 'POST'])
def signup():
    global account
    form = SignUpForm()

    if current_user.is_authenticated:
        return redirect(url_for('index'))
    else:
        if form.validate_on_submit():
            if account.check_user(form.email.data):
                # User Exist
                flash("User Already Exists")
            else:
                account.create_user(User(form.username.data, form.email.data, form.password.data))
                flash("User Created Successfully")
                return redirect("login")

    return render_template("signup.html", form=form)


@app.route("/logout")
def logout():
    """Logs Out A Currently LoggedIn User"""
    logout_user()
    flash("Logged Out Successfully")
    return redirect(url_for("index"))


@app.route("/create_shoppinglist", methods=['GET', 'POST'])
def create_shopping_lst():
    form = CreateShoppingList()
    if current_user.is_authenticated:
        if form.validate_on_submit():
            shopping_list = ShoppingList(form.name.data, form.body.data)

            try:
                current_user.create_shopping_lst(shopping_list)
            except ShoppingListAlreadyExist:
                flash("Shopping List " + form.name.data + " Already Exists")
                return render_template("create_shoppinglist.html", form=form)

            flash("Created Shopping List " + form.name.data + " You Now Have "
                  + str(len(current_user.shopping_lists)))

            return redirect(url_for('index'))

        return render_template("create_shoppinglist.html", form=form)
    else:
        return redirect(url_for('index'))


@app.route("/invalid")
def invalid():
    return render_template("invalid_creds.html")


if __name__ == '__main__':
    app.run(debug=True)
