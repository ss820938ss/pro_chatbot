import sys

import requests
from flask import *
from flask_wtf import form

from pybo.views.auth_views import login_required
from pybo.models import Products, Categories, Users
from pybo.models import Cart
from pybo import db

bp = Blueprint('order', __name__, url_prefix='/order')

products = None
user = None


@bp.route('/order/', methods=('GET', 'POST'))
@login_required
def _order(categories=None):
    if request.method == 'GET':
        global products
        global user

        user = db.session.query(Users).filter_by(email=session.get('user_id')).first()

        productId = request.args.get('productId')
        name = request.args.get('name')
        qty = request.args.get('qty')

        products = db.session.query(Products).filter_by(productId=user.userId).first()
        categories = db.session.query(Categories).filter_by(name=name).first()

        cart = Cart(userId=user.userId, productId=productId, qty=qty, price=products.price)
        db.session.add(cart)
        db.session.commit()

        cart_list = db.session.query(Cart).filter_by(userId=user.userId).first()


        print("========111", cart, file=sys.stderr)
        print("========111", products, file=sys.stderr)
    else:
        flash('물건을 담는데 실패했습니다.')

    return render_template('order/order.html', form=form, products=products, user=user, cart=cart_list, categories=categories)


@bp.route('/payment/', methods=('GET', 'POST'))
@login_required
def payment():
    global user

    user = db.session.query(Users).filter_by(email=session.get('user_id')).first()
    productId = request.args.get('productId')
    Qty = request.args.get('qty')

    cart = Cart(userId=user.userId, productId=productId, qty=Qty, price=products.price)
    db.session.remove(cart)
    db.session.commit()

    return render_template('order/payment.html', user=user)
