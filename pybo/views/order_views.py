from flask import Blueprint, render_template, request, jsonify

from pybo.models import Order

bp = Blueprint('order', __name__, url_prefix='/order')


@bp.route('/order/')
def _order():
    return render_template('order/order.html')


@bp.route('/order/add', methods=['POST'])
def add_to_cart():
    cart = Order.add(product=request.form['product'], quantity=int(request.form['quantity']))
    return jsonify(cart)


@bp.route("order/order")
def view_cart():
    cart = Order.get()
    return render_template("order/order.html", cart=cart)