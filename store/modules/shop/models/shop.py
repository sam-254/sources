from store.core.model import Base
from store.core.mixins import *
from store.core.tables.shop import *


class Shop(Base, DateTimeMixin):
    __category__ = 'Shop'

    description = db.Column(db.String)
    money_format = db.Column(db.String)
    name = db.Column(db.String)
    shopify_payments_account_id = db.Column(db.String)
    domains = db.Column(db.Integer, db.ForeignKey('domain.id'))
    privacy_polices = db.Column(db.Integer, db.ForeignKey('policy.id'))
    ship_to_countries = db.relationship('Country', secondary=shops_shipcountries_relation,
                                        backref=db.backref('shops', lazy='dynamic'))
