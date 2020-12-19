from store.core.model import Base
from store.extensions import db


class Pricerange(Base):
    __category__ = 'Product'

    max_variant_price = db.Column(db.Float)
    min_variant_price = db.Column(db.Float)
    product = db.Column(db.Integer, db.ForeignKey('product.id'))
