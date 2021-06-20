from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from flask_sqlalchemy import SQLAlchemy
from flask_script import Shell, Manager
from flask_migrate import Migrate
from flask_mail import Mail
import os

basedir = os.path.abspath(os.path.dirname(__file__))


app = Flask(__name__)


bootstrap = Bootstrap(app)


@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/user/<name>")
def user():
    return render_template("user.html")


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html"), 500


if __name__ == "__main__":
    app.run(debug=True)
