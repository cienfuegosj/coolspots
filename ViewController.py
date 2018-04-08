"""
@ Author:  Javier Cienfuegos
@ Title:    ViewController.py
@ Description: Routes the url to multiple templates and basically
            controls the flow of web pages.
"""

from datetime import date
from flask import *
from flask_pymongo import PyMongo
from flask_login import LoginManager, login_user, login_required, logout_user
from model import SQLDatabase, EmailLogManager, mongoDatabase
from user import User, DevelopmentUser
from flask_mail import *
import logging, xmltodict, json


app = Flask(__name__)
app.secret_key = "ABAAMAMA"
app.config['MONGO_DBNAME'] = 'coolspots'
app.config['MONGO_URI'] = "mongodb://admin:admin@ds237979.mlab.com:37979/coolspots"
mongo = PyMongo(app)
login_manager = LoginManager()
login_manager.init_app(app)


@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html", title="Home | coolspots", active="home", loginFailed=True)
    else:
        pass

@login_required
@app.route("/home", methods=["GET"])
def home():
    return render_template("home.html", title="Home | coolspots", current_type="Restaurants")


@app.route("/about", methods=["GET"])
def about():
    return render_template("about.html", title="About | coolspots")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "GET":
        return render_template("contact.html", title="Contact | coolspots")
    else:
        # Do any email contact things here
        pass


@login_required
@app.route("/home/<id>/<type>/favorites")
def favorite_search(id, type):
    # Query the database for user's top five based on type
    pass

@login_required
@app.route("/home/<id>/recents")
def recent_search(id, type):
    # Query the database for user's recent five based on type
    pass

@login_required
@app.route("/home/<id>/current_polls")
def current_polls(id, type):
    # Query the database for user's current_polls
    pass

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    redirect(url_for(login))


if __name__ == '__main__':
    app.run(debug=True,port=7171)