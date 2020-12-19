from store.core.model import Base
from store.extensions import db


class Domain(Base):
    __category__ = 'Shop'

    host = db.Column(db.String)
    ssl_enabled = db.Column(db.Boolean)
    url = db.Column(db.String)
    shops = db.relationship('Shop', lazy=True, uselist=True,
                            backref=db.backref('domain', uselist=True))
