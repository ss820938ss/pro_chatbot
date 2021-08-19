from flask import Blueprint, render_template

from pybo.models import Question
from pybo.models import Admin, Member, Menu, Question


bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo!'


@bp.route('/')
def index():
    menu_list = Menu.query.order_by(Menu.menu_no)
    return render_template('menu/menu_list.html', menu_list=menu_list, image_file="image/test1.jpg")


@bp.route('/detail/<int:menu_no>/')
def detail(menu_no):
    menu_detail = Menu.query.get(menu_no)
    return render_template('menu/menu_detail.html', menu_detail=menu_detail)
