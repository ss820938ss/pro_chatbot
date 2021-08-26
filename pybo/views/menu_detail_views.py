from flask import Blueprint, render_template

bp = Blueprint('menu_detail', __name__, url_prefix='/menu_detail')


@bp.route('/coffee01/')
def _coffee01():
    return render_template('menu_detail/coffee01.html')


@bp.route('/coffee02/')
def _coffee02():
    return render_template('menu_detail/coffee02.html')


@bp.route('/coffee03/')
def _coffee03():
    return render_template('menu_detail/coffee03.html')


@bp.route('/coffee04/')
def _coffee04():
    return render_template('menu_detail/coffee04.html')


@bp.route('/coffee05/')
def _coffee05():
    return render_template('menu_detail/coffee05.html')


@bp.route('/juice01/')
def _juice01():
    return render_template('menu_detail/juice01.html')


@bp.route('/juice02/')
def _juice02():
    return render_template('menu_detail/juice02.html')


@bp.route('/juice03/')
def _juice03():
    return render_template('menu_detail/juice03.html')


@bp.route('/tea01/')
def _tea01():
    return render_template('menu_detail/tea01.html')


@bp.route('/tea02/')
def _tea02():
    return render_template('menu_detail/tea02.html')


@bp.route('/cake01/')
def _cake01():
    return render_template('menu_detail/cake01.html')


@bp.route('/cake02/')
def _cake02():
    return render_template('menu_detail/cake02.html')


@bp.route('/cake03/')
def _cake03():
    return render_template('menu_detail/cake03.html')


@bp.route('/cookie01/')
def _cookie01():
    return render_template('menu_detail/cookie01.html')


@bp.route('/cookie02/')
def _cookie02():
    return render_template('menu_detail/cookie02.html')
