from flask import Blueprint, url_for, render_template


bp = Blueprint('store', __name__, url_prefix='/store')


@bp.route('/store/')
def store():
    return render_template('store/store.html')