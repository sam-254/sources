from store.core.model import Base
from store.extensions import db


class Selectedinput(Base):
    __category__ = 'Product'

    name = db.Column(db.String)
    value = db.Column(db.String)
