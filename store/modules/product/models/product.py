from store.core.model import Base
from store.core.mixins import *
from store.core.tables.product import *
from store.extensions import db


class Product(Base, DateTimeMixin):
    __category__ = 'Product'

    sku = db.Column(db.String(255), nullable=False)
    title = db.Column(db.String)
    key = db.Column(db.String(30))  # required
    product_type = db.Column(db.String)
    description = db.Column(db.String)
    handle = db.Column(db.String)  # auto generate from title . like Black Shirt --> Black-Shirt
    descriptionHtml = db.Column(db.String)
    vendor = db.Column(db.String)
    namespace = db.Column(db.String(20), nullable=False)
    taxable = db.Column(db.Boolean(), default=False)
    available_for_sale = db.Column(db.Boolean(), default=False)
    total_inventory = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime(), default=db.func.now())
    updated_at = db.Column(db.DateTime(), onupdate=db.func.now(), default=db.func.now())
    metafields = db.relationship('Metafield', backref='prod', uselist=True)
    price_range = db.relationship('Pricerange', backref='pricerange', uselist=True)
    options = db.relationship('Option', secondary=options_products_relation,
                              backref=db.backref('products', lazy='dynamic'))
    tags = db.relationship('Tag', secondary=tags_products_relation,
                           backref=db.backref('products', lazy='dynamic'))
    selected_options = db.relationship('Selectedinput', secondary=selected_options_products_relation,
                                       backref=db.backref('products', lazy='dynamic'))
    variant_by_selected_options = db.relationship('Variantoptions', lazy=True, uselist=True,
                                                  backref=db.backref('products', uselist=True))

    @classmethod
    def get_by_sku(cls, sku):
        return cls.query.filter_by(sku=sku).first()
