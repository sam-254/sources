from store.core.model import Base
from store.extensions import db


class Option(Base):
    __category__ = 'Product'

    name = db.Column(db.String)
