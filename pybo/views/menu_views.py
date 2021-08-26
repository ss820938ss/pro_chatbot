from flask import Blueprint, render_template

bp = Blueprint('menu', __name__, url_prefix='/menu')


@bp.route('/list/')
def _list():
    return render_template('menu/menu_list.html')


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
