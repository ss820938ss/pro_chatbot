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
def _order(categories=None, cart=None):
    if request.method == 'GET':
        global products
        global user

        user = db.session.query(Users).filter_by(email=session.get('user_id')).first()

        productId = request.args.get('productId')
        name = request.args.get('name')

        products = db.session.query(Products).filter_by(productId=productId).first()
        categories = db.session.query(Categories).filter_by(name=name).first()

        # cart = db.session.query(Cart).filter_by(productId=cart.productId).first()

        print("========111", user, file=sys.stderr)
        print("========111", products, file=sys.stderr)
        # db.session.add(cart)
        # db.session.commit()
    else:
        flash('물건을 담는데 실패했습니다.')

    return render_template('order/order.html', form=form, user=user, products=products, categories=categories)


@bp.route('/payment/', methods=('GET', 'POST'))
@login_required
def payment():
    return render_template('order/payment.html')