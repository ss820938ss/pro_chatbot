import sys
from turtle import pd
import re

import requests
from flask import *
from flask_wtf import form
from sqlalchemy.sql import label
from sqlalchemy import func

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
def _order(categories=None, price_total=None):
    if request.method == 'GET':
        global user
        global cart

        user = db.session.query(Users).filter_by(email=session.get('user_id')).first()

        productId = request.args.get('productId')
        name = request.args.get('name')
        price = request.args.get('price')
        image = request.args.get('image')
        qty = request.args.get('qty')

        products = db.session.query(Products).filter_by(productId=productId).first()
        categories = db.session.query(Categories).filter_by(name=name).first()

        cart = Cart(userId=user.userId, productId=productId, qty=qty, price=price, image=image, name=name)
        db.session.add(cart)
        db.session.commit()

        # print("========1", type(price_total), file=sys.stderr)
        # print("========2", price_total, file=sys.stderr)
        cart_list = Cart.query.order_by(Cart.userId).all()

        price_total = db.session.query(Cart.price, label('price', func.sum(Cart.price))).first()  # 합계

        print("1", price_total[0])
        print("2", price_total[1])

    else:
        flash('물건을 담는데 실패했습니다.')

    return render_template('order/order.html', form=form, products=products, user=user, cart=cart, cart_list=cart_list,
                           categories=categories, price_total=price_total[1])


# # 갯수수정
# @bp.route('/cart_update/', methods=('GET', 'POST'))
# @login_required
# def cart_update():
#     form = cart_update(request.form)
#     if request.method == 'POST':
#         global cart
#
#         user = db.session.query(Users).filter_by(email=session.get('user_id')).first()
#
#         productId = request.args.get('productId')
#         name = request.args.get('name')
#         price = request.args.get('price')
#         image = request.args.get('image')
#         qty = request.args.get('qty')
#
#         products = db.session.query(Products).filter_by(productId=productId).first()
#         categories = db.session.query(Categories).filter_by(name=name).first()
#
#         price_total = db.session.query(Cart.price).order_by().all()  # 합계 all 쓰면 list 로만 나오는데 더하기가 안됨
#
#         print("========1", type(price_total), file=sys.stderr)
#         print("========2", price_total, file=sys.stderr)
#         qty_total = db.session.query(Cart.qty).filter(Cart.userId).count()  # 갯수...인데 지금 추가한 항목이 동시에 올라감
#
#         cart = Cart(userId=user.userId, productId=productId, qty=qty_total, price=price, image=image, name=name)
#
#         cart.qty = form.qty.data
#         db.session.commit()
#     else:
#         flash('삭제 중 오류가 발생했습니다.')
#
#     return render_template('order/cart_update.html', form=form, products=products, user=user, cart=cart, cart_list=cart_list, categories=categories, price_total=price_total, qty_total=qty_total)


# 장바구니 비우기
@bp.route('/cart_delete/', methods=('GET', 'POST'))
@login_required
def cart_delete():
    if request.method == 'GET':
        global cart

        db.session.query(Cart).filter(Cart.userId > 0).delete()
        db.session.commit()
    else:
        flash('삭제 중 오류가 발생했습니다.')

    return render_template('order/cart_delete.html', cart=cart)


# 결제하기
@bp.route('/payment/', methods=('GET', 'POST'))
@login_required
def payment():
    if request.method == 'GET':
        global cart

        db.session.query(Cart).filter(Cart.userId > 0).delete()
        db.session.commit()
    else:
        flash('결제 중 오류가 발생했습니다.')

    return render_template('order/payment.html', cart=cart)
