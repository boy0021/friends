from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('homepage.html')

@app.route('/login')
def login():
    return render_template('loginpage.html')

@app.route('/register')
def register():
    return render_template('regiestepage.html')


@app.route('/user/<username>')
def user(username):
    # return 'user  '+username+'  page'
    return render_template('userpage.html')


if __name__ == '__main__':
    app.run()
