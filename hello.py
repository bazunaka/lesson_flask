from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from flask_sqlalchemy import SQLAlchemy
import os

basedir = os.path.abspath(os.path.dirname(__file__))

class NameForm(Form):
   name = StringField('Ваше имя?', validators=[Required()])
   submit = SubmitField('Подтвердить')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'flask.db')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

bootstrap = Bootstrap(app)
db = SQLAlchemy(app)

class Role (db.Model):
   __tablename__ = 'roles'
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(64), unique=True)

   def __repr__ (self):
      return '<Role %r>' % self.name

class User (db.Model):
   __tablename__ = 'users'
   id = db.Column(db.Integer, primary_key=True)
   username = db.Column(db.String(64), unique=True, index=True)

   def __repr__ (self):
      return '<User %r>' % self.username

@app.route('/', methods=['GET', 'POST'])
def index():
   form = NameForm()
   if form.validate_on_submit():
      old_name = session.get('name')
      if old_name is not None and old_name != form.name.data:
         flash("Проверьте правильность ввода имени!")
      session['name'] = form.name.data
      return redirect(url_for('index'))
   return render_template('index.html', form = form, name = session.get('name'))

@app.route('/user/<name>')
def user(name):
   return render_template('user.html', name = name)

@app.errorhandler(404)
def page_not_found(e):
   return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
   return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug = True)