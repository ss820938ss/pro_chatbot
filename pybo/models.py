from pybo import db


# 상품
class Categories(db.Model):
    categoryId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)


class Products(db.Model):
    productId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(200), nullable=False)
    image = db.Column(db.String(200), nullable=False)
    stock = db.Column(db.Integer, nullable=False)

    categoryId = db.Column(db.Integer, db.ForeignKey('categories.categoryId', ondelete='CASCADE'), nullable=True)


class Cart(db.Model):
    __table_name__ = 'Cart'
    __table_args__ = {'sqlite_autoincrement': True}
    cartId = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    userId = db.Column(db.Integer, nullable=True)
    productId = db.Column(db.Integer, nullable=True)
    qty = db.Column(db.Integer, nullable=True)
    price = db.Column(db.Integer, nullable=True)
    image = db.Column(db.String(200), nullable=True)
    name = db.Column(db.String(200),  nullable=True)


# 회원관리
class Admin(db.Model):
    adminId = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    phone = db.Column(db.String(30), nullable=False)


class Users(db.Model):
    userId = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    phone = db.Column(db.String(30), nullable=False)


# 게시판
class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)

    user_id = db.Column(db.String(200), db.ForeignKey('users.userId', ondelete='CASCADE'), nullable=True)
    user = db.relationship('Users', backref=db.backref('question_set'))


class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'))
    question = db.relationship('Question', backref=db.backref('answer_set'))
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)

    user_id = db.Column(db.String(200), db.ForeignKey('users.userId', ondelete='CASCADE'), nullable=True)
    user = db.relationship('Users', backref=db.backref('answer_set'))



