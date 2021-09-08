import sys

import requests
from flask import *
from flask_wtf import form
from sqlalchemy import distinct
from sqlalchemy.sql.functions import count
from sqlalchemy.util import counter

from pybo.views.auth_views import login_required
from pybo.models import Products, Categories, Users
from pybo.models import Cart
from pybo import db

bp = Blueprint('order', __name__, url_prefix='/order')


# 장바구니 목록
user = None
cart = None


@bp.route('/order/', methods=('GET', 'POST'))
@login_required
def _order(categories=None):
    if request.method == 'GET':
        global user
        global cart

        user = db.session.query(Users).filter_by(email=session.get('user_id')).first()

        productId = request.args.get('productId')
        name = request.args.get('name')
        qty = request.args.get('qty')

        products = db.session.query(Products).filter_by(productId=productId).first()
        categories = db.session.query(Categories).filter_by(name=name).first()

        cart = Cart(userId=user.userId, productId=productId, qty=qty, price=products.price, image=products.image, name=products.name)

        db.session.add(cart)
        db.session.commit()

        cart_list = db.session.query(Cart).filter_by(userId=user.userId).all()

        #cart_list = Cart.query.order_by(Cart.userId)

        total_price = int(cart.price * cart.qty)
        total_qty = cart.qty

        print("========111", total_qty, file=sys.stderr)
        print("========222", total_price, file=sys.stderr)
    else:
        flash('물건을 담는데 실패했습니다.')

    return render_template('order/order.html', form=form, products=products, user=user, cart=cart, cart_list=cart_list, categories=categories, total_price=total_price, total_qty=total_qty)


@bp.route('/payment/', methods=('GET', 'POST'))
@login_required
def payment():
    return render_template('order/payment.html')

