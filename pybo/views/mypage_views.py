from flask import Blueprint, url_for, render_template, flash, request, session
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect

from pybo import db
from .auth_views import login_required
from ..forms import MemberModifyform
from pybo.models import Member

# bp = Blueprint('mypage', __name__, url_prefix='/mypage')
#
#
# @bp.route('/mypage/<str:id>', methods=('GET', 'POST'))
# @login_required
# def get_profile():
#     profile = Member.query.get_or_404(Member.id)
#     if session.get('user_id') != profile.id:
#         flash('조회권한이 없습니다.')
#         return redirect(url_for('main.index', id=profile.id))
#     if request.method == 'POST':
#         form = MemberModifyform()
#         if form.validate_on_submit():
#             form.populate_obj(profile)
#             db.session.commit()
#             return redirect(url_for('mypage.get_profile', id=profile.id))
#     else:
#         form = MemberModifyform(obj=profile)
#     return render_template('mypage/mypage.html', id=id, form=form)
