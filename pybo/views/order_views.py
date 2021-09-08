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
        price_total = db.session.query(Cart.price).order_by().all()  # 합계

        qty_total = db.session.query(Cart.price).filter(Cart.userId).count()  # 갯수 합계...인데 지금 추가한 항목이 동시에 올라감

        categories = db.session.query(Categories).filter_by(name=name).first()

        cart = Cart(userId=user.userId, productId=productId, qty=qty_total, price=products.price, image=products.image, name=products.name)

        db.session.add(cart)
        db.session.commit()

        # cart_list = db.session.query(Cart).filter_by(userId=user.userId).all()
        cart_list = Cart.query.order_by(Cart.userId).all()

        print("========111", cart, file=sys.stderr)
        print("========222", price_total, file=sys.stderr)
        print("========333", cart_list, file=sys.stderr)
    else:
        flash('물건을 담는데 실패했습니다.')

    return render_template('order/order.html', form=form, products=products, user=user, cart=cart, cart_list=cart_list, categories=categories, price_total=price_total, qty_total=qty_total)


@bp.route('/payment/', methods=('GET', 'POST'))
@login_required
def payment():
    if request.method == 'GET':
        global cart
        cart = db.session.query(Cart).first()
        db.session.delete(cart)
        db.session.commit()
        return redirect(url_for('order.payment'))
    else:
        flash('결제 중 오류가 발생했습니다.')

    return render_template('order/payment.html', cart=cart)

