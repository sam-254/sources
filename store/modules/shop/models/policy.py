from store.extensions import db
from store.core.model import Base


class Policy(Base):
    __category__ = 'Policy'

    body = db.Column(db.String)
    handle = db.Column(db.String)
    title = db.Column(db.String)
    url = db.Column(db.String)


class Privacy(Policy):
    shop = db.relationship('Shop', lazy=True, uselist=True,
                           backref=db.backref('privacy_policy', uselist=False))


class Refund(Policy):
    shop = db.relationship('Shop', lazy=True, uselist=True,
                           backref=db.backref('refund_policy', uselist=False))


class Service(Policy):
    shop = db.relationship('Shop', lazy=True, uselist=True,
                           backref=db.backref('terms_of_service', uselist=False))
