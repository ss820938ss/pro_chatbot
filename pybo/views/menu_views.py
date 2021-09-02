from flask import *
from sqlalchemy import func

from pybo.models import Products, Categories
from pybo import db

bp = Blueprint('menu', __name__, url_prefix='/menu')


products = None


@bp.route('/list/', methods=('GET', 'POST'))
def _list():
    if request.method == 'GET':
        global products
        products = db.session.query(Products).filter_by(productId=session.get('productsId')).first()

    return render_template('menu/menu_list.html', products=products)


@bp.route('/coffee/')
def _coffee():
    return render_template('menu/menu_coffee.html')


@bp.route('/juice/')
def _juice():
    return render_template('menu/menu_juice.html')


@bp.route('/tea/')
def _tea():
    return render_template('menu/menu_tea.html')


@bp.route('/cake/')
def _cake():
    return render_template('menu/menu_cake.html')


@bp.route('/cookie/')
def _cookie():
    return render_template('menu/menu_cookie.html')


@bp.route('/menu_detail/', methods=('GET', 'POST'))
def menu_detail(categories=None):
    if request.method == 'GET':
        global products
        productId = request.args.get('productId')
        name = request.args.get('name')
        products = db.session.query(Products).filter_by(productId=productId).first()
        categories = db.session.query(Categories).filter_by(name=name).first()
    return render_template('menu/menu_detail.html', products=products, categories=categories)
