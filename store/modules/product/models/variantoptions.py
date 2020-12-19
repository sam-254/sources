from store.core.model import Base
from store.extensions import db
from store.core.tables.product import variants_options_relation, images_options_relation


class Variantoptions(Base):
    __category__ = 'Product'

    available_for_sale = db.Column(db.Boolean, default=False)
    currently_not_in_stock = db.Column(db.Boolean)
    requires_shipping = db.Column(db.Boolean)
    quantity_available = db.Column(db.Integer)
    compare_at_price = db.Column(db.Float)
    unit_price = db.Column(db.Float)
    weight = db.Column(db.Float)
    price = db.Column(db.Float)
    namespace = db.Column(db.String)
    title = db.Column(db.String)
    sku = db.Column(db.String)
    key = db.Column(db.String)
    selected_options = db.relationship('Option', secondary=variants_options_relation,
                                       backref=db.backref('variantoptions', lazy='dynamic'))
    images = db.relationship('Image', secondary=images_options_relation,
                             backref=db.backref('variantoptions', lazy='dynamic'))
    metafield = db.relationship('Metafield', backref='variant_options', lazy=True, uselist=True)
    product = db.Column(db.Integer, db.ForeignKey('product.id'))
