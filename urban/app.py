from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///urban.db'
db= SQLAlchemy(app)
# db.create_all()

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


@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

@app.route('/compelete')
def compelete():
    return render_template('compelete.html')


@app.route('/electronics')
def electronics():
    return render_template('electronics.html')


@app.route('/fashion')
def fashion():
    return render_template('fashion.html')



@app.route('/furniture')
def furniture():
    return render_template('furniture.html')

if __name__ == '__main__':
    app.run(debug=True)