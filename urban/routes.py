from flask import render_template
from urban import app

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/books')
def books():
    return render_template('books.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/electronics')
def electronics():
    return render_template('electronics.html')


@app.route('/furniture')
def furniture():
    return render_template('furniture.html')


