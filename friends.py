from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('homepage.html')

@app.route('/login')
def login():
    return 'login page'

@app.route('/register')
def register():
    return 'register page'

@app.route('/user/<username>')
def user(username):
    return 'user  '+username+'  page'



if __name__ == '__main__':
    app.run()
