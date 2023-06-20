from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///urban.db'
db= SQLAlchemy(app)


class Products(db.Model):
    id=db.Column(db.Integer(), primary_key=True)
    image= db.Column(db.String(length=30), nullable=False)
    name= db.Column(db.String(length=30), nullable=False)
    price= db.Column(db.Integer(), nullable=False)
    type= db.Column(db.String(length=30), nullable=False)

class Users(db.Model):
    id=db.Column(db.Integer(), primary_key=True)
    username= db.Column(db.String(length=30), nullable=False)
    first_name= db.Column(db.String(length=30), nullable=False)
    address= db.Column(db.String(length=30), nullable=False)
    email= db.Column(db.String(length=30), nullable=False)

    # def __init__(self,name,username,password):
    #     self.name = name
    #     self.username = username
    #     self.password = password

with app.app_context():
    db.create_all()
  
    

@app.route('/')
@app.route('/home')
def index():
    products = Products.query.all()
    return render_template('index.html',  products=products)


@app.route('/books')
def books():
    products = Products.query.all()
    products = Products.query.filter_by(type="Books")
    return render_template('books.html', products=products)

@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/login' , methods=['GET', 'POST'])
def login():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         user = Users.query.filter_by(username=username).first()

#         if user and check_password_hash(user.password, password):
#             # Authentication successful
#             session['user_id'] = user.id
#             return redirect(url_for('index'))
#         else:
#             # Authentication failed
#             error = 'Invalid username or password'
#             return render_template('login.html', error=error)

    return render_template('login.html')


@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

@app.route('/compelete')
def compelete():
    return render_template('compelete.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/electronics')
def electronics():
    products = Products.query.all()
    products = Products.query.filter_by(type="Electronics")
    return render_template('electronics.html', products=products)


@app.route('/fashion')
def fashion():
    products = Products.query.all()
    products = Products.query.filter_by(type="Fashion")
    return render_template('fashion.html', products=products)



@app.route('/furniture')
def furniture():
    products = Products.query.all()
    products = Products.query.filter_by(type="Furniture")
    return render_template('furniture.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)


