from pybo import db


class Menu(db.Model):
    menu_no = db.Column(db.Integer, primary_key=True)
    menu_name = db.Column(db.String(200), nullable=False)
    menu_price = db.Column(db.Integer, nullable=False)
    menu_kate = db.Column(db.String(200), nullable=False)


class Admin(db.Model):
    ad_no = db.Column(db.Integer, primary_key=True)
    ad_id = db.Column(db.String(200), nullable=False)
    ad_name = db.Column(db.String(200), nullable=False)
    ad_email = db.Column(db.String(200), nullable=False)
    ad_password = db.Column(db.String(200), nullable=False)


class Member(db.Model):
    no = db.Column(db.Integer, primary_key=True)
    id = db.Column(db.String(200), nullable=False)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)

    user_id = db.Column(db.String(200), db.ForeignKey('member.id', ondelete='CASCADE'), nullable=True)
    user = db.relationship('Member', backref=db.backref('question_set'))


class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'))
    question = db.relationship('Question', backref=db.backref('answer_set'))
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)

    user_id = db.Column(db.String(200), db.ForeignKey('member.id', ondelete='CASCADE'), nullable=True)
    user = db.relationship('Member', backref=db.backref('answer_set'))


class Order(db.Model):
    order_id = db.Column(db.Integer, primary_key=True)
    product = db.Column(db.Integer, db.ForeignKey('menu.menu_no', ondelete='CASCADE'), nullable=True)
    quantity = db.Column(db.Integer, nullable=True)
    order_price = db.Column(db.Integer, db.ForeignKey('menu.menu_price', ondelete='CASCADE'), nullable=True)