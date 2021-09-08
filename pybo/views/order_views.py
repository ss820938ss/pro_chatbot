import sys
from turtle import pd

import requests
from flask import *
from flask_wtf import form

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
        price_total1 = db.session.query(Cart.price).order_by(cart).all()  # 가격 합계 구하기, 현재는 list 로만 출력

        categories = db.session.query(Categories).filter_by(name=name).first()

        cart = Cart(userId=user.userId, productId=productId, qty=qty, price=products.price, image=products.image, name=products.name)

        db.session.add(cart)
        db.session.commit()

        cart_list = db.session.query(Cart).filter_by(userId=user.userId).all()

        #cart_list = Cart.query.order_by(Cart.userId)

        print("========111", price_total1, file=sys.stderr)
    else:
        flash('물건을 담는데 실패했습니다.')

    return render_template('order/order.html', form=form, products=products, user=user, cart=cart, cart_list=cart_list, categories=categories, price_total=price_total1)


@bp.route('/payment/', methods=('GET', 'POST'))
@login_required
def payment():
    return render_template('order/payment.html')

