from store.core.model import Base
from store.extensions import *


class Imagetype(Base):
    __category__ = 'Image'

    image_type = db.Column(db.String)  # JPG PNG WEBP
    images = db.relationship('Image', backref='imagetype', lazy=True)
