from flask import Flask
from flask import render_template
from flask import request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Table, Column, Integer, String, Date, Float

import config

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username
# DB class


@app.route('/')
def home():
    return render_template('homepage.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method=='GET':
        return render_template('loginpage.html')
    else:
        return "login page POST request"


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('regiestepage.html')
    else:
        return "login page POST request"



@app.route('/user/<username>', methods=['GET', 'POST'])
def user(username):
    if request.method == 'GET':
        return render_template('userpage.html')
    else:
        return "login page POST request"
    # userpage



if __name__ == '__main__':
    app.run()
