from app import db
from sqlalchemy import or_
from app.v1.generic.constant.role_constant import ROLE_USER


class User(db.Model):
    __tablename__ = 'user'

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(600), nullable=False)
    role = db.Column(db.String(10), nullable=False)
    balance = db.Column(db.Integer(), nullable=False)
    name = db.Column(db.String(60), nullable=False)
    picture = db.Column(db.String(300))
    phone = db.Column(db.String(11))
    email = db.Column(db.String(100))

    def __init__(self, username, password, name, phone, email):
        self.username = username
        self.password = password
        self.name = name
        self.phone = phone
        self.email = email
        self.role = ROLE_USER
        self.balance = 0
        self.picture = ''

    def save(self):
        record = db.session.add(self)
        db.session.commit()
        return record

    @classmethod
    def find_users(cls):
        return cls.query.all()

    @classmethod
    def find_existing_user(cls, username, phone, email):
        return cls.query.filter(or_(cls.username == username, cls.phone == phone, cls.email == email)).first()

    @classmethod
    def find_user_by_username(cls, username):
        return cls.query.filter_by(username=username).first()
