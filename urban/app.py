from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///urban.db'
db= SQLAlchemy(app)
with app.app_context():
    db.create_all()


class Products(db.Model):
    id=db.Column(db.Integer(), primary_key=True)
    image= db.Column(db.String(length=30), nullable=False)
    name= db.Column(db.String(length=30), nullable=False)
    price= db.Column(db.Integer(), nullable=False)
    type= db.Column(db.String(length=30), nullable=False)
    
    

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/books')
def books():
    return render_template('books.html')

@app.route('/register')
def register():
    return render_template('register.html')


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