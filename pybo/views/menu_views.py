from flask import Blueprint, render_template

from pybo.models import Admin, Member, Menu


bp = Blueprint('menu', __name__, url_prefix='/menu')


@bp.route('/list/')
def _list():
    menu_list = Menu.query.order_by(Menu.menu_no)
    return render_template('menu/menu_list.html', menu_list=menu_list, image_file="image/test1.jpg")


@bp.route('/detail/<int:menu_no>/')
def detail(menu_no):
    menu_detail = Menu.query.get_or_404(menu_no)
    return render_template('menu/menu_detail.html', menu_detail=menu_detail)