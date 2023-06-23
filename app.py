from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///urban.db'
db= SQLAlchemy(app)


class User(db.Model):
   # __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(length=50),unique=True,nullable=False)
    email_address = db.Column(db.String(length=50),unique=True,nullable=False)
    password_hash= db.Column(db.String(length=60),nullable=False)
    product_type = db.Column(db.String(50))


class Product(db.Model):
   # __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=50),unique=True,nullable=False)
    description = db.Column(db.String(length=100))
    image_url = db.Column(db.String(length=200))
    product_type = db.Column(db.String(length=50))

if __name__=='__main__':
    db.create_all()
    app.run(host='0.0.0.0',debug=True)