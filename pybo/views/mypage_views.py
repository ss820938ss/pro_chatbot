from flask import Blueprint, url_for, render_template, flash, request, session, g
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect

from pybo import db
from pybo.forms import MemberCreateForm, MemberLoginForm
from pybo.models import Member
import functools


bp = Blueprint('mypage', __name__, url_prefix='/mypage')


@bp.route('/mypage/', methods=('GET', 'POST'))
def signup():
    form = MemberCreateForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = Member.query.filter_by(id=form.id.data).first()
        if not user:
            user = Member(
                id=form.id.data,
                name=form.name.data,
                password=generate_password_hash(form.password1.data),
                email=form.email.data)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('main.index'))
        else:
            flash('이미 존재하는 사용자입니다.')
    return render_template('auth/signup.html', form=form)