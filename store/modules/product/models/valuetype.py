from store.core.model import Base
from store.extensions import db


class Valuetype(Base):
    __category__ = 'Product'

    value = db.Column(db.String)
    metafields = db.relationship('Metafield', backref='valuetype', lazy=True)
