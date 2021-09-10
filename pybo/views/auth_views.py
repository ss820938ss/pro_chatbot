import sqlite3

from flask import Blueprint, url_for, render_template, flash, request, session, g
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect

from pybo import db
from pybo.forms import UsersCreateForm, UsersLoginForm, UsersModifyForm, UsersPassModifyForm
from pybo.models import Users
import functools
import sys

import sqlite3, hashlib, os

bp = Blueprint('auth', __name__, url_prefix='/auth')


# 회원가입
@bp.route('/signup/', methods=('GET', 'POST'))
def signup():
    form = UsersCreateForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if not user:
            user = Users(
                email=form.email.data,
                password=str(generate_password_hash(form.password1.data)),
                name=form.name.data,
                address=form.address.data,
                phone=form.phone.data)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('main.index'))
        else:
            flash('이미 존재하는 사용자입니다.')
    return render_template('auth/join.html', form=form)


# 로그인
@bp.route('/login/', methods=('GET', 'POST'))
def login():
    form = UsersLoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        error = None
        user = Users.query.filter_by(email=form.email.data).first()
        # print("========444444",hash ,  user.password, file=sys.stderr)

        if not user:
            error = "존재하지 않는 사용자입니다."
        elif not check_password_hash(user.password, form.password.data):
            error = "비밀번호가 올바르지 않습니다."
        if error is None:
            session.clear()
            session['user_id'] = user.email
            return redirect(url_for('main.index'))
        flash(error)
    return render_template('auth/login.html', form=form)


# 회원정보 유지
@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = Users.query.get(user_id)


# 로그아웃
@bp.route('/logout/')
def logout():
    session.clear()
    return redirect(url_for('main.index'))


# 로그인 안했을때 접근금지
def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        user = session.get('user_id')
        if user is None:
            return redirect(url_for('auth.login'))
        return view(**kwargs)

    return wrapped_view


# 회원정보 확인
user = None


@bp.route('/mypage/', methods=('GET', 'POST'))
@login_required
def mypage():
    if request.method == 'GET':
        global user
        user = Users.query.filter_by(email=session.get('user_id')).first()

    return render_template('auth/mypage.html', form=request, user=user)


# 회원정보 수정
@bp.route('/mypage/modify', methods=('GET', 'POST'))
@login_required
def mypage_modify():
    form = UsersModifyForm(request.form)
    # print("========", session.get('user_id'), file=sys.stderr)
    if request.method == 'POST':
        global user
        user = db.session.query(Users).filter_by(email=session.get('user_id')).first()
        # print("========111", user.email, file=sys.stderr)
        user.email = session.get('user_id')
        user.name = form.name.data
        user.address = form.address.data
        user.phone = form.phone.data

        db.session.commit()
        # print("========3333", user.name, file=sys.stderr)
    else:
        flash('회원정보 수정 중 오류가 발생했습니다')

    return render_template('auth/modify.html', form=form, users=user)


# 회원탈퇴
@bp.route('/delete/', methods=('GET', 'POST'))
@login_required
def delete():
    if request.method == 'GET':
        global user
        user = db.session.query(Users).filter_by(email=session.get('user_id')).first()
        # print("========3333", user.email, file=sys.stderr)
        db.session.delete(user)
        db.session.commit()
        session.clear()
        return redirect(url_for('main.index'))
    else:
        flash('탈퇴 중 오류가 발생했습니다.')

    return render_template('auth/delete.html', users=user)


# 비밀번호 변경
@bp.route("/changePassword/", methods=["GET", "POST"])
@login_required
def changePassword():
    form = UsersPassModifyForm(request.form)

    # print("******", form.password.data)
    if request.method == "POST":
        global user
        user = db.session.query(Users).filter_by(email=session.get('user_id')).first()
        # print("========3333", form.password.data, user.password, file=sys.stderr)
        user.email = session.get('user_id')
        hash = str(generate_password_hash(form.password.data))
        user.password = hash
        # print("========33332", hash,  user.password, file=sys.stderr)
        db.session.commit()
    else:
        flash('비밀번호 수정 중 오류가 발생했습니다')

    return render_template('auth/changePassword.html', form=form, users=user)
