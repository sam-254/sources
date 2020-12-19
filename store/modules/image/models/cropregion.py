from store.core.model import Base
from store.extensions import *


class Cropregion(Base):
    __category__ = 'Image'

    name = db.Column(db.String)
    images = db.relationship('Image', backref='cropregion', lazy=True)
