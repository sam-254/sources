from store.core.model import Base
from store.core.mixins import *
from store.extensions import *


class Image(Base, DateTimeMixin):
    __category__ = 'Image'

    alt_text = db.Column(db.String)
    original_src = db.Column(db.String)
    transformed_src = db.Column(db.String)
    crop = db.Column(db.Integer, db.ForeignKey('cropregion.id'))  # INTEGER  JSON_STRING STRING
    max_height = db.Column(db.Integer)
    max_width = db.Column(db.Integer)
    image_content_type = db.Column(db.Integer, db.ForeignKey('imagetype.id'))  # JPG PNG WEBP
    scale = db.Column(db.Integer)
