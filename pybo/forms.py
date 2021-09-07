from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Email


# 회원가입
class UsersCreateForm(FlaskForm):
    email = EmailField('이메일', validators=[Email(), DataRequired(), Length(min=5, max=30)])
    password1 = PasswordField('비밀번호', validators=[
        DataRequired(), EqualTo('password2', '비밀번호가 일치하지 않습니다')])
    password2 = PasswordField('비밀번호확인', validators=[DataRequired()])
    name = StringField('사용자이름', validators=[DataRequired(), Length(min=3, max=25)])
    address = StringField('주소', validators=[DataRequired(), Length(min=3, max=200)])
    phone = StringField('휴대폰', validators=[DataRequired(), Length(min=3, max=15)])


# 로그인
class UsersLoginForm(FlaskForm):
    email = EmailField('이메일', validators=[Email(), DataRequired(), Length(min=5, max=30)])
    password = PasswordField('비밀번호', validators=[DataRequired()])


# 회원수정
class UsersModifyForm(FlaskForm):
    email = EmailField('Email Address', validators=[DataRequired(), Email()])
    name = StringField('사용자이름', validators=[DataRequired(), Length(min=3, max=25)])
    address = StringField('주소', validators=[DataRequired(), Length(min=3, max=200)])
    phone = StringField('휴대폰', validators=[DataRequired(), Length(min=3, max=15)])


# 비밀번호 수정
class UsersPassModifyForm(FlaskForm):
    email = EmailField('Email Address', validators=[DataRequired(), Email()])
    password = PasswordField('비밀번호', validators=[DataRequired()])


# 게시판
class QuestionForm(FlaskForm):
    subject = StringField('제목', validators=[DataRequired('제목은 필수입력 항목입니다.')])
    content = TextAreaField('내용', validators=[DataRequired('내용은 필수입력 항목입니다.')])


class AnswerForm(FlaskForm):
    content = TextAreaField('내용', validators=[DataRequired('내용은 필수입력 항목입니다.')])





# 비밀번호 요청 양식 재설정
class ResetPasswordRequestForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')
