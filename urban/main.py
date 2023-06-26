from flask import Blueprint
from .models import Products, CartItems, Coupons
from flask import render_template,url_for, request, redirect
from . import db
from flask_login import login_required, current_user

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/home')
def index():
    # from . import app

    # with app.app_context():
    #     db.create_all()
    # new_user = Products(image='item.jpg', name='Item 3', price=100, type='electronics')
    # db.session.add(new_user)
    # db.session.commit()
        # new_user = Coupons(code='diwali20', amount='110')
        # db.session.add(new_user)
        # db.session.commit()a
    products = Products.query.all()
    return render_template('index.html',  products=products)


@main.route('/category/<slug>')
def books(slug):
    print(slug)
    products = Products.query.filter_by(type=slug).all()
    print(products)
    return render_template('books.html', products=products)


@main.route('/contact')
def contact():
    return render_template('contact.html')

@main.route('/sell')
def sell():
    return render_template('sell.html')



@main.route('/profile')
@login_required
def profile():
    
    return render_template('profile.html')

@main.route('/checkout')
def checkout():
    return render_template('checkout.html')

@main.route('/compelete')
def compelete():
    return render_template('compelete.html')

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/cart', methods=['POST','GET'])
@login_required
def cart():
    user_id = current_user.id
    cart_items = CartItems.query.filter_by(user_id=user_id).all()
    subtotal = 0
    for i in cart_items:
        subtotal += i.product.price * i.quantity
    tax = 0.18 * subtotal
    if(request.method == 'POST'):
        code = request.form.get('coupon_code')
        coupon = Coupons.query.filter_by(code=code, status='active').first()
        if coupon:
            print('coupon code: ', code, ' Amount: ',coupon.amount)
            subtotal -= coupon.amount
            tax = 0.18 * subtotal
        print('subtotal: ', subtotal, ' tax: ',tax)
        if(subtotal<0):
            subtotal = 0
            tax = 0
        return {'subtotal':subtotal,'tax':tax}
    return render_template('cart.html', cart_items=cart_items, subtotal=subtotal, tax=tax)


@main.route('/add_to_cart', methods=['POST'])
@login_required
def add_to_cart():
    prod_id = request.form.get('prod_id')
    quantity = request.form.get('quantity')

    existing_product = CartItems.query.filter_by(product_id=prod_id, user_id=current_user.id).first()
    if existing_product:
        existing_product.quantity += int(quantity)
        db.session.commit()
    else:
        cart_item = CartItems(product_id=prod_id,quantity=quantity,user_id=current_user.id)
        db.session.add(cart_item)
        db.session.commit()
    
    return redirect(url_for('main.cart'))

@main.route('/cart_action', methods=['POST'])
@login_required
def cart_action():
    if(request.form.get('delete_item')):
        delete_item_id = request.form.get('prod_id')
        print(' prod id: ',delete_item_id)
        delete_item = CartItems.query.filter_by(product_id=delete_item_id,user_id=current_user.id).first()
        db.session.delete(delete_item)
        db.session.commit()
    elif(request.form.get('quantity')):
        quantity = request.form.get('quantity')
        prod_id = request.form.get('prod_id')
        print('quantity: ',quantity, ' prod id: ',prod_id)
        existing_product = CartItems.query.filter_by(product_id=prod_id, user_id=current_user.id).first()
        print(existing_product)
        if(int(quantity)==0 and existing_product):
            print('some')
            db.session.delete(existing_product)
            db.session.commit()
            return 'Updated'
        if existing_product:
            existing_product.quantity = int(quantity)
            db.session.commit() 
    return 'Updated'

@main.route('/checkout', methods=['POST'])
@login_required
def checkout_post():
    CartItems.query.filter_by(user_id=current_user.id).delete()
    db.session.commit()
    return redirect(url_for('main.index'))