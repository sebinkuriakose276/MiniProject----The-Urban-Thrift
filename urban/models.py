from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from urban import db, login_manager

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

class Products(db.Model):
    id=db.Column(db.Integer(), primary_key=True)
    image= db.Column(db.String(length=30), nullable=False)
    name= db.Column(db.String(length=30), nullable=False)
    price= db.Column(db.Integer(), nullable=False)
    type= db.Column(db.String(length=30), nullable=False)

class Users(UserMixin, db.Model):
    id=db.Column(db.Integer(), primary_key=True)
    username= db.Column(db.String(length=30), nullable=False)
    phone= db.Column(db.String(length=30), nullable=False)
    email= db.Column(db.String(length=30), nullable=False)
    password = db.Column(db.String(100))

class CartItems(db.Model):
    id=db.Column(db.Integer(), primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    product = db.relationship("Products", backref='product')
    quantity = db.Column(db.Integer())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

class Coupons(db.Model):
    id=db.Column(db.Integer(), primary_key=True)
    code = db.Column(db.String(length=10))
    amount = db.Column(db.Integer())
    status = db.Column(db.String, default='active')


    