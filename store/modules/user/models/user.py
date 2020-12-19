import jwt
import datetime

from passlib.hash import pbkdf2_sha256 as sha256

from store.config import config
from store.core.model import Base
from store.core.mixins import *
from store.core.tables.user import *


class User(Base, NameMixin, DateTimeMixin):
    __tablename__ = 'user'
    __category__ = 'User'

    email = db.Column(db.String)
    password_hash = db.Column(db.String)
    age = db.Column(db.Integer)
    roles = db.relationship('Role', secondary=roles_users_relation,
                            backref=db.backref('users', uselist=False)),
    my_friends = db.relationship(
        "User",
        secondary=friend_relation,
        primaryjoin='User.id==friend_relation.c.my_id',
        secondaryjoin='User.id==friend_relation.c.my_friends_id',
        lazy='dynamic')
    best_friend = db.relationship(
        "User",
        secondary=best_fried_relation,
        primaryjoin='User.id==best_fried_relation.c.my_id',
        secondaryjoin='User.id==best_fried_relation.c.my_friends_id',
        uselist=False, )

    def add_node(self, node):
        self.right_nodes.append(node)

    @classmethod
    def get_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    @property
    def password(self):
        raise AttributeError('password: write-only field')

    @password.setter
    def password(self, password):
        self.password_hash = sha256.hash(password)

    def check_password(self, password):
        return sha256.verify(password, self.password_hash)

    @staticmethod
    def encode_auth_token(user_id, remember_me=False):
        try:
            day = 30 if remember_me else 1
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=day, seconds=14),
                'iat': datetime.datetime.utcnow(),
                'sub': user_id
            }
            return jwt.encode(
                payload,
                config.SECRET_KEY,
                algorithm='HS256'
            )
        except Exception as e:
            return e

    @staticmethod
    def decode_auth_token(auth_token):
        try:
            payload = jwt.decode(auth_token, config.SECRET_KEY)
            return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'
