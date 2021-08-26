from flask import Blueprint, render_template

bp = Blueprint('order', __name__, url_prefix='/order')


@bp.route('/order/')
def _order():
    return render_template('order/order.html')