from flask import Flask, render_template, url_for, request
from flask_bootstrap import Bootstrap
from werkzeug.utils import redirect

from app.account import Account
from app.user import User

app = Flask(__name__)
app.config['SECRET_KEY'] = "wireless"
account = Account()
bootstrap = Bootstrap(app)


@app.route("/")
def index():
    return "Home Page"


@app.route("/login", methods=['GET', 'POST'])
def login():
    print(request.method)
    if request.method == 'POST':
        print(len(account.users))
        user = account.check_user(request.form['email'])
        if user:
            print(user.name + " Has Password " + request.form['psw'])
            # check password
            if request.form['psw'] == user.password:
                print("OK")
                return redirect(url_for('home'))
            else:
                print("Not OK")
                return redirect(url_for('invalid'))
                # flash("Invalid Username Or Password")
        else:
            return "User Doesn't Exist"

    return render_template("login.html")


@app.route("/signup", methods=['GET', 'POST'])
def signup():
    global account
    if request.method == 'POST':
        if account.check_user(request.form['email']):
            # User Exist
            return "User Already Exists"
        else:
            account.create_user(User(request.form['username'], request.form['email'], request.form['psw']))
            print(len(account.users))
            return redirect("login")

    return render_template("signup.html")


@app.route("/home", methods=['GET', 'POST'])
def home():
    return render_template("userdashboard.html")


@app.route("/invalid", methods=['GET', 'POST'])
def invalid():
    return render_template("invalid_creds.html")


if __name__ == '__main__':
    app.run(debug=True)
