import sys

import requests
from flask import *
from flask_wtf import form

from pybo.views.auth_views import login_required
from pybo.models import Products, Categories, Users
from pybo.models import Cart
from pybo import db

bp = Blueprint('order', __name__, url_prefix='/order')


# @bp.route('/order/')
# def _order():
#     return render_template('order/order.html')


products = None


@bp.route('/order/', methods=('GET', 'POST'))
@login_required
def _order():
    if request.method == 'GET':
        global products
        productId = request.args.get('productId')
        name = request.args.get('name')
        email = session.get('user_id')

        products = db.session.query(Products).filter_by(productId=productId).first()
        categories = db.session.query(Categories).filter_by(name=name).first()

        cart = Cart(
            name=form.name.data)
        # products.price = form.price.data
        # products.image = form.image.data
        # products.categoryId = form.categoryId.data

        print("========111", products.name, file=sys.stderr)

        db.session.add(cart)
        db.session.commit()
    else:
        flash('물건을 담는데 실패했습니다.')

    return render_template('order/order.html', form=form, products=products, categories=categories, user=email)
