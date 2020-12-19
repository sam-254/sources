from store.core.model import Base
from store.extensions import db
from store.core.mixins import DateTimeMixin
from store.core.tables.product import metafield_self_relation


class Metafield(Base, DateTimeMixin):
    __category__ = 'Product'

    description = db.Column(db.String)
    key = db.Column(db.String)
    namespace = db.Column(db.String)
    value = db.Column(db.String)
    parent_resource = db.relationship(
        "Metafield",
        secondary=metafield_self_relation,
        primaryjoin='Metafield.id==metafield_relation.c.my_id',
        secondaryjoin='Metafield.id==metafield_relation.c.my_parent_id',
        uselist=False
    )
    product = db.Column(db.Integer, db.ForeignKey('product.id'))
    value_type = db.Column(db.Integer, db.ForeignKey('valuetype.id'))  # INTEGER  JSON_STRING STRING
    variant_option = db.Column(db.Integer, db.ForeignKey('variantoptions.id'))
