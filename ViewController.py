"""
@ Author:  Javier Cienfuegos
@ Title:    ViewController.py
@ Description: Routes the url to multiple templates and basically
            controls the flow of web pages.
"""

from datetime import date
from flask import *
from flask_login import LoginManager, login_user, login_required, logout_user
from model import SQLDatabase, EmailLogManager, mongoDatabase
from user import User, DevelopmentUser
from flask_mail import *
import logging, xmltodict, json


app = Flask(__name__)
app.secret_key = "ABAAMAMA"

# Email Management
app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME = 'cienfuegosjdevelop@gmail.com',
    MAIL_PASSWORD = 'Promagic1'
    )


@app.route("/", methods=["GET", "POST"])
def login():

    return render_template("login.html", title="Home | Organizer", active="home", loginFailed=True)


@app.route("/about", methods=["GET"])
def about():
    return render_template("about.html", title="About | Organizer")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "GET":
        return render_template("contact.html", title="Contact | Organizer")
    else:
        # Do any email contact things here
        pass

if __name__ == '__main__':
    app.run(debug=True,port=7171)